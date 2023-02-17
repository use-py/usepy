---
outline: deep
---

:::tip
python中的目录的功能扩展，核心是`pathlib`库
:::

## usePath <Badge type="warning" text="beta" />


### get_current_path

获取当前文件的路径。

```python
def get_current_path() -> Path:
    """
    获取当前文件的路径
    :return: 当前文件的路径
    """
    ...
```

### exists

判断文件或目录是否存在。

```python
def exists(path: Union[str, Path]) -> bool:
    """
    判断文件或目录是否存在
    :param path: 文件或目录
    :return: 是否存在
    """
    ...
```


### mk_dirs

创建多级目录。

```python
def mk_dirs(dir_path: str, mode=0o777) -> Path:
    """
    创建多级目录
    :param dir_path: 目录路径
    :param mode: 权限 0o777
    :return: 目录路径
    """
    ...
```


### rename

重命名文件或目录。

```python
def rename(old_path: str, new_path: str) -> None:
    """
    重命名文件或目录
    :param old_path: 旧路径
    :param new_path: 新路径
    :return:
    """
    ...
```


### listdir

获取目录下的目录列表。

```python
def listdir(path: str, sub_dir: bool = True) -> List[Path]:
    """
    列出目录下的所有目录
    :param path: 目录路径
    :param sub_dir: 是否包含子目录
    :return: 文件和目录列表
    """
    ...
``` 


### listfile

获取目录下的文件列表。

```python
def listfile(path: str, sub_dir: bool = True, suffix_list: List[str] = None) -> List[Path]:
    """
    列出目录下的所有文件
    :param path: 目录路径
    :param sub_dir: 是否包含子目录
    :param suffix_list: 文件后缀列表
    :return: 文件列表
    """
    ...
```


### list

获取目录下的文件和目录列表。

```python
def list(path: str, sub_dir: bool = True, suffix_list: List[str] = None) -> List[Path]:
    """
    列出目录下的所有文件和目录
    :param path: 目录路径
    :param sub_dir: 是否包含子目录
    :param suffix_list: 文件后缀列表
    :return: 文件和目录列表
    """
    ···
```
