from typing import TypeVar, Sequence

T = TypeVar("T")


def first(array: Sequence[T]) -> T | None:
    """
    Gets the first element of `array`.

    :param array: The array to query.
    :type array: Sequence[T]
    :return: Returns the first element of `array`.
    :rtype: T | None

    :Example:

    >>> first([1, 2, 3])
    1
    """
    return array[0] if array else None
