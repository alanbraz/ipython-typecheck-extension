"""Experimental packege for IPython extension."""
from .typecheck import TypeCheck
from .autotime import timer


def load_ipython_extension(ipython):
    ipython.events.register('pre_run_cell', timer.start)
    ipython.events.register('post_run_cell', timer.stop)
    ipython.register_magics(TypeCheck)


def unload_ipython_extension(ipython):
    ipython.events.unregister('pre_run_cell', timer.start)
    ipython.events.unregister('post_run_cell', timer.stop)
