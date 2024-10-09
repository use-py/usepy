from typing import Dict


def sort_by_value(original_dict: Dict, az: bool = True) -> Dict:
    """sort dict by value

    Args:
        original_dict (Dict): The original dictionary.
        az (bool): Whether to sort in ascending order. Defaults to True.

    Returns:
        Dict: The sorted dictionary.

    Examples:
        >>> sort_by_value({"a": 3, "b": 2, "c": 1}, False)
        {'c': 1, 'b': 2, 'a': 3}
    """
    return dict(sorted(original_dict.items(), key=lambda x: x[1], reverse=not az))
