---
outline: deep
---

# parse
解析日期时间字符串

```python
from usepy import parse
```

### 参数

- `time_str`: 要解析的时间字符串
- `fmt`: 时间字符串的格式（可选）

### 返回值

- `datetime`: 解析后的日期时间对象

### 例子

```python
>>> from usepy import parse, format
>>> dt = parse("2023-04-01 12:30:45")
>>> format(dt)
'2023-04-01 12:30:45'
>>> dt = parse("2023年04月01日 12时30分45秒")
>>> format(dt)
'2023-04-01 12:30:45'
```
```

</rewritten_file>
