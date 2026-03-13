from typing import Union

from usepy.string.capitalize import capitalize


def pascal_case(string: Union[str, bytes]) -> str:
    """
    Converts a string to Pascal case.

    Pascal case is the naming convention in which each word is capitalized and concatenated without any separator characters.

    Args:
        string (Union[str, bytes]): The input string to be converted to Pascal case.

    Returns:
        str: The converted string in Pascal case.

    Examples:
        >>> pascal_case('pascalCase')
        'PascalCase'
        >>> pascal_case('some whitespace')
        'SomeWhitespace'
        >>> pascal_case('hyphen-text')
        'HyphenText'
        >>> pascal_case('HTTPRequest')
        'HttpRequest'
    """
    from usepy.string._get_words import get_words

    if isinstance(string, bytes):
        string = string.decode('utf-8')

    words = get_words(string)
    return ''.join(capitalize(word) for word in words)