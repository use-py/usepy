---
outline: deep
---

# to_md5
将值转换为MD5哈希

```python
from usepy import to_md5
```

### 参数

- `data`: 要转换的数据

### 返回值

- `str`: MD5哈希值

### 例子

```python
>>> to_md5("hello")
'5d41402abc4b2a76b9719d911017c592'
>>> to_md5(b"hello")
'5d41402abc4b2a76b9719d911017c592'
```
