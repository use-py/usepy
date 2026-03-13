from typing import Dict


def sort_by_key(original_dict: Dict, az: bool = True) -> Dict:
    """sort dict by key

    Args:
        original_dict (Dict): The original dictionary.
        az (bool): Whether to sort in ascending order. Defaults to True.

    Returns:
        Dict: The sorted dictionary.

    Examples:
        >>> sort_by_key({'c': 1, 'b': 2, 'a': 3})
        {'a': 3, 'b': 2, 'c': 1}
    """
    return dict(sorted(original_dict.items(), reverse=not az))
