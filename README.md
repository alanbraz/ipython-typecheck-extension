# ipython-typecheck-extension

From this [tutorial](http://journalpanic.com/post/spice-up-thy-jupyter-notebooks-with-mypy/) that customizes IPython notebook with `magic` commands, this repo implements the same feature but using an [extension](http://ipython.readthedocs.io/en/stable/config/extensions/index.html).

In addition, it runs the `typecheck` not only at the current cell, but in all previous cells. So if a variable is defined as integer in the first cell and you try to assign a string value to it in a second cell, it should fail.

## Notebook example
