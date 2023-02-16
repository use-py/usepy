from collections import defaultdict
from typing import List, Dict


class UseDict:

    @staticmethod
    def find_keys(original_dict: Dict, val: any) -> List:
        """
        查找字典中指定值的所有键
        :param original_dict: 原始字典
        :param val: 指定值
        :return: 键列表
        >>> UseDict.find_keys({'a': 1, 'b': 2, 'c': 3}, 2)
        ['b']
        """
        return list(key for key, value in original_dict.items() if value == val)

    @staticmethod
    def reverse(original_dict: Dict) -> Dict:
        """
        反转字典
        :param original_dict: 原始字典
        :return: 反转后的字典
        >>> UseDict.reverse({'a': 1, 'b': 2, 'c': 3})
        {1: 'a', 2: 'b', 3: 'c'}
        """
        return {v: k for k, v in original_dict.items()}

    @staticmethod
    def sort_by_key(original_dict: Dict, az: bool = False) -> Dict:
        """
        按键排序
        :param original_dict: 原始字典
        :param az: 是否升序 True: 升序 False: 降序
        :return: 排序后的字典
        >>> UseDict.sort_by_key({'c': 1, 'b': 2, 'a': 3})
        {'a': 3, 'b': 2, 'c': 1}
        """
        return dict(sorted(original_dict.items(), reverse=az))

    @staticmethod
    def sort_by_value(original_dict: Dict, az: bool = False) -> Dict:
        """
        按值排序
        :param original_dict: 原始字典
        :param az: 是否升序 True: 升序 False: 降序
        :return: 排序后的字典
        >>> UseDict.sort_by_value({'c': 1, 'b': 2, 'a': 3})
        {'c': 1, 'b': 2, 'a': 3}
        """
        return dict(sorted(original_dict.items(), key=lambda x: x[1], reverse=az))

    @staticmethod
    def arrays_to_dict(keys: List, values: List) -> Dict:
        """
        将两个数组转换为字典
        :param keys: 键列表
        :param values: 值列表
        :return: 字典
        >>> UseDict.arrays_to_dict(['a', 'b', 'c'], [1, 2, 3])
        {'a': 1, 'b': 2, 'c': 3}
        """
        return dict(zip(keys, values))

    @staticmethod
    def merge(*dicts: Dict) -> Dict:
        """
        合并字典
        :param dicts: 字典列表
        :return: 合并后的字典
        >>> UseDict.merge({'a': 1}, {'b': 2}, {'c': 3})
        {'a': 1, 'b': 2, 'c': 3}
        """
        return {k: v for d in dicts for k, v in d.items()}

    @staticmethod
    def merge_values(*dicts: Dict) -> Dict:
        """
        合并字典，相同的key合并为数组
        :param dicts: 字典列表
        :return: 合并后的字典
        >>> UseDict.merge_values({'a': 1, 'b': 'foo', 'c': 400}, {'a': 3, 'b': 200, 'd': 400})
        {'a': [1, 3], 'b': ['foo', 200], 'c': [400], 'd': [400]}
        """
        res = defaultdict(list)
        for d in dicts:
            for key in d:
                res[key].append(d[key])
        return dict(res)
