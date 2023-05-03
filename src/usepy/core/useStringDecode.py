import base64


def useStringDecode(encode_str: str, key: str) -> str:
    """
    解密字符串
    :param encode_str: 加密字符串
    :param key: 密钥
    :return: 解密后字符串
    """
    decoded_chars = []
    original_str = base64.urlsafe_b64decode(encode_str).decode('utf-8')
    for i in range(len(original_str)):
        key_c = key[i % len(key)]
        decoded_c = chr((ord(original_str[i]) - ord(key_c) + 256) % 256)
        decoded_chars.append(decoded_c)
    decoded_string = "".join(decoded_chars)
    return decoded_string
