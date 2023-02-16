# -*- coding: utf-8 -*-
"""
@Author  : miclon
@Time    : 2022/9/6
@Desc    : 字符串导入模块
@Example
    process:
    import_object('this')

    output:
    The Zen of Python, by Tim Peters
    ……

"""
import functools
import importlib


def import_object(value: str):
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


class LazyImport(object):
    def __init__(self, name):
        self.cache = {}
        self.mod_name = name

    def __getattr__(self, name):
        mod = self.cache.get(self.mod_name)
        if not mod:
            mod = importlib.import_module(self.mod_name)
            self.cache[self.mod_name] = mod
        return getattr(mod, name)
