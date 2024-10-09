---
outline: deep
---

# dynamic_import
从字符串动态导入模块和函数

```python
from usepy import dynamic_import
```

### 参数

- `module_string`: 要导入的模块和函数的字符串表示

### 返回值

- `tuple`: 包含导入的模块和函数的元组

### 例子

```python
>>> module, function = dynamic_import("json.dumps")
>>> function.__name__
'dumps'
>>> module.__name__
'json'

>>> module, function = dynamic_import("os.path.join")
>>> function.__name__
'join'
>>> module.__name__
'posixpath'  # 或 'ntpath'，取决于操作系统

>>> module, _ = dynamic_import("sys")
>>> module.__name__
'sys'
```
