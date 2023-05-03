def useDataToDict(data: str) -> dict:
    """
    将字符串data转换为字典
    :param data: data字符串。格式为`key1=value1&key2=value2`
    :return: dict
    """
    return dict(x.split('=') for x in data.split('&'))  # noqa
