from usepy import useRunInThread


def test_run_in_thread():
    @useRunInThread
    def foo():
        return 1

    assert foo() is None
