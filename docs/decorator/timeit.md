---
outline: deep
---

::: info

    @Author: MicLon
    @Date: 2023/02/27
    @Description: 统计函数运行时间装饰器

:::

## 使用

`@useTimeIt`装饰器，用于统计函数执行时间

```python
@useDecorator.timeit
def test():
    time.sleep(1)

test()  # test took 1.000 seconds
```
