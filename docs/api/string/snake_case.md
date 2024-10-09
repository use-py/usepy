---
outline: deep
---

# snake_case
将字符串转换为下划线命名法

```python
from usepy import snake_case
```

### 参数

- `string`: 要转换的字符串

### 例子

```python
>>> snake_case('camelCase')
'camel_case'
>>> snake_case('some whitespace')
'some_whitespace'
>>> snake_case('hyphen-text')
'hyphen_text'
>>> snake_case('HTTPRequest')
'http_request'
```
