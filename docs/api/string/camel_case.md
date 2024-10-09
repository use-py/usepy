---
outline: deep
---

# camel_case
将字符串转换为驼峰命名法

```python
from usepy import camel_case
```

### 参数

- `string`: 要转换的字符串

### 例子

```python
>>> camel_case('camelCase')
'camelCase'
>>> camel_case('some whitespace')
'someWhitespace'
>>> camel_case('hyphen-text')
'hyphenText'
>>> camel_case('HTTPRequest')
'httpRequest'
```
