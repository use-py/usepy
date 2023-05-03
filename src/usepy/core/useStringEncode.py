import base64


def useStringEncode(original_str: str, key: str) -> str:
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
