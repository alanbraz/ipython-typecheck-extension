from .typecheck import TypeCheck

from IPython.core.magics.execution import _format_time as format_delta
import time
from __future__ import print_function

class LineWatcher(object):
    """
    Class that implements a basic timer.
    Register the `start` and `stop` methods with the IPython events API.
    """
    def __init__(self):
        self.start_time = 0.0

    def start(self):
        self.start_time = time.time()

    def stop(self):
        stop_time = time.time()
        if self.start_time:
            diff = stop_time - self.start_time
            assert diff > 0
            print('time: {}'.format(format_delta(diff)))

timer = LineWatcher()

def load_ipython_extension(ipython):
    ipython.events.register('pre_run_cell', timer.start)
    ipython.events.register('post_run_cell', timer.stop)
    ipython.register_magics(TypeCheck)

def unload_ipython_extension(ipython):
    ipython.events.unregister('pre_run_cell', timer.start)
    ipython.events.unregister('post_run_cell', timer.stop)
