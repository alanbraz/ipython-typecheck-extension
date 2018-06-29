"""Experimental packege for IPython extension."""
from .typecheck import TypeCheck
from .autotime import timer


class VarWatcher(object):
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

def load_ipython_extension(ipython):
    # ipython.events.register('pre_run_cell', typecheck.check)
    ipython.events.register('pre_run_cell', timer.start)
    ipython.events.register('post_run_cell', timer.stop)
    tc = TypeCheck(ipython)
    ipython.events.register('pre_run_cell', tc.check)
    vw = VarWatcher(ipython)
    ipython.events.register('pre_execute', vw.pre_execute)
    ipython.events.register('pre_run_cell', vw.pre_run_cell)
    ipython.events.register('post_execute', vw.post_execute)
    ipython.events.register('post_run_cell', vw.post_run_cell)


def unload_ipython_extension(ipython):
    ipython.events.unregister('pre_run_cell', timer.start)
    ipython.events.unregister('post_run_cell', timer.stop)
