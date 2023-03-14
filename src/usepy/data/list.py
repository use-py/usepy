from typing import List, Generator, Dict, Optional, Callable, Literal, Any, Tuple, Union

SortType = Optional[
    Literal["quick", "bubble", "select"]
]

ListType = Union[List, Tuple]


class UseList:

    @staticmethod
    def split(collection: ListType, n: int) -> Generator[List, None, None]:
        """
        按指定数量平均分割列表
        :param collection: 原始列表
        :param n: 指定数量
        :return: 分割后的列表

        >>> list(UseList.split([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        >>> list(UseList.split((1, 2, 3, 4, 5, 6, 7, 8, 9), 4))
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

        >>> UseList.reverse([1, 2, 3, 4, 5])
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

        >>> UseList.objs_to_obj([{'id': 1, 'name': 'miclon'}, {'id': 2, 'name': 'miclon2'}], 'id')
        {1: {'id': 1, 'name': 'miclon'}, 2: {'id': 2, 'name': 'miclon2'}}
        """
        return {b[key]: b for b in collection}

    @staticmethod
    def dedupe(collection: List, key: Optional[Callable] = None):
        """
        列表去重，保持顺序
        >>> list(UseList.dedupe([1, 5, 2, 1, 9, 1, 5, 10]))
        [1, 5, 2, 9, 10]
        >>> list(UseList.dedupe([{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}], key=lambda d: (d['x'], d['y'])))
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

        >>> UseList.sort_quick([0, 5, 3, 2, 2])
        [0, 2, 2, 3, 5]
        >>> UseList.sort_quick([])
        []
        >>> UseList.sort_quick([-2, 5, 0, -45])
        [-45, -2, 0, 5]
        """
        if len(collection) < 2:
            return collection
        pivot = collection.pop()
        greater: List[int] = []
        lesser: List[int] = []
        for element in collection:
            (greater if element > pivot else lesser).append(element)
        return UseList.sort_quick(lesser) + [pivot] + UseList.sort_quick(greater)

    @staticmethod
    def sort_select(collection: List) -> List:
        """
        选择排序
        :param collection: 待排序数组
        :return: 排序后数组

        >>> UseList.sort_select([0, 5, 3, 2, 2])
        [0, 2, 2, 3, 5]
        >>> UseList.sort_select([])
        []
        >>> UseList.sort_select([-2, 5, 0, -45])
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
        if hasattr(UseList, name):
            return getattr(UseList, name)(collection)
        else:
            raise Exception('algorithm not found')

    @staticmethod
    def sort_by_list(collection: List, sort_list: List) -> List:
        """
        按指定列表排序，前者列表 按 后者列表排序
        :param collection: 待排序数组
        :param sort_list: 指定排序列表
        :return: 排序后数组

        >>> UseList.sort_by_list([1, 2, 3, 4, 5], [5, 4, 3, 2, 1])
        [5, 4, 3, 2, 1]
        >>> UseList.sort_by_list(['blue', 'green', 'orange', 'purple', 'yellow'], [3, 2, 5, 4, 1])
        ['yellow', 'green', 'blue', 'purple', 'orange']
        """
        return [val for (_, val) in sorted(zip(sort_list, collection), key=lambda x: x[0])]

    @staticmethod
    def flatten(nested: ListType) -> List:
        """
        多维数组扁平化
        :param nested: 多维数组
        :return: 扁平化数组

        >>> UseList.flatten([1, [2, 3, [4, 5]], 6])
        [1, 2, 3, 4, 5, 6]
        """
        result = []
        for item in nested:
            if isinstance(item, (list, tuple)):
                try:
                    result.extend(UseList.flatten(item))
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

        >>> UseList.min_by([{'n': 4}, {'n': 2}, {'n': 8}, {'n': 6}], lambda v: v['n'])
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

        >>> UseList.max_by([{'n': 4}, {'n': 2}, {'n': 8}, {'n': 6}], lambda v: v['n'])
        {'n': 8}
        """
        return max(collection, key=fn)
