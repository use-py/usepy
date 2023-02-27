---
outline: deep
---

::: info

    @Author: MicLon
    @Date: 2023/02/27
    @Description: 单例模式装饰器

:::

## 介绍

一个多线程安全的单例模式装饰器。

## 使用

`@useSingleton`单例模式装饰器，同样适用于多线程环境下。

```python
@useDecorator.singleton
class A:
    pass

a = A()
b = A()
assert a is b  # pass
```
