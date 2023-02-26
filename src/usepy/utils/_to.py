"""
    @Author: MicLon
    @Date: 2023/02/19
    @Description: 用于转换数据类型的工具函数
"""
import hashlib
import re
from typing import Any, AnyStr


def string(data: Any) -> str:
    """
    将任意数据转换为字符串
    :param data: data
    :return: string
    """
    if isinstance(data, str):
        return data
    if isinstance(data, bytes):
        return data.decode()
    return str(data)


def md5(data: AnyStr) -> str:
    """
    将字符数据转换为md5
    :param data: data
    :return: md5
    """
    return hashlib.md5(string(data).encode()).hexdigest()


def sha1(data: AnyStr) -> str:
    """
    将字符数据转换为sha1
    :param data: data
    :return: sha1
    """
    return hashlib.sha1(string(data).encode()).hexdigest()


def camel(data: str, char: str = '-') -> str:
    """
    将字符数据转换为驼峰命名
    :param data: data
    :param char: 特征字符，如：-、_
    :return:
    >>> camel("test")
    'test'
    >>> camel("test-case")
    'testCase'
    >>> camel("test_case", char="_")
    'testCase'
    """
    return re.sub(char + r'(\w)', lambda m: m.group(1).upper(), data)


def snake(data: str, char: str = '_') -> str:
    """
    将字符数据转换为下划线命名
    :param data: data
    :param char: 特征字符，如：-、_
    :return:
    >>> snake("test")
    'test'
    >>> snake("testCase")
    'test_case'
    >>> snake("testCase", char="-")
    'test-case'
    """
    return re.sub(r'([A-Z])', lambda m: char + m.group(1).lower(), data)
