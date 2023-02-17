---
outline: deep
---

## useTimer

定时器

```python

# 每隔1秒执行一次
timer = useTimer("test", lambda: print("test"), 1)
timer.scheduler()

# 取消定时器
timer.cancel()

```


## useTimerManager

定时器管理器

```python

timer1 = useTimer("test", lambda: print("test"), 1) # 每隔1秒执行一次
timer2 = useTimer("test2", lambda: print("test2"), 2) # 每隔2秒执行一次


timer_manager = useTimerManager(timer1, timer2)

timer_manager.execute() # 执行定时器
```
