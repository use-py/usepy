from typing import TypeVar, Sequence
from usepy.typing_ import Union



T = TypeVar("T")


def first(array: Sequence[T]) -> Union[T, None]:
    """
    Gets the first element of `array`.

    :param array: The array to query.
    :type array: Sequence[T]
    :return: Returns the first element of `array`.
    :rtype: Union[T, None]

    :Example:

    >>> first([1, 2, 3])
    1
    """
    return array[0] if array else None
