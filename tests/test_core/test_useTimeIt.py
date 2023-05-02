from usepy import useTimeIt


def test_timeit():
    @useTimeIt
    def foo():
        return 1

    assert foo() == 1
