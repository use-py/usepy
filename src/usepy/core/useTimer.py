# -*- coding=utf-8 -*-
"""
定时器及定时器管理器
"""
import threading
from typing import Dict


class useTimer(object):
    __slots__ = ['_name', '_timer', '_fn', '_interval', '_ignore_ex', '_on_result', '_on_exception',
                 '_args', '_kwargs']

    def __init__(self,
                 name,
                 fn,
                 interval=7,
                 *args,
                 **kwargs):
        """
        Timer
        :param name:  timer name
        :param fn:    function which scheduler
        :param interval:  scheduler interval, default 7s
        :param args:      args in function
        :param kwargs:    kwargs in function
        """
        #
        self._name = name
        # Thread.Timer
        self._timer = None
        # function which callable
        self._fn = fn
        # timer interval default 7s
        self._interval = interval
        # whether ignore invoke exception
        self._ignore_ex = False
        self._on_result = None
        self._on_exception = None
        # function args
        self._args = args
        # function kwargs
        self._kwargs = kwargs

    @property
    def name(self):
        return self._name

    def set_name(self, name):
        self._name = name
        return self

    @property
    def fn(self):
        return self._fn

    def set_fn(self, fn):
        self._fn = fn
        return self

    @property
    def interval(self, ):
        return self._interval

    def set_interval(self, interval):
        self._interval = interval
        return self

    @property
    def ignore_ex(self):
        return self._ignore_ex

    def set_ignore_ex(self, ignore_ex):
        self._ignore_ex = ignore_ex
        return self

    @property
    def on_result(self):
        return self._on_result

    def set_on_result(self, fn):
        self._on_result = fn
        return self

    @property
    def on_exception(self):
        return self._on_exception

    def set_on_exception(self, fn):
        self._on_exception = fn
        return self

    def alive(self):
        if self._timer is None:
            return False
        return self._timer.is_alive()

    def scheduler(self, immediate=True):
        """
        开始调度
        :param immediate: 立即执行
        """
        if immediate:
            try:
                res = self._fn(*self._args, **self._kwargs)
                if self._on_result:
                    self._on_result(res)
            except Exception as ex:
                if self._on_exception:
                    self._on_exception(ex)
                if not self._ignore_ex:
                    # stop timer
                    raise ex
        self._timer = threading.Timer(self._interval, self.scheduler, kwargs={"immediate": True})
        self._timer.start()

    def cancel(self):
        if self._timer:
            self._timer.cancel()


class useTimerManager(object):
    def __init__(self, ):
        self._timers_container: Dict[str, useTimer] = {}
        self._executed = False

    def all_timers(self) -> Dict[str, useTimer]:
        return self._timers_container

    def add_timer(self, *timer: useTimer) -> 'useTimerManager':
        """
        add timer to manager
        :param timer: Timer
        :return:
        """
        for timer in timer:
            if not isinstance(timer, useTimer):
                raise TypeError("timer must be Timer instance")

            self._timers_container[timer.name] = timer
        return self

    def execute(self):
        """
        scheduler all timer in manager
        :return: None
        """
        if self._executed:
            return
        for name, timer in self._timers_container.items():
            if timer.alive():
                continue
            timer.scheduler()
        self._executed = True

    def cancel_timer(self, timer_name=None):
        """
        cancel timer , and   timer still in container
        it can execute again.
        :param timer_name:
        :return: None
        """
        timer = self._timers_container.get(timer_name)
        if timer:
            timer.cancel()

    def cancel(self):
        """
        cancel all timer in container
        :return: None
        """
        for _, timer in self._timers_container.items():
            timer.cancel()

    def stop_timer(self, timer_name):
        """
        cancel  timer and remove it from timer container
        :param timer_name:
        :return: None
        """
        self.cancel_timer(timer_name)
        self._timers_container.pop(timer_name)

    def stop(self):
        """
        remove all timer, and it can not execute again
        """
        self.cancel()
        self._timers_container.clear()
