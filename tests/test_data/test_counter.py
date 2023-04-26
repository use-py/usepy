from usepy import useCounter


def test_inc():
    counter = useCounter(init_value=0, max_value=10)
    counter.inc()
    assert counter.get() == 1
    counter.inc(3)
    assert counter.get() == 4
    counter.inc(8)
    assert counter.get() == 10  # max


def test_dec():
    counter = useCounter(init_value=10, min_value=5)
    counter.dec(2)
    assert counter.get() == 8
    counter.dec(5)  # min_value限制
    assert counter.get() == 5


def test_use_counter():
    counter = useCounter()
    counter.set(10)
    assert counter.get() == 10
    counter.inc()
    assert counter.get() == 11
    counter.dec(2)
    assert counter.get() == 9
