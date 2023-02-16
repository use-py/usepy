import inspect
import doctest
from doctest import DocTestParser

from typing import Optional, List

from pydantic import BaseModel

from usepy.data import useString

from docstring_parser import parse


class Function(BaseModel):
    name: str
    description: Optional[str]
    doc: Optional[str]
    demo: Optional[str]


class Class(BaseModel):
    name: str
    description: Optional[str]
    doc: Optional[str]
    functions: List[Function]


class DocParser:
    def __init__(self, doc: str):
        self.doc = doc

    @staticmethod
    def _parse_description(doc: str) -> Optional[str]:
        return None

    def parse(self):
        res = DocTestParser().parse(self.doc)
        self._parse_description(res[0])


def run_demo():
    for name, func in inspect.getmembers(useString):
        if name.startswith('_'):
            continue
        # print(name, func, func.__doc__)
        if func.__doc__:
            docstring = parse(func.__doc__)
            print(docstring.deprecation, docstring.long_description, docstring.short_description)
            print(docstring.params[0].arg_name, docstring.params[0].description, docstring.params[0].type_name)
            print(docstring.returns.description)
            # res = doctest.DocTestParser().parse(func.__doc__)
            # res = [item for item in res if item]
            # for item in res:
            #     print(item)


if __name__ == '__main__':
    run_demo()
