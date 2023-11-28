from usepy import useCatchError


def test_useCatchError_catches_exception():
    @useCatchError(return_val="error")
    def func():
        raise Exception("test exception")

    assert func() == "error"  # because of `useCatchError` return_val='error'


def test_catch_error():
    @useCatchError()
    def foo():
        raise Exception("foo")

    @useCatchError(return_val=1)
    def foo2():
        raise Exception("foo2")

    assert foo() is None
    assert foo2() == 1
