---
outline: deep
---

# is_url
检查给定的字符串是否为有效的URL

```python
from usepy import is_url
```

### 参数

- `url`: 要检查的字符串

### 例子

```python
>>> is_url("https://www.google.com")
True
>>> is_url("http://localhost:8080")
True
>>> is_url("ftp://example.com")
False
>>> is_url("not a url")
False
>>> is_url("")
False
```
