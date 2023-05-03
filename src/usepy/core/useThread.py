import functools
from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED


class useThread:
    pool: "_Pool"

    def __init__(self, num=1, *args, **kwargs):
        self.num = num

    def __call__(self, func):
        @functools.wraps(func)
        def _wrapper(*args, **kwargs):
            with ThreadPoolExecutor(max_workers=self.num) as run_pool:
                for i in range(self.num):
                    run_pool.submit(func, *args, **kwargs)
            return func

        return _wrapper

    @staticmethod
    def pool(num): ...


class _Pool:
    jobs = []

    def __call__(self, func):
        @functools.wraps(func)
        def _wrapper(*args, **kwargs):
            self.jobs.append(
                self.pool.submit(func, *args, **kwargs)
            )

        return _wrapper

    @classmethod
    def wait(cls):
        wait(cls.jobs, return_when=ALL_COMPLETED)

    @classmethod
    def result(cls):
        return [job.result() for job in cls.jobs]


class useThreadPool(_Pool):
    jobs = []

    def __init__(self, num=10):
        self.pool = ThreadPoolExecutor(max_workers=num)


useThread.pool = useThreadPool
