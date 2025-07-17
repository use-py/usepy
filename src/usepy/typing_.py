import sys


if sys.version_info >= (3, 10):
    from typing import Union
else:
    from typing_extensions import Union
