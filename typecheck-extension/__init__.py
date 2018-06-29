from .typecheck import typecheck

def load_ipython_extension(ipython):
    # The `ipython` argument is the currently active `InteractiveShell`
    # instance, which can be used in any way. This allows you to register
    # new magics or aliases, for example.
    ipython.register_magics(typecheck)

def unload_ipython_extension(ipython):
    # If you want your extension to be unloadable, put that logic here.
