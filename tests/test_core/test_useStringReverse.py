from usepy import useStringReverse


def test_reverse():
    assert useStringReverse("") == ""
    assert useStringReverse("abc") == "cba"
    assert useStringReverse("abc123") == "321cba"
    assert useStringReverse("abc123def") == "fed321cba"
