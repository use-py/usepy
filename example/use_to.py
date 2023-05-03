from usepy import useToString


def demo_to():
    print("demo_to")
    print(useToString('https://www.baidu.com'))
    print(useToString(b'https://www.baidu.com'))
    print(useToString(123))
    print(useToString(123.456))
    print(useToString(True))
    print(useToString(None))
    print(useToString([1, 2, 3]))
    print(useToString({'a': 1, 'b': 2, 'c': 3}))
    pass


if __name__ == '__main__':
    demo_to()
