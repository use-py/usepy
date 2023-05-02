def useFormatSizeof(num: int, suffix='B') -> str:
    """
    将字节转换为可读的格式
    :param num: 字节长度
    :param suffix: 后缀
    :return: str

    >>> useFormatSizeof(1024)
    '1.0 KB'
    """
    for unit in ['', 'K', 'M', 'G', 'T', 'P', 'E', 'Z']:
        if abs(num) < 1024.0:
            return f"{num:.1f} {unit}{suffix}"
        num /= 1024.0
    return f"{num:.1f} Y{suffix}"
