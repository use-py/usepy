import inspect


def useFuncName(cls=None):
    """在函数/方法中取自身名称，如果参数cls不为空则返回 类名.方法名

    :param cls: 类对象
    :return: 格式：[cls_name.]func_name
    """
    return ('' if cls is None else cls.__class__.__name__ + '.') + inspect.stack()[1][3]
