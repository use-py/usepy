---
outline: deep
---

# timestamp
获取日期时间对象的时间戳

```python
from usepy import timestamp
```

### 参数

- `dt`: 日期时间对象（可选）
- `digits`: 时间戳位数，10或13（可选）

### 返回值

- `int`: 整数时间戳

### 例子

```python
>>> from usepy import timestamp, now
>>> timestamp()  # 10位时间戳
1680339000
>>> timestamp(digits=13)  # 13位时间戳
1680339000000
>>> dt = now()
>>> timestamp(dt, digits=13)
1680339000000
```
```

