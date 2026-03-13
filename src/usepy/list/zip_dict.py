from typing import TypeVar, List, Dict

P = TypeVar('P')
V = TypeVar('V')


def zip_dict(keys: List[P], values: List[V]) -> Dict[P, V]:
    """
    Combines two arrays, one of property names and one of corresponding values, into a single object.

    This function takes two arrays: one containing property names and another containing corresponding values.
    It returns a new dictionary where the property names from the first array are keys, and the corresponding elements
    from the second array are values. If the `keys` array is longer than the `values` array, the remaining keys will
    have `None` as their values.

    Args:
        keys (List[P]): An array of property names.
        values (List[V]): An array of values corresponding to the property names.

    Returns:
        Dict[P, V]: A new dictionary composed of the given property names and values.

    Examples:
        >>> key1 = ['a', 'b', 'c']
        >>> key2 = [1, 2, 3]
        >>> zip_dict(key1, key2)
        {'a': 1, 'b': 2, 'c': 3}

        >>> key1 = ['a', 'b', 'c']
        >>> key2 = [1, 2]
        >>> zip_dict(key1, key2)
        {'a': 1, 'b': 2, 'c': None}

        >>> key1 = ['a', 'b']
        >>> key2 = [1, 2, 3]
        >>> zip_dict(key1, key2)
        {'a': 1, 'b': 2}
    """
    result = {}
    for i, key in enumerate(keys):
        result[key] = values[i] if i < len(values) else None
    return result
