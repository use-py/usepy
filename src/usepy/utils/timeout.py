import threading
from typing import Optional, Callable


class useTimeoutFn(object):

    def __init__(self, interval: float, cb: Callable, immediate: bool = False):
        """
        :param interval: 超时时间
        :param cb: 超时后回调
        :param immediate: 立即执行
        """
        self._timer: Optional[threading.Timer] = None
        self.is_pending: bool = False
        self._interval = interval
        self._cb = cb

        if immediate:
            self.start()

    def stop(self):
        self.is_pending = False
        if self._timer is not None:
            self._timer.cancel()

    def start(self):
        self.is_pending = True
        self._timer = threading.Timer(self._interval, self._cb)
        self._timer.start()


def useTimeout(interval):
    return useTimeoutFn(interval, lambda: ...)
