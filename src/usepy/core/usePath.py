import pathlib
from pathlib import Path
from typing import List, Union


class usePath(object):

    @staticmethod
    def get_current_path() -> Path:
        """
        获取当前路径
        :return: 当前路径
        """
        return pathlib.Path().absolute()

    @staticmethod
    def exists(path: Union[str, Path]) -> bool:
        """
        判断文件或目录是否存在
        :param path: 路径
        :return: 是否存在
        """
        return pathlib.Path(path).exists()

    @staticmethod
    def mk_dirs(dir_path: str, mode=0o777) -> Path:
        """
        创建多级目录
        :param dir_path: 目录路径
        :param mode: 权限 0o777
        :return: 目录路径
        """
        pathlib.Path(dir_path).mkdir(parents=True, exist_ok=True, mode=mode)
        return pathlib.Path(dir_path)

    @staticmethod
    def rename(old_path: str, new_path: str) -> None:
        """
        重命名文件或目录
        :param old_path: 旧路径
        :param new_path: 新路径
        :return:
        """
        if not pathlib.Path(old_path).exists():
            raise FileNotFoundError(f'{old_path} not found')
        pathlib.Path(old_path).rename(new_path)

    @staticmethod
    def _list_path(path: str, sub_dir: bool = True) -> List[Path]:
        """
        迭代目录
        :param path: 目录路径
        :param sub_dir: 是否包含子目录
        :return: 迭代器
        """
        _path = pathlib.Path(path)
        _glob = _path.glob('*') if not sub_dir else _path.rglob('*')
        return [p for p in _glob if p.exists()]

    @staticmethod
    def listdir(path: str, sub_dir: bool = True) -> List[Path]:
        """
        列出目录下的所有目录
        :param path: 目录路径
        :param sub_dir: 是否包含子目录
        :return: 文件和目录列表
        """
        return [p for p in usePath._list_path(path, sub_dir) if p.is_dir()]

    @staticmethod
    def listfile(path: str, sub_dir: bool = True, suffix_list: List[str] = None) -> List[Path]:
        """
        列出目录下的所有文件
        :param path: 目录路径
        :param sub_dir: 是否包含子目录
        :param suffix_list: 文件后缀列表
        :return: 文件列表
        """
        suffix_list = suffix_list or []
        return [p for p in usePath._list_path(path, sub_dir) if p.is_file() and p.suffix in suffix_list]

    @staticmethod
    def list(path: str, sub_dir: bool = True, suffix_list: List[str] = None) -> List[Path]:
        """
        列出目录下的所有文件和目录
        :param path: 目录路径
        :param sub_dir: 是否包含子目录
        :param suffix_list: 文件后缀列表
        :return: 文件和目录列表
        """
        suffix_list = suffix_list or []
        return [p for p in usePath._list_path(path, sub_dir) if p.suffix in suffix_list]
