"""
    @Author: MicLon
    @Date: 2023/02/19
    @Description: 一些其他工具集合
"""

from uuid import uuid4


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


def gen_unique_id():
    """
    生成唯一id
    :return:
    """
    return f"{uuid4().hex}"
