---
outline: deep
---

# now
获取当前日期时间

```python
from usepy import now
```

### 返回值

- `datetime`: 当前日期时间对象

### 例子

```python
>>> from usepy import now, format
>>> current_time = now()
>>> format(current_time)
'2023-04-01 15:30:00'  # 实际输出会根据当前时间而变化
```
```

