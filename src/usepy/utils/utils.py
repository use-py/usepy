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
    return dict(x.split('=', 1) for x in cookies.split('; '))  # noqa


def headers_to_dict(headers: str) -> dict:
    """
    将字符串headers转换为字典
    :param headers: headers字符串
    :return: dict
    """
    return dict(map(lambda x: x.strip(), line.split(':')) for line in headers.split('\n') if ':' in line)  # noqa


def data_to_dict(data: str) -> dict:
    """
    将字符串data转换为字典
    :param data: data字符串。格式为`key1=value1&key2=value2`
    :return: dict
    """
    return dict(x.split('=') for x in data.split('&'))  # noqa


def gen_unique_id():
    """
    生成唯一id
    :return:
    """
    return f"{uuid4().hex}"


def sizeof_fmt(num: int, suffix='B') -> str:
    """
    将字节转换为可读的格式
    :param num: 字节长度
    :param suffix: 后缀
    :return: str

    >>> sizeof_fmt(1024)
    '1.0 KB'
    """
    for unit in ['', 'K', 'M', 'G', 'T', 'P', 'E', 'Z']:
        if abs(num) < 1024.0:
            return f"{num:.1f} {unit}{suffix}"
        num /= 1024.0
    return f"{num:.1f} Y{suffix}"


if __name__ == '__main__':
    print(sizeof_fmt(1024))
