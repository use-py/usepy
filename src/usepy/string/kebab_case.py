from typing import Union


def kebab_case(string: Union[str, bytes]) -> str:
    """
    Converts a string to kebab case.

    Kebab case is the naming convention in which each word is written in lowercase
    and separated by a dash (-) character.

    Args:
        string (Union[str, bytes]): The input string to be converted to kebab case.

    Returns:
        str: The converted string in kebab case.

    Examples:
        >>> kebab_case('camelCase')
        'camel-case'
        >>> kebab_case('some whitespace')
        'some-whitespace'
        >>> kebab_case('hyphen-text')
        'hyphen-text'
        >>> kebab_case('HTTPRequest')
        'http-request'
    """
    from usepy.string._get_words import get_words

    if isinstance(string, bytes):
        string = string.decode('utf-8')

    words = get_words(string)
    return '-'.join(word.lower() for word in words)
