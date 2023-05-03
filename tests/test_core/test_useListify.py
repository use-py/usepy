from usepy import useListify


def test_listify():
    @useListify()
    def foo():
        yield 1

    @useListify()
    def foo2():
        yield 1
        yield 2

    @useListify(dict)
    def foo3():
        yield 'a', 1
        yield 'b', 2

    assert foo() == [1]
    assert foo2() == [1, 2]
    assert foo3() == {'a': 1, 'b': 2}
