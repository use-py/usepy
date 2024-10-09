---
outline: deep
---
## useSnowflakeId

用于生成分布式唯一ID。

```python
from usepy import useSnowflakeId

snowflake = useSnowflakeId()
snowflake.generate_id() # 生成唯一ID
```

### 参数

- `datacenter_id`：数据中心ID，范围为0-31，可选，默认为1
- `worker_id`：工作机器ID，范围为0-31，可选，默认为1
- `sequence`：序列号，范围为0-4095，占12位，可选，默认为0

### 返回值

- `id`：唯一ID
