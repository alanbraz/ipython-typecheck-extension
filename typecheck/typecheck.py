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
        cells_to_run = "\n".join(self.ok_cells + [current_cell])
        # print("cells_to_run", cells_to_run)
        mypy_result = api.run(['-c', cells_to_run, '--ignore-missing-imports'])
        error = None
        if mypy_result[0]:
            error = mypy_result[0]
        if mypy_result[1]:
            error = mypy_result[1]
        print("error", error)
        if error is not None or error != '':
            print("TypeCheck: " + error, file=sys.stderr)
        else:
            self.ok_cells.append(current_cell)
