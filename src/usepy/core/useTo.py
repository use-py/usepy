import hashlib
import re
from typing import AnyStr, Optional

from usepy.vars import EMPTY_VALUES


def useToString(s, encoding=None, errors='strict'):
    """
    将 bytes 或者 bytearray 转换为 str
    :param s: bytes 或者 bytearray
    :param encoding: 编码
    :param errors: 错误处理
    :return: str
    """
    if isinstance(s, str):
        return s
    if not isinstance(s, (bytes, bytearray)):
        return str(s)
    return s.decode(encoding or 'utf-8', errors)


def useToBytes(s, encoding=None, errors='strict'):
    """
    将 str 转换为 bytes
    :param s: str
    :param encoding: 编码
    :param errors: 错误处理
    :return: bytes
    """
    if isinstance(s, bytes):
        return s
    if not isinstance(s, str):
        return bytes(s)
    return s.encode(encoding or 'utf-8', errors)


def useToMD5(data: AnyStr) -> str:
    """
    将字符数据转换为md5
    :param data: data
    :return: md5
    """
    return hashlib.md5(useToString(data).encode()).hexdigest()


def useToSHA1(data: AnyStr) -> str:
    """
    将字符数据转换为sha1
    :param data: data
    :return: sha1
    """
    return hashlib.sha1(useToString(data).encode()).hexdigest()


def useToCamel(data: str, char: str = '-') -> str:
    """
    将字符数据转换为驼峰命名
    :param data: data
    :param char: 特征字符，如：-、_
    :return:
    >>> useToCamel("test")
    'test'
    >>> useToCamel("test-case")
    'testCase'
    >>> useToCamel("test_case", char="_")
    'testCase'
    """
    return re.sub(char + r'(\w)', lambda m: m.group(1).upper(), data)


def useToSnake(data: str, char: str = '_') -> str:
    """
    将字符数据转换为下划线命名
    :param data: data
    :param char: 特征字符，如：-、_
    :return:
    >>> useToSnake("test")
    'test'
    >>> useToSnake("testCase")
    'test_case'
    >>> useToSnake("testCase", char="-")
    'test-case'
    """
    return re.sub(r'([A-Z])', lambda m: char + m.group(1).lower(), data)


def useToBoolean(value: any) -> Optional[bool]:
    """
    将数据转换为布尔值
    :param value:
    :return:
    """
    if value in list(EMPTY_VALUES):
        return None
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        value = value.lower()
        if value in ('t', 'true', '1'):
            return True
        elif value in ('f', 'false', '0'):
            return False
    raise ValueError("unrecognized")


if __name__ == '__main__':
    useToBoolean(True)
    useToBoolean(1)
