# -*- coding: utf-8 -*-
"""
@Author  : miclon
@Time    : 2022/9/6
@Desc    : 字符串导入模块
@Example
    process:
    useImport('this')

    output:
    The Zen of Python, by Tim Peters
    ……

"""
import functools
import importlib
from types import ModuleType


def useImport(value: str):
    """
    字符串动态导入模块
    :param value: 字符串路径
    :return:
    """
    modname, var = value, None
    if ":" in value:
        modname, var = value.split(":", 1)

    module = importlib.import_module(modname)
    if var is not None:
        var_lst = var.split(".")
        try:
            return module, functools.reduce(getattr, var_lst, module)
        except AttributeError:
            raise ImportError("Module %r does not define a %r variable." % (modname, var)) from None
    return module, None


class useLazyImport(ModuleType):
    def __init__(self, name, module_globals=None):
        if module_globals is None:
            module_globals = globals()
        self._mod_name = name
        self._module_globals = module_globals
        super(useLazyImport, self).__init__(name)

    def _load(self):
        module = importlib.import_module(self.__name__)
        self._module_globals[self._mod_name] = module
        self.__dict__.update(module.__dict__)
        return module

    def __getattr__(self, item):
        return getattr(self._load(), item)

    def __dir__(self):
        return dir(self._load())

    def __repr__(self):
        return f"<useLazyImport {self.__name__}>"
