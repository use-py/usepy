from random import randint, choice


def useRandomString(min_len=3, max_len=20, characters=None):
    """
    生成随机字符串
    :param min_len: 最小长度
    :param max_len: 最大长度
    :param characters: 字符集
    :return: 随机字符串
    """
    import string

    _characters = string.ascii_letters + string.digits
    characters = characters or _characters
    _len = randint(min_len, max_len) if max_len > min_len else min_len
    return ''.join((choice(characters) for _ in range(_len)))


def useRandomUUID():
    from uuid import uuid4
    return f"{uuid4().hex}"
