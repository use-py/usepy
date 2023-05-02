"""
    @Author: MicLon
    @Date: 2023/02/19
    @Description: 用于检查数据类型的工具函数
"""
import re


def useIsToken(value) -> bool:
    """
    检查`value`是否符合token规范
    :param value: 要检查的值
    :return:
    """
    return bool(re.match('^[A-Za-z0-9]{3,32}$', value))


def useIsString(value) -> bool:
    """
    检查`value`是否是字符串
    :param value: 要检查的值
    :return: bool
    """
    return isinstance(value, (str, bytes))


def useIsRegexp(value) -> bool:
    """
    检查`value`是否是正则表达式
    :param value: 要检查的值
    :return:
    """
    return isinstance(value, type(re.compile("regex_test")))
