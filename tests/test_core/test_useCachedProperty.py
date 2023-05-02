from usepy import useCachedProperty


class MyClass:
    @useCachedProperty
    def number(self):
        return 1


def test_useCachedProperty():
    mc = MyClass()
    assert mc.number == 1
    assert mc._number == 1
