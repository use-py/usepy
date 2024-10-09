from typing import Callable, TypeVar, Dict

T = TypeVar('T')
K = TypeVar('K')


def key_by(lst: list[T], get_key_from_item: Callable[[T], K]) -> Dict[K, T]:
    """
    Maps each element of a list based on a provided key-generating function.

    This function takes a list and a function that generates a key from each element. It returns
    a dictionary where the keys are the generated keys and the values are the corresponding elements.
    If there are multiple elements generating the same key, the last element among them is used
    as the value.

    Args:
        lst (list[T]): The list of elements to be mapped.
        get_key_from_item (Callable[[T], K]): A function that generates a key from an element.

    Returns:
        Dict[K, T]: A dictionary where keys are mapped to each element of a list.

    Example:
        >>> array = [
        ...     {'category': 'fruit', 'name': 'apple'},
        ...     {'category': 'fruit', 'name': 'banana'},
        ...     {'category': 'vegetable', 'name': 'carrot'}
        ... ]
        >>> key_by(array, lambda item: item['category'])
        {'fruit': {'category': 'fruit', 'name': 'banana'}, 'vegetable': {'category': 'vegetable', 'name': 'carrot'}}
    """
    result: Dict[K, T] = {}

    for item in lst:
        key = get_key_from_item(item)
        result[key] = item

    return result
