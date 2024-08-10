from typing import TypeVar, Sequence, Set

T = TypeVar('T')


def without(array: Sequence[T], *values: T) -> list[T]:
    """
    Creates a new list that excludes all specified values from the given array.

    It correctly excludes `NaN`, as it compares values using the `==` operator
    in Python, which handles `NaN` correctly.

    Args:
        array (Sequence[T]): The sequence to filter.
        *values (T): The values to exclude.

    Returns:
        list[T]: A new list without the specified values.

    Examples:
        >>> without([1, 2, 3, 4, 5], 2, 4)
        [1, 3, 5]

        >>> without(['a', 'b', 'c', 'a'], 'a')
        ['b', 'c']
    """
    values_set: Set[T] = set(values)
    return [item for item in array if item not in values_set]
