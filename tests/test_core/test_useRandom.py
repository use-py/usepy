from usepy import useRandomString, useRandomUUID


def test_uuid():
    assert useRandomUUID() != useRandomUUID()
    assert len(useRandomUUID()) == 32


def test_random():
    assert useRandomString(10) != useRandomString(10)
    assert len(useRandomString(min_len=10, max_len=10)) == 10
    assert len(useRandomString(max_len=3)) <= 3
    assert len(useRandomString(min_len=30)) >= 30
