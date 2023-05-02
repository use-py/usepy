from typing import Optional, Tuple


def get_section(
        original_str: str,
        start_str: Optional[str] = None,
        end_str: Optional[str] = None
) -> Tuple[Optional[str], Optional[int], Optional[int]]:
    """
    获取字符串区间内容
    :param original_str: 原始字符串
    :param start_str: 开始字符串
    :param end_str: 结束字符串
    :return: 区间内容
    >>> get_section('abc123def', 'abc', 'def')
    ('123', 3, 6)
    >>> get_section('abc123def', 'abc')
    ('123def', 3, 9)
    >>> get_section('abc123def', end_str='def')[0]
    'abc123'
    """
    if start_str is None:
        start_ = 0
    else:
        start_ = original_str.find(start_str)
        if start_ >= 0:
            start_ += len(start_str)
        else:
            return None, start_, None
    if end_str is None:
        end_ = len(original_str)
    else:
        end_ = original_str.find(end_str, start_)
    if end_ >= 0:
        return original_str[start_:end_], start_, end_
    return None, None, None


def useStringMiddle(
        original_str: str,
        start_str: Optional[str] = None,
        end_str: Optional[str] = None
) -> Optional[str]:
    """
    获取字符串中间内容
    :param original_str: 原始字符串
    :param start_str: 开始字符串
    :param end_str: 结束字符串
    :return: 中间内容
    >>> useStringMiddle('abc123def', 'abc', 'def')
    '123'
    """
    find_str, _, _ = get_section(original_str, start_str, end_str)
    return find_str


def useStringMiddleBatch(
        original_str: str,
        start_str: Optional[str] = None,
        end_str: Optional[str] = None,
        max_count: Optional[int] = None
) -> list:
    """
    获取字符串中间内容
    :param original_str: 原始字符串
    :param start_str: 开始字符串
    :param end_str: 结束字符串
    :param max_count: 最大数量
    :return: 中间内容
    >>> useStringMiddleBatch('abc123def456abc789def', 'abc', 'def')
    ['123', '789']
    >>> useStringMiddleBatch('abc123def456abc789def', 'abc', 'def', 1)
    ['123']
    """
    result = []
    while True:
        find_str, start_, end_ = get_section(original_str, start_str, end_str)
        if find_str is None:
            break
        result.append(find_str)
        original_str = original_str[end_ + len(end_str or ''):]
    return result[:max_count]


def useStringLeft(
        original_str: str,
        end_str: str
) -> Optional[str]:
    """
    获取字符串左边内容
    :param original_str: 原始字符串
    :param end_str: 结束字符串
    :return: 左边内容
    >>> useStringLeft('abc123def', 'def')
    'abc123'
    """
    find_str, _, _ = get_section(original_str, end_str=end_str)
    return find_str


def useStringRight(
        original_str: str,
        start_str: str
) -> Optional[str]:
    """
    获取字符串右边内容
    :param original_str: 原始字符串
    :param start_str: 开始字符串
    :return: 右边内容
    >>> useStringRight('abc123def', 'abc')
    '123def'
    """
    find_str, _, _ = get_section(original_str, start_str=start_str)
    return find_str
