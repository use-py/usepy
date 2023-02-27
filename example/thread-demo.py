import time

from usepy import useThread


@useThread.pool(num=10)
def demo_func(name):
    print("Thread %s: starting", f"<{name}>")
    time.sleep(2)
    print("Thread %s: finishing", f"<{name}>")


@useThread(5)
def demo_run_thread():
    demo_func(name='demo_run_thread')


def demo_run_thread_pool():
    for _ in range(10):
        demo_func(name='demo_run_thread_pool')


if __name__ == '__main__':
    demo_run_thread_pool()
    useThread.pool.wait()
    demo_run_thread()
