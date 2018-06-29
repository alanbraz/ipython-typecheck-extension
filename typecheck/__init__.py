"""Experimental packege for IPython extension."""
from .typecheck import TypeCheck
from .autotime import timer

__version__ = "0.2"

class VarWatcher(object):
    def __init__(self, ip):
        self.shell = ip

    def pre_run_cell(self, info):
        print('Cell code: "%s"' % info.raw_cell)
        print("info", info)

    def post_run_cell(self, result=None):
        if result is not None:
            print('Cell code: "%s"' % result.info.raw_cell)
            if result.error_before_exec:
                print('Error before execution: %s' % result.error_before_exec)
        else:
            print("No result.")

def load_ipython_extension(ipython):
    # ipython.events.register('pre_run_cell', typecheck.check)
    ipython.events.register('pre_run_cell', timer.start)
    ipython.events.register('post_run_cell', timer.stop)
    tc = TypeCheck(ipython)
    ipython.events.register('pre_run_cell', tc.check)
    vw = VarWatcher(ipython)
    ipython.events.register('pre_run_cell', vw.pre_run_cell)
    ipython.events.register('post_run_cell', vw.post_run_cell)


def unload_ipython_extension(ipython):
    ipython.events.unregister('pre_run_cell', timer.start)
    ipython.events.unregister('post_run_cell', timer.stop)
