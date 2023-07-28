import functools
import importlib
import os
import sys
from glob import glob


def find_plugin_modules():
    plugins = []
    for module in sys.path:
        path = os.path.join(os.path.dirname(__file__), module)
        for file in glob(os.path.join(path, 'usepy_plugin_*')):
            path_name = os.path.basename(file)
            try:
                plugins.append(importlib.import_module(path_name))
            except ModuleNotFoundError:
                pass
    return plugins


plugin_modules = find_plugin_modules()


def __getattr__(name):
    for pm in plugin_modules:
        if not hasattr(pm, name):
            continue
        return functools.reduce(getattr, [name], pm)
    else:
        raise ModuleNotFoundError(f"module `{__name__}` has no function `{name}`")
