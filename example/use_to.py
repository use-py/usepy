from usepy import useTo


def demo_to():
    print("demo_to")
    print(useTo.to_string('https://www.baidu.com'))
    print(useTo.to_string(b'https://www.baidu.com'))
    print(useTo.to_string(123))
    print(useTo.to_string(123.456))
    print(useTo.to_string(True))
    print(useTo.to_string(None))
    print(useTo.to_string([1, 2, 3]))
    print(useTo.to_string({'a': 1, 'b': 2, 'c': 3}))
    pass


if __name__ == '__main__':
    demo_to()
