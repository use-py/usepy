func_str = """
from usepy.data import useString

def run_demo():
    return useString.get_middle('abc', 'a', 'c')
"""
namespace = {}
fun = compile(func_str, '<string>', 'exec')
exec(fun, namespace)
ret = namespace['run_demo']()
print("ret", ret)
