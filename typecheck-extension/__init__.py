"""Experimental packege for IPython extension."""
from .typecheck import TypeCheck
from .autotime import timer


def load_ipython_extension(ipython):
    # ipython.events.register('pre_run_cell', typecheck.check)
    ipython.events.register('pre_run_cell', timer.start)
    ipython.events.register('post_run_cell', timer.stop)
    tc = TypeCheck(ipython)
    ipython.events.register('pre_execute', tc.pre_execute)
    ipython.events.register('pre_run_cell', tc.pre_run_cell)
    ipython.events.register('pre_run_cell', tc.check)
    ipython.events.register('post_execute', tc.post_execute)
    ipython.events.register('post_run_cell', tc.post_run_cell)


def unload_ipython_extension(ipython):
    ipython.events.unregister('pre_run_cell', timer.start)
    ipython.events.unregister('post_run_cell', timer.stop)
