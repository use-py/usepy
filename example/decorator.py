import logging
import time

from usepy import useCatchError, useListify, useRunInThread, useSingleton, useTimeIt

logging.basicConfig(level=logging.DEBUG)


@useSingleton
class Test:
    pass


@useSingleton
class Test2:
    pass


@useCatchError()
def exception_demo():
    raise Exception("test")


@useTimeIt
def timeit():
    time.sleep(1)


@useRunInThread
def run_in_thread():
    time.sleep(1)
    print("run_in_thread")


@useListify()
def listify():
    yield 1


@useListify(collection=set)
def listify2():
    yield 1
    yield 2
    yield 2


@useListify(collection=dict)
def listify3():
    yield 1, 2
    yield 2, 3
    yield 2, 4


if __name__ == "__main__":
    listify()  # [1]
    listify2()  # {1, 2}
    listify3()  # {1: 2, 2: 3}
