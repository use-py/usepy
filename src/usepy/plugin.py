import functools
import importlib
import os
import site
from glob import glob


def find_plugin_modules():
    plugins = []
    for module_path in site.getsitepackages():
        for file in glob(
                # 兼容老版本模块
                os.path.join(module_path, "usepy_plugin_*")) + glob(
                os.path.join(module_path, "use_*")
        ):
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
