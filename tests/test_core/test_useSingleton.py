from usepy import useSingleton


def test_singleton():
    @useSingleton
    class Foo(object):
        pass

    foo = Foo()
    foo2 = Foo()
    assert foo is foo2
