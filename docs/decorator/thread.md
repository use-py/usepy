---
outline: deep
---

::: info

    @Author: MicLon
    @Date: 2023/02/27
    @Description: 线程与线程池装饰器

:::


## 介绍

它是一个不破坏原函数功能的基础上，为函数添加线程功能的装饰器。

## 使用

```python{3}
import time

from usepy import useThread


# 一个拥有10个线程的线程池
@useThread.pool(num=10)
def demo_func(name):
    print("Thread %s: starting", f"<{name}>")
    time.sleep(2)
    print("Thread %s: finishing", f"<{name}>")


# 直接5个线程执行
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
```
