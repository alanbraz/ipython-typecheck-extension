"""
Add mypy type-checking cell magic to jupyter/ipython.
Save this script to your ipython profile's startup directory.
IPython's directories can be found via `ipython locate [profile]` to find the current ipython directory and ipython profile directory, respectively.
For example, this file could exist on a path like this on mac:
/Users/yourusername/.ipython/profile_default/startup/typecheck.py
where /Users/yourusername/.ipython/profile_default/ is the ipython directory for
the default profile.
The line magic is called "typecheck" to avoid namespace conflict with the mypy
package.
"""
class TypeCheck(object):
    """
    Class that implements a basic timer.
    """
    def __init__(self, ip):
        self.shell = ip
        self.last_x = None

    def pre_execute(self):
        self.last_x = self.shell.user_ns.get('x', None)

    def pre_run_cell(self, info):
        print('Cell code: "%s"' % info.raw_cell)

    def post_execute(self):
        if self.shell.user_ns.get('x', None) != self.last_x:
            print("x changed!")

    def post_run_cell(self, result):
        print('Cell code: "%s"' % result.info.raw_cell)
        if result.error_before_exec:
            print('Error before execution: %s' % result.error_before_exec)

    def check(self, info):
        print("typecheck...")
        """
        Run the following cell though mypy.
        Any parameters that would normally be passed to the mypy cli
        can be passed on the first line, with the exception of the
        -c flag we use to pass the code from the cell we want to execute
         i.e.
        %%typecheck --ignore-missing-imports
        ...
        ...
        ...
        mypy stdout and stderr will print prior to output of cell. If there are no conflicts,
        nothing will be printed by mypy.
        """

        # from IPython import get_ipython
        from mypy import api
        import sys

        # inserting a newline at the beginning of the cell
        # ensures mypy's output matches the the line
        # numbers in jupyter
        print('Cell code: "%s"' % info.raw_cell)
        cell = info.raw_cell
        mycell = '\n' + cell
        mypy_result = api.run(['-c', mycell] + line.split())

        if mypy_result[0]:
            print(mypy_result[0], file=sys.stderr)
        if mypy_result[1]:
            print(mypy_result[1], file=sys.stderr)
