try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal
from typing import List, Generator, Dict, Optional, Callable, Any, Tuple, Union

from functools import reduce
from operator import and_, or_

SortType = Optional[
    Literal["quick", "bubble", "select"]
]

ListType = Union[List, Tuple]


class useList:

    @staticmethod
    def split(collection: ListType, n: int) -> Generator[List, None, None]:
        """
        按指定数量平均分割列表
        :param collection: 原始列表
        :param n: 指定数量
        :return: 分割后的列表

        >>> list(useList.split([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        >>> list(useList.split((1, 2, 3, 4, 5, 6, 7, 8, 9), 4))
        [(1, 2, 3, 4), (5, 6, 7, 8), (9,)]
        """
        for i in range(0, len(collection), n):
            yield collection[i:i + n]

    @staticmethod
    def reverse(collection: ListType) -> List:
        """
        反转列表
        :param collection: 待反转列表
        :return: 反转后列表

        >>> useList.reverse([1, 2, 3, 4, 5])
        [5, 4, 3, 2, 1]
        """
        return collection[::-1]

    @staticmethod
    def objs_to_obj(collection: List[Dict], key: str) -> Dict:
        """
        将对象列表转换为指定key名的对象
        :param collection: 对象列表
        :param key: 指定key名
        :return: 指定key名的对象

        >>> useList.objs_to_obj([{'id': 1, 'name': 'miclon'}, {'id': 2, 'name': 'miclon2'}], 'id')
        {1: {'id': 1, 'name': 'miclon'}, 2: {'id': 2, 'name': 'miclon2'}}
        """
        return {b[key]: b for b in collection}

    @staticmethod
    def dedupe(collection: List, key: Optional[Callable] = None):
        """
        列表去重，保持顺序
        >>> list(useList.dedupe([1, 5, 2, 1, 9, 1, 5, 10]))
        [1, 5, 2, 9, 10]
        >>> list(useList.dedupe([{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}], key=lambda d: (d['x'], d['y'])))
        [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 2, 'y': 4}]
        """
        seen = set()
        for item in collection:
            value = item if key is None else key(item)
            if value not in seen:
                yield item
                seen.add(value)

    @staticmethod
    def sort_bubble(collection: List) -> List:
        """
        冒泡排序
        :param collection: 待排序数组
        :return: 排序后数组
        """
        for i in range(len(collection) - 1):
            for j in range(len(collection) - 1 - i):
                if collection[j] > collection[j + 1]:
                    collection[j], collection[j + 1] = collection[j + 1], collection[j]
        return collection

    @staticmethod
    def sort_quick(collection: List) -> List:
        """
        快速排序
        :param collection: 待排序数组
        :return: 排序后数组

        >>> useList.sort_quick([0, 5, 3, 2, 2])
        [0, 2, 2, 3, 5]
        >>> useList.sort_quick([])
        []
        >>> useList.sort_quick([-2, 5, 0, -45])
        [-45, -2, 0, 5]
        """
        if len(collection) < 2:
            return collection
        pivot = collection.pop()
        greater: List[int] = []
        lesser: List[int] = []
        for element in collection:
            (greater if element > pivot else lesser).append(element)
        return useList.sort_quick(lesser) + [pivot] + useList.sort_quick(greater)

    @staticmethod
    def sort_select(collection: List) -> List:
        """
        选择排序
        :param collection: 待排序数组
        :return: 排序后数组

        >>> useList.sort_select([0, 5, 3, 2, 2])
        [0, 2, 2, 3, 5]
        >>> useList.sort_select([])
        []
        >>> useList.sort_select([-2, 5, 0, -45])
        [-45, -2, 0, 5]
        """
        for i in range(len(collection) - 1):
            min_index = i
            for j in range(i + 1, len(collection)):
                if collection[j] < collection[min_index]:
                    min_index = j
            collection[i], collection[min_index] = collection[min_index], collection[i]
        return collection

    @staticmethod
    def sort(collection: List, algorithm: SortType = 'bubble') -> List:
        """
        排序
        :param collection: 待排序数组
        :param algorithm: 排序算法, 默认冒泡排序
        :return: 排序后数组
        """
        name = f'sort_{algorithm}'
        if hasattr(useList, name):
            return getattr(useList, name)(collection)
        else:
            raise Exception('algorithm not found')

    @staticmethod
    def sort_by_list(collection: List, sort_list: List) -> List:
        """
        按指定列表排序，前者列表 按 后者列表排序
        :param collection: 待排序数组
        :param sort_list: 指定排序列表
        :return: 排序后数组

        >>> useList.sort_by_list([1, 2, 3, 4, 5], [5, 4, 3, 2, 1])
        [5, 4, 3, 2, 1]
        >>> useList.sort_by_list(['blue', 'green', 'orange', 'purple', 'yellow'], [3, 2, 5, 4, 1])
        ['yellow', 'green', 'blue', 'purple', 'orange']
        """
        return [val for (_, val) in sorted(zip(sort_list, collection), key=lambda x: x[0])]

    @staticmethod
    def flatten(nested: ListType) -> List:
        """
        多维数组扁平化
        :param nested: 多维数组
        :return: 扁平化数组

        >>> useList.flatten([1, [2, 3, [4, 5]], 6])
        [1, 2, 3, 4, 5, 6]
        """
        result = []
        for item in nested:
            if isinstance(item, (list, tuple)):
                try:
                    result.extend(useList.flatten(item))
                except TypeError:
                    result.append(item)
            else:
                result.append(item)
        return result

    @staticmethod
    def min_by(collection: List, fn: Callable) -> Any:
        """
        返回最小值
        :param collection: 数组
        :param fn: 函数
        :return: 最小值

        >>> useList.min_by([{'n': 4}, {'n': 2}, {'n': 8}, {'n': 6}], lambda v: v['n'])
        {'n': 2}
        """
        return min(collection, key=fn)

    @staticmethod
    def max_by(collection: List, fn: Callable) -> Any:
        """
        返回最大值
        :param collection: 数组
        :param fn: 函数
        :return: 最大值

        >>> useList.max_by([{'n': 4}, {'n': 2}, {'n': 8}, {'n': 6}], lambda v: v['n'])
        {'n': 8}
        """
        return max(collection, key=fn)

    @staticmethod
    def difference(original_list: List, exclude_list: List, fn: Optional[Callable] = None):
        """
        求差集
        :param original_list: 原数组
        :param exclude_list: 排除数组
        :param fn: 函数
        :return: 差集

        >>> useList.difference([1, 2, 3], [1, 4])
        [2, 3]
        >>> useList.difference([{'a': 1, 'b': 2}, {'a': 2, 'b': 3}], [{'a': 1, 'b': 2}])
        [{'a': 2, 'b': 3}]
        >>> useList.difference([1, 2, 3], [1, 4], fn=lambda x: x ** 2)
        [3]
        """
        fn = fn or (lambda x: x)
        return [item for item in original_list if fn(item) not in exclude_list]


def useListFilter(array: List, fn: Callable):
    """
    数组过滤
    :param array: 数组
    :param fn: 函数
    :return:
    """
    return list(filter(fn, array))


def useListFlatten(array: List):
    """
    数组扁平化
    :param array: 数组
    :return:
    """
    return useList.flatten(array)


def useListDifference(original_array: List, exclude_array: List, fn: Optional[Callable] = None):
    """
    求差集
    :param original_array: 原数组
    :param exclude_array: 排除数组
    :param fn: 函数
    :return: 差集

    >>> useListDifference([1, 2, 3], [1, 4])
    [2, 3]
    >>> useListDifference([{'a': 1, 'b': 2}, {'a': 2, 'b': 3}], [{'a': 1, 'b': 2}])
    [{'a': 2, 'b': 3}]
    >>> useListDifference([1, 2, 3], [1, 4], fn=lambda x: x ** 2)
    [3]
    """
    return useList.difference(original_array, exclude_array, fn)


def useListEvery(array: List, fn: Callable):
    """
    数组每一项都满足条件
    :param array: 数组
    :param fn: 函数
    :return:
    """
    return reduce(and_, [fn(element) for element in array])


def useListSome(array: List, fn: Callable):
    """
    数组有一项满足条件
    :param array: 数组
    :param fn: 函数
    :return:
    """
    return reduce(or_, [fn(element) for element in array])


def useListSort(array: List, algorithm: SortType = 'bubble'):
    """
    数组排序
    :param array: 数组
    :param algorithm: 排序算法, 默认冒泡排序
    :return: 排序后数组
    """
    return useList.sort(array, algorithm)


def useListUnique(array: List, fn: Optional[Callable] = None):
    """
    数组去重
    :param fn:
    :param array: 数组
    :return: 去重后数组
    """
    return list(useList.dedupe(array, fn))
