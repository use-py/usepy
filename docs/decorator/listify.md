---
outline: deep
---

::: info

    @Author: MicLon
    @Date: 2023/02/27
    @Description: 将函数的返回值转换为列表

:::

## 使用

`@useListify`将函数的返回值转换为列表。

```python
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


listify()  # [1]
listify2()  # {1, 2}
listify3()  # {1: 2, 2: 3}
```
