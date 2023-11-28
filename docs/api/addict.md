---
outline: deep
---
## useAdDict

用于解决字典取值繁琐的问题。

```python
from usepy import useAdDict

d = useAdDict({'a': 1, 'b': 2, 'c': {'d': 3, 'e': 4}})
assert d.a == 1
assert d.c.e == 4
```
