import pytest

from usepy import useList, useListFilter, useListFlatten, useListDifference, useListEvery, useListSome, useListSort, \
    useListUnique, useListMergeByKey


def test_split():
    assert list(useList.split([1, 2, 3, 4], 2)) == [[1, 2], [3, 4]]
    assert list(useList.split([1, 2, 3, 4, 5, 6, 7, 8], 3)) == [[1, 2, 3], [4, 5, 6], [7, 8]]
    assert list(useList.split([], 4)) == []
    assert list(useList.split("1234", 2)) == ["12", "34"]
    assert list(useList.split("12345", 2)) == ["12", "34", "5"]
    assert list(useList.split((1, 2, 3), 2)) == [(1, 2), (3,)]


def test_objs_to_obj():
    assert useList.objs_to_obj(
        [{'id': 1, 'name': 'miclon'}, {'id': 2, 'name': 'miclon2'}], 'id'
    ) == {1: {'id': 1, 'name': 'miclon'},
          2: {'id': 2, 'name': 'miclon2'}}
    assert useList.objs_to_obj(
        [{'id': 1, 'name': 'miclon'}, {'id': 2, 'name': 'miclon2'}], 'name'
    ) == {'miclon': {'id': 1, 'name': 'miclon'},
          'miclon2': {'id': 2, 'name': 'miclon2'}}
    # 重复的key，后面的会覆盖前面的
    assert useList.objs_to_obj(
        [{'id': 123, 'name': 'miclon'}, {'id': 456, 'name': 'miclon'}], 'name'
    ) == {'miclon': {'id': 456, 'name': 'miclon'}}


def test_dedupe():
    assert list(useListUnique([1, 5, 2, 1, 9, 1, 5, 10])) == [1, 5, 2, 9, 10]
    assert list(useListUnique([{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}],
                              fn=lambda d: (d['x'], d['y']))) == [{'x': 1, 'y': 2}, {'x': 1, 'y': 3},
                                                                  {'x': 2, 'y': 4}]
    assert list(useList.dedupe([1, 5, 2, 1, 9, 1, 5, 10], key=lambda x: x % 3)) == [1, 5, 9]


def test_sort():
    assert useListSort([1, 8, 6, 11, 3, 0]) == [0, 1, 3, 6, 8, 11]
    assert useListSort([1, 8, 6, 11, 3, 0], algorithm="quick") == [0, 1, 3, 6, 8, 11]
    assert useList.reverse(
        useList.sort([1, 8, 6, 11, 3, 0], algorithm="quick")
    ) == [11, 8, 6, 3, 1, 0]

    assert useList.sort_by_list(['blue', 'green', 'orange', 'purple', 'yellow'], [3, 2, 5, 4, 1]) == ['yellow', 'green',
                                                                                                      'blue', 'purple',
                                                                                                      'orange']
    assert useList.sort_bubble([1, 8, 6, 11, 3, 0]) == [0, 1, 3, 6, 8, 11]
    assert (
            useList.sort([1, 8, 6, 11, 3, 0], algorithm="select")
            == useList.sort([1, 8, 6, 11, 3, 0], algorithm="quick")
    )


def test_min_max_by():
    assert useList.min_by([{"a": 1, "b": 2}, {"a": 3, "b": 5}], lambda v: v['a']) == {"a": 1, "b": 2}
    assert useList.max_by([{"a": 1, "b": 2}, {"a": 3, "b": 5}], lambda v: v['a']) == {"a": 3, "b": 5}
    assert useList.max_by([{'n': 4}, {'n': 2}, {'n': 8}, {'n': 6}], lambda v: v['n']) == {'n': 8}
    assert useList.min_by([{'n': 4}, {'n': 2}, {'n': 8}, {'n': 6}], lambda v: v['n']) == {'n': 2}
    assert useList.max_by([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], lambda v: v) == 10
    assert useList.min_by([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], lambda v: v) == 1


@pytest.mark.parametrize(
    "array,expected,fn",
    [
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], [2, 4, 6, 8], lambda x: x % 2 == 0),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 3, 5, 7, 9], lambda x: x % 2 == 1),
    ]
)
def test_useListFilter(array, expected, fn):
    assert useListFilter(array, fn) == expected


@pytest.mark.parametrize(
    "array,expected",
    [
        ([1, 2, [3, 4, [5, 6], 7], 8], [1, 2, 3, 4, 5, 6, 7, 8]),
        ([1, 2, [3, 4, (5, 5), 7], 8], [1, 2, 3, 4, 5, 5, 7, 8]),
        ((1, 2, (3, 4, (5, 5), 7), 8), [1, 2, 3, 4, 5, 5, 7, 8]),
    ]
)
def test_useListFlatten(array, expected):
    assert useListFlatten(array) == expected


@pytest.mark.parametrize(
    "array1,array2,fn,expected",
    [
        ([1, 2, 3], [1, 4], None, [2, 3]),
        ([{'a': 1, 'b': 2}, {'a': 2, 'b': 3}], [{'a': 1, 'b': 2}], None, [{'a': 2, 'b': 3}]),
        ([1, 2, 3], [1, 4], lambda x: x ** 2, [3]),
    ]
)
def test_useListDifference(array1, array2, fn, expected):
    assert useListDifference(array1, array2, fn) == expected


@pytest.mark.parametrize(
    "array,fn,expected",
    [
        ([1, 2, 3, 4, 5], lambda x: x > 0, True),
        ([2, 4, 6, 8], lambda x: x % 2 == 0, True),
        ([1, 2, 4, 6, 8], lambda x: x % 2 == 0, False),
    ]
)
def test_useListEvery(array, fn, expected):
    assert useListEvery(array, fn) == expected


@pytest.mark.parametrize(
    "array,fn,expected",
    [
        ([1, -1, 0, -10], lambda x: x > 0, True),
        ([1, 3, 5, 7], lambda x: x % 2 == 0, False)
    ]
)
def test_useListSome(array, fn, expected):
    assert useListSome(array, fn) == expected


@pytest.mark.parametrize(
    "array1,array2,key,expected",
    [
        ([{"id": 1, "age": 18}], [{"id": 1, "name": "miclon"}], "id", [{"id": 1, "age": 18, "name": "miclon"}]),
        ([{"id": 1, "age": 18}], [{"name": "miclon"}], "id", [{'id': 1, "age": 18}, {'name': 'miclon'}]),
        ([{"id": 1, "age": 18}], [], "id", [{"id": 1, "age": 18}]),
    ]
)
def test_useListMergeByKey(array1, array2, key, expected):
    assert useListMergeByKey(array1, array2, key) == expected
