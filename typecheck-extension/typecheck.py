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

from IPython.core.magic import (Magics, magics_class, line_magic, cell_magic)
import sys

@magics_class
class TypeCheck(Magics):

    @line_magic
    def linelen(self, line):
        "my line magic"
        return len(line)

    @cell_magic
    def typecheck(self, line, cell):
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

        # inserting a newline at the beginning of the cell
        # ensures mypy's output matches the the line
        # numbers in jupyter

        mycell = '\n' + cell

        mypy_result = api.run(['-c', mycell] + line.split())
        print("typecheck...")

        if mypy_result[0] or mypy_result[1]:  # print mypy stdout
            if mypy_result[0]:
                print(mypy_result[0], file=sys.stderr)
            if mypy_result[1]:
                print(mypy_result[1], file=sys.stderr)
        else:
            return cell
            # shell = get_ipython()
            # shell.run_cell(cell)
