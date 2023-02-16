import string
import base64

from random import randint, choice
from typing import Optional, Tuple

from usepy.utils.utils import gen_unique_id

_characters = string.ascii_letters + string.digits


class UseString:

    @staticmethod
    def uuid():
        return gen_unique_id()

    @staticmethod
    def to_str(s, encoding=None, errors='strict'):
        """
        将 bytes 或者 bytearray 转换为 str
        :param s: bytes 或者 bytearray
        :param encoding: 编码
        :param errors: 错误处理
        :return: str
        """
        if isinstance(s, str):
            return s
        if not isinstance(s, (bytes, bytearray)):
            return str(s)
        return s.decode(encoding or 'utf-8', errors)

    @staticmethod
    def to_bytes(s, encoding=None, errors='strict'):
        """
        将 str 转换为 bytes
        :param s: str
        :param encoding: 编码
        :param errors: 错误处理
        :return: bytes
        """
        if isinstance(s, bytes):
            return s
        if not isinstance(s, str):
            return bytes(s)
        return s.encode(encoding or 'utf-8', errors)

    @staticmethod
    def random(min_len=3, max_len=20, characters=None):
        """
        生成随机字符串
        :param min_len: 最小长度
        :param max_len: 最大长度
        :param characters: 字符集
        :return: 随机字符串
        """
        characters = characters or _characters
        _len = randint(min_len, max_len) if max_len > min_len else min_len
        return ''.join((choice(characters) for _ in range(_len)))

    @staticmethod
    def _get_section(
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
        >>> UseString._get_section('abc123def', 'abc', 'def')
        ('123', 3, 6)
        >>> UseString._get_section('abc123def', 'abc')
        ('123def', 3, 9)
        >>> UseString._get_section('abc123def', end_str='def')[0]
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

    @staticmethod
    def get_middle(
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
        >>> UseString.get_middle('abc123def', 'abc', 'def')
        '123'
        """
        find_str, _, _ = UseString._get_section(original_str, start_str, end_str)
        return find_str

    @staticmethod
    def get_middle_batch(
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
        >>> UseString.get_middle_batch('abc123def456abc789def', 'abc', 'def')
        ['123', '789']
        >>> UseString.get_middle_batch('abc123def456abc789def', 'abc', 'def', 1)
        ['123']
        """
        result = []
        while True:
            find_str, start_, end_ = UseString._get_section(original_str, start_str, end_str)
            if find_str is None:
                break
            result.append(find_str)
            original_str = original_str[end_ + len(end_str or ''):]
        return result[:max_count]

    @staticmethod
    def get_left(
            original_str: str,
            end_str: str
    ) -> Optional[str]:
        """
        获取字符串左边内容
        :param original_str: 原始字符串
        :param end_str: 结束字符串
        :return: 左边内容
        >>> UseString.get_left('abc123def', 'def')
        'abc123'
        """
        find_str, _, _ = UseString._get_section(original_str, end_str=end_str)
        return find_str

    @staticmethod
    def get_right(
            original_str: str,
            start_str: str
    ) -> Optional[str]:
        """
        获取字符串右边内容
        :param original_str: 原始字符串
        :param start_str: 开始字符串
        :return: 右边内容
        >>> UseString.get_right('abc123def', 'abc')
        '123def'
        """
        find_str, _, _ = UseString._get_section(original_str, start_str=start_str)
        return find_str

    @staticmethod
    def reverse(original_str: str) -> str:
        """
        反转字符串
        :param original_str: 原始字符串
        :return: 反转后字符串
        >>> UseString.reverse('abc')
        'cba'
        """
        return original_str[::-1]

    @staticmethod
    def encode(original_str: str, key: str) -> str:
        """
        加密字符串
        :param original_str: 原始字符串
        :param key: 密钥
        :return: 加密后字符串
        """
        encoded_chars = []
        for i in range(len(original_str)):
            key_c = key[i % len(key)]
            encoded_c = chr(ord(original_str[i]) + ord(key_c) % 256)
            encoded_chars.append(encoded_c)
        encoded_string = "".join(encoded_chars)
        return base64.urlsafe_b64encode(encoded_string.encode('utf-8')).decode('utf-8')

    @staticmethod
    def decode(original_str: str, key: str) -> str:
        """
        解密字符串
        :param original_str: 原始字符串
        :param key: 密钥
        :return: 解密后字符串
        """
        decoded_chars = []
        original_str = base64.urlsafe_b64decode(original_str).decode('utf-8')
        for i in range(len(original_str)):
            key_c = key[i % len(key)]
            decoded_c = chr((ord(original_str[i]) - ord(key_c) + 256) % 256)
            decoded_chars.append(decoded_c)
        decoded_string = "".join(decoded_chars)
        return decoded_string
