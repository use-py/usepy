from typing import Tuple, List, Any


def zip_tuple(*lsts: List[Any]) -> List[Tuple[Any, ...]]:
    """
    Combines multiple arrays into a single array of tuples.

    This function takes multiple arrays and returns a new array where each element is a tuple
    containing the corresponding elements from the input arrays. If the input arrays are of
    different lengths, the resulting array will have the length of the longest input array,
    with `None` values for missing elements.

    Args:
        *lsts: The arrays to zip together.

    Returns:
        A new array of tuples containing the corresponding elements from the input arrays.

    Examples:
        >>> arr1 = [1, 2, 3]
        >>> arr2 = ['a', 'b', 'c']
        >>> zip_tuple(arr1, arr2)
        [(1, 'a'), (2, 'b'), (3, 'c')]

        >>> arr3 = [True, False]
        >>> zip_tuple(arr1, arr2, arr3)
        [(1, 'a', True), (2, 'b', False), (3, 'c', None)]
    """
    result: List[Tuple[Any, ...]] = []

    max_index = max(len(arr) for arr in lsts)

    for i in range(max_index):
        element: List[Any] = []

        for arr in lsts:
            element.append(arr[i] if i < len(arr) else None)

        result.append(tuple(element))

    return result
