import pytest
from usepy import useSynchronized
import threading


@useSynchronized
def add(x, y):
    return x + y


def test_useSynchronized_decorator():

    def thread_function(result_list):
        result = add(1, 2)
        result_list.append(result)

    results = []
    threads = []
    num_threads = 10

    for _ in range(num_threads):
        thread = threading.Thread(target=thread_function, args=(results,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    assert all(result == 3 for result in results)

