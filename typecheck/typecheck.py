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
    Class that implements mypy call.
    """
    def __init__(self, ip):
        self.shell = ip

    def check(self, info):
        # print("typecheck...")
        from mypy import api
        import sys
        """
        Run the following cell though mypy.
        Any parameters that would normally be passed to the mypy cli
        can be passed on the first line, with the exception of the
        -c flag we use to pass the code from the cell we want to execute
        mypy stdout and stderr will print prior to output of cell.
        If there are no conflicts, mnothing will be printed by mypy.
        """
        mycell = info.raw_cell
        # TODO send all previous code cells, instead of current cell
        mypy_result = api.run(['-c', mycell, '--ignore-missing-imports'])
        if mypy_result[0]:
            print("TypeCheck: " + mypy_result[0], file=sys.stderr)
        if mypy_result[1]:
            print("TypeCheck: " + mypy_result[1], file=sys.stderr)

        # TODO try to abort cell to run if typecheck error, return False or return None, None don't work
