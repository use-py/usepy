---
outline: deep
---

::: info

    @Author: MicLon
    @Date: 2023/02/27
    @Description: 将函数放入线程中执行

:::

## 使用

  `@useRunInThread`装饰器，用于将函数放入线程中执行
  
  ```python
@useDecorator.run_in_thread
def run_in_thread():
    time.sleep(1)
    print('run_in_thread')

# 同时执行3个线程
for i in range(3):
    run_in_thread()
```
