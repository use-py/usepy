---
outline: deep
---

# pascal_case
将字符串转换为帕斯卡命名法

```python
from usepy import pascal_case
```

### 参数

- `string`: 要转换的字符串

### 例子

```python
>>> pascal_case('pascalCase')
'PascalCase'
>>> pascal_case('some whitespace')
'SomeWhitespace'
>>> pascal_case('hyphen-text')
'HyphenText'
>>> pascal_case('HTTPRequest')
'HttpRequest'
```
