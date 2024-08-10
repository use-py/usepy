from typing import TypeVar

from usepy.string.capitalize import capitalize

T = TypeVar('T', bound=str)


def camel_case(string: T) -> T:
    """
    Converts a string to camel case.

    Camel case is the naming convention in which each word is written in lowercase
    and separated by an underscore (_) character.

    Args:
        string (T): The input string to be converted to camel case.

    Returns:
        str: The converted string in camel case.

    Examples:
        >>> camel_case('camelCase')
        'camelCase'
        >>> camel_case('some whitespace')
        'someWhitespace'
        >>> camel_case('hyphen-text')
        'hyphenText'
        >>> camel_case('HTTPRequest')
        'httpRequest'
    """
    from usepy.string._get_words import get_words

    words = get_words(string)

    if not words:
        return ""

    first, *rest = words
    capitalized_rest = [capitalize(word) for word in rest]

    return f"{first.lower()}{''.join(capitalized_rest)}"
