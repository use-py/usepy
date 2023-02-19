"""
    @Author: MicLon
    @Date: 2023/02/19
    @Description: 用于转换数据类型的工具函数
"""

from typing import Any


def cookie_to_dict(cookies: str) -> dict:
    """
    将字符串cookie转换为字典
    :param cookies: cookie字符串
    :return: dict
    """
    return {cookie.split('=')[0]: cookie.split('=')[-1] for cookie in cookies.split('; ')}


def headers_to_dict(headers: str) -> dict:
    """
    将字符串headers转换为字典
    :param headers: headers字符串
    :return: dict
    """
    header_dict = {}
    for line in headers.split('\n'):
        if ':' in line:
            key, value = line.split(':', 1)
            header_dict[key.strip()] = value.strip()
    return header_dict


def data_to_dict(data: str) -> dict:
    """
    将字符串data转换为字典
    :param data: data字符串。格式为`key1=value1&key2=value2`
    :return: dict
    """
    return {item.split('=')[0]: item.split('=')[-1] for item in data.split('&')}


def to_string(data: Any) -> str:
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
