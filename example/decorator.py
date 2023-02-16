import logging
import time

from usepy.decorator import useDecorator, useSingleton

logging.basicConfig(level=logging.DEBUG)


@useSingleton
class Test:
    pass


@useDecorator.singleton
class Test2:
    pass


@useDecorator.catch_error()
def exception_demo():
    raise Exception('test')


@useDecorator.except_debug
def error2():
    1 / 0


@useDecorator.timeit
def timeit():
    time.sleep(1)


@useDecorator.run_in_thread
def run_in_thread():
    time.sleep(1)
    print('run_in_thread')


@useDecorator.listify()
def listify():
    yield 1


@useDecorator.listify(collection=set)
def listify2():
    yield 1
    yield 2
    yield 2


@useDecorator.listify(collection=dict)
def listify3():
    yield 1, 2
    yield 2, 3
    yield 2, 4


if __name__ == '__main__':
    listify()  # [1]
    listify2()  # {1, 2}
    listify3()  # {1: 2, 2: 3}
