from typing import TypeVar, Sequence, List, Iterable

T = TypeVar('T')


def intersection(*arrays: Iterable[T]) -> List[T]:
    """
    Returns the intersection of multiple arrays.

    The order of the result is determined by the first array.

    Args:
        *arrays (Iterable[T]): The arrays to intersect.

    Returns:
        List[T]: A new array of values that are in all given arrays.

    Examples:
        >>> intersection([1, 2, 3], [2, 3, 4], [2, 3, 5])
        [2, 3]
        >>> intersection([1, 2, 3], [4, 5, 6])
        []
        >>> intersection([1, 2, 2, 3], [2, 3])
        [2, 3]
    """
    if not arrays:
        return []

    # Convert all arrays to sets for efficient lookup
    sets = [set(arr) for arr in arrays[1:]]

    result = []
    seen = set()
    for item in arrays[0]:
        if item not in seen and all(item in s for s in sets):
            result.append(item)
            seen.add(item)

    return result