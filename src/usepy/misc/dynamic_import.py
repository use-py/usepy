import importlib
import os
import sys


def dynamic_import(module_string: str):
    """
    import function from string
    >>> module, function = dynamic_import("json.dumps")
    >>> function.__name__
    'dumps'
    >>> module.__name__
    'json'
    """
    try:
        module_name, function_name = module_string.rsplit(".", 1)
        module = importlib.import_module(module_name)
    except ImportError:
        module_path, module_name, function_name = module_string.rsplit(".", 2)
        sys.path.append(os.path.abspath(module_path))
        module = importlib.import_module(module_name)
    except ValueError:
        function_name = ""
        module = importlib.import_module(module_string)
    except Exception as e:
        raise ImportError(f"无法导入 {module_string}")

    function = getattr(module, function_name, None)
    return module, function
