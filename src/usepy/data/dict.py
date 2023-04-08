from collections import defaultdict
from copy import deepcopy
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
            合并多个字典，后面的字典会覆盖前面的字典

            :param dicts: 字典
            :return: 合并后的字典

            >>> UseDict.merge({'a': 1, 'b': 2}, {'b': 3, 'c': 4})
            {'a': 1, 'b': 3, 'c': 4}
            >>> UseDict.merge({'a': 1, 'b': 2}, {'b': 3, 'c': 4}, {'b': None, 'c': 5})
            {'a': 1, 'b': None, 'c': 5}
            >>> UseDict.merge({'a': 1, 'b': 2}, {'b': 3, 'c': 4}, {'b': '', 'c': 5})
            {'a': 1, 'b': '', 'c': 5}
            """
        result = {}
        for d in dicts:
            result.update(d)
        return result
    
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
    
    @staticmethod
    def merge_value(original_dict: dict) -> dict:
        """
        合并字典，相同的key合并为数组
        :param original_dict: 字典
        :return: 合并后的字典
        >>> UseDict.merge_value({'a': 1, 'b': 'foo', 'c': 400, 'd': 400})
        {1: ['a'], 'foo': ['b'], 400: ['c', 'd']}
        """
        res = defaultdict(list)
        for key, value in original_dict.items():
            res[value].append(key)
        return dict(res)
    
    @staticmethod
    def deep_update(main_dict: Dict, update_dict: Dict) -> None:
        """
        深度更新字典
        :param main_dict: 原始字典
        :param update_dict: 新字典
        :return: 更新后的字典
        >>> dict1 = {'a': {'b': 1}}
        >>> UseDict.deep_update(dict1, {'a': {'c': 2}})
        >>> assert dict1 == {'a': {'b': 1, 'c': 2}}
        """
        for key, value in update_dict.items():
            if (
                    key in main_dict
                    and isinstance(main_dict[key], dict)
                    and isinstance(value, dict)
            ):
                UseDict.deep_update(main_dict[key], value)
            elif (
                    key in main_dict
                    and isinstance(main_dict[key], list)
                    and isinstance(update_dict[key], list)
            ):
                main_dict[key] = main_dict[key] + update_dict[key]
            else:
                main_dict[key] = value
    
    @staticmethod
    def expand(source: dict, with_parent: bool = False, parent='') -> dict:
        """
        递归展开字典

        Args:
            source (dict): 待展开的字典。
            with_parent (bool, optional): 是否将 key 与其父级 key 通过 '.' 拼接。默认为 False。
            parent (str, optional): 当 with_prefix 为 True 时，key 拼接的前缀。默认为空字符串。

        Returns:
            dict: 展开后的字典。

        Examples:
            >>> source = {'a': {'b': 1, 'c': {'d': 2}}}
            >>> UseDict.expand(source)
            {'b': 1, 'd': 2}
            >>> UseDict.expand(source, with_parent=True)
            {'a.b': 1, 'a.c.d': 2}
        """
        result = {}
        for key, value in source.items():
            new_key = f"{parent}.{key}" if with_parent and parent else key
            if isinstance(value, dict):
                result.update(UseDict.expand(value, with_parent, new_key))
            else:
                result[new_key] = value
        return result
    
    @staticmethod
    def pops(data: dict, keys: list) -> dict:
        """
        从字典中弹出指定的多个键值对
        
        :param data: 原始字典
        :param keys: 键列表
        :return: 弹出的键值对
        
        >>> UseDict.pops({'a': 1, 'b': 2, 'c': 3}, ['a', 'c'])
        {'a': 1, 'c': 3}
        """
        res = {}
        for key in keys:
            if key in data:
                res[key] = data.pop(key)
        return res
    
    @staticmethod
    def pops_by_key_prefix(data: dict, key_prefix: str) -> dict:
        """
        从字典中弹出指定前缀的所有键值对
        
        :param data: 原始字典
        :param key_prefix: 键前缀
        :return: 弹出的键值对
        
        >>> UseDict.pops_by_key_prefix({'a': 1, 'b': 2, 'c': 3, 'aa': 4, 'ab': 5}, 'a')
        {'a': 1, 'aa': 4, 'ab': 5}
        """
        res = {}
        for key in list(data.keys()):
            if key.startswith(key_prefix):
                res[key] = data.pop(key)
        return res
    
    @staticmethod
    def delete_keys(data: dict, keys: list) -> None:
        """
        从字典中删除指定的多个键值对
        
        :param data: 原始字典
        :param keys: 键列表
        
        >>> data = {'a': 1, 'b': 2, 'c': 3}
        >>> UseDict.delete_keys(data, ['a', 'c'])
        >>> assert data == {'b': 2}
        """
        for key in keys:
            if key in data:
                del data[key]
    
    @staticmethod
    def delete_keys_by_key_prefix(data: dict, key_prefix: str) -> None:
        """
        从字典中删除指定前缀的所有键值对
        
        :param data: 原始字典
        :param key_prefix: 键前缀
        
        >>> data = {'a': 1, 'b': 2, 'c': 3, 'aa': 4, 'ab': 5}
        >>> UseDict.delete_keys_by_key_prefix(data, 'a')
        >>> assert data == {'b': 2, 'c': 3}
        """
        for key in list(data.keys()):
            if key.startswith(key_prefix):
                del data[key]
    
    @staticmethod
    def replace_keys(data: dict, mapping: dict) -> dict:
        """
        替换字典中的键
        
        :param data: 原始字典
        :param mapping: 键映射
        :return: 替换后的字典
        
        >>> UseDict.replace_keys({'a': 1, 'b': 2, 'c': 3}, {'a': 'aa', 'b': 'bb'})
        {'aa': 1, 'bb': 2, 'c': 3}
        """
        return {mapping.get(key, key): value for key, value in data.items()}
