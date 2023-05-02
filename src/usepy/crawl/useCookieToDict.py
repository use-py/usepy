def useCookieToDict(cookies: str) -> dict:
    """
    将字符串cookie转换为字典
    :param cookies: cookie字符串
    :return: dict
    """
    return dict(x.split('=', 1) for x in cookies.split('; '))  # noqa
