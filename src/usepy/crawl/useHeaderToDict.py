def useHeaderToDict(headers: str) -> dict:
    """
    将字符串headers转换为字典
    :param headers: headers字符串
    :return: dict
    """
    return dict(map(lambda x: x.strip(), line.split(':')) for line in headers.split('\n') if ':' in line)  # noqa
