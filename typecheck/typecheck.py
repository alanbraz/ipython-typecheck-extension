class TypeCheck(object):

    def __init__(self, ip):
        self.shell = ip
        self.ok_cells = []

    def check(self):
        # print("typecheck...")
        from mypy import api
        import sys
        cells = self.shell.user_ns["In"]
        # print("cells", cells)
        current_cell = cells[-1]
        # print("current_cell", current_cell)
        current_cell_lines = []
        for line in current_cell.split("\n"):
            # ignore magic commands
            if "get_ipython" not in line:
                current_cell_lines.append(line)
        if len(current_cell_lines) > 0:
            current_cell = "\n".join(current_cell_lines)
            cells_to_run = "\n".join(self.ok_cells + [current_cell])
            # print("cells_to_run", cells_to_run)
            mypy_result = api.run(['-c', cells_to_run, '--ignore-missing-imports'])
            error = None
            if mypy_result[0]:
                error = mypy_result[0]
            if mypy_result[1]:
                error = mypy_result[1]
            if error is not None:
                parts = error.split(":")
                line = int(parts[1])
                parts[1] = str(line - len(("\n".join(self.ok_cells)).split("\n")))
                error = (":").join(parts)
                print("TypeCheck: " + error, file=sys.stderr)
            else:
                self.ok_cells.append(current_cell)
