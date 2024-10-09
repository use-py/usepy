---
outline: deep
---

# lower_case
将字符串转换为小写并用空格分隔单词

```python
from usepy import lower_case
```

### 参数

- `string`: 要转换的字符串

### 例子

```python
>>> lower_case('camelCase')
'camel case'
>>> lower_case('some whitespace')
'some whitespace'
>>> lower_case('hyphen-text')
'hyphen text'
>>> lower_case('HTTPRequest')
'http request'
```
