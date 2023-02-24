from usepy import useTo


def demo_to():
    print("demo_to")
    print(useTo.string('https://www.baidu.com'))
    print(useTo.string(b'https://www.baidu.com'))
    print(useTo.string(123))
    print(useTo.string(123.456))
    print(useTo.string(True))
    print(useTo.string(None))
    print(useTo.string([1, 2, 3]))
    print(useTo.string({'a': 1, 'b': 2, 'c': 3}))
    pass


if __name__ == '__main__':
    demo_to()
