"""
    @Author: MicLon
    @Date: 2023/02/19
    @Description: 用于转换数据类型的工具函数
"""

from typing import Any


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
