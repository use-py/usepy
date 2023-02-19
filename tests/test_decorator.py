from usepy import (
    useCachedProperty,  # noqa
    useCatchError,
    useListify,
    useRunInThread,
    useSingleton,
    useTimeIt,
)


def test_cached_property():
    class Foo(object):
        @useCachedProperty
        def bar(self):
            return 1

    foo = Foo()
    assert foo.bar == 1
    assert foo.bar == 1


def test_catch_error():
    @useCatchError()
    def foo():
        raise Exception('foo')

    @useCatchError(return_val=1)
    def foo2():
        raise Exception('foo2')

    assert foo() is None
    assert foo2() == 1


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


def test_run_in_thread():
    @useRunInThread
    def foo():
        return 1

    assert foo() is None


def test_singleton():
    @useSingleton
    class Foo(object):
        pass

    foo = Foo()
    foo2 = Foo()
    assert foo is foo2


def test_timeit():
    @useTimeIt
    def foo():
        return 1

    assert foo() == 1
