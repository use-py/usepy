---
outline: deep
---

# kebab_case
将字符串转换为短横线命名法

```python
from usepy import kebab_case
```

### 参数

- `string`: 要转换的字符串

### 例子

```python
>>> kebab_case('camelCase')
'camel-case'
>>> kebab_case('some whitespace')
'some-whitespace'
>>> kebab_case('hyphen-text')
'hyphen-text'
>>> kebab_case('HTTPRequest')
'http-request'
```
