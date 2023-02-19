from docstring_parser import parse
import inspect

from usepy import useIs, useTo


# 获取模块中所有方法
def get_all_methods(module):
    methods = {}
    for name in dir(module):
        if name.startswith('_') or name == 'typing.Any':
            continue
        attr = getattr(module, name)
        if callable(attr):
            methods[name] = attr
    return methods


def get_module_meta(module):
    return module.__doc__


# 将函数转换为字符串
def get_doc(func):
    return inspect.getdoc(func)


# 获取函数的代码
def get_func_code(func):
    if not hasattr(func, '__name__'):
        return False
    output = '''def {func_name}({params}):
    """
    {docstring}
    """
    ...
    '''
    params = inspect.signature(func).parameters
    params = ', '.join([f'{name}' for name, param in params.items()])
    docstring = inspect.getdoc(func)
    docstring = docstring.replace('\n', '\n\t')

    return output.format(func_name=func.__name__, params=params, docstring=docstring)


def build_module_doc(module):
    methods = get_all_methods(module)
    print("::: info")
    print(get_module_meta(module))
    print(":::")
    print("\n\n")
    markdown = []
    for name, method in methods.items():
        markdown.append(f'## {name}')
        short_description = parse(get_doc(method)).short_description
        markdown.append(short_description)
        # markdown.append("\n")
        func_code = get_func_code(method)

        if func_code:
            markdown.append(
                '```python\n' + get_func_code(method) + '\n```'
            )
        else:
            markdown = []
            continue

    print('\n'.join(markdown))


if __name__ == '__main__':
    build_module_doc(useTo)
