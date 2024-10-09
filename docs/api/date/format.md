---
outline: deep
---

# format
格式化日期时间对象

```python
from usepy import format
```

### 参数

- `dt`: 要格式化的datetime对象
- `fmt`: 格式化字符串（可选）

### 例子

```python
>>> from datetime import datetime
>>> dt = datetime(2023, 4, 1, 12, 30, 45)
>>> format(dt)
'2023-04-01 12:30:45'
>>> format(dt, "%Y年%m月%d日 %H时%M分%S秒")
'2023年04月01日 12时30分45秒'
```
