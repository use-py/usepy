from jmespath import search
from pydantic import BaseModel
from pydantic.utils import GetterDict


class Getter(GetterDict):
    """
    自定义 GetterDict，用于 pydantic 的 orm_mode
    """

    def get(self, key, default):  # noqa
        model, data = self._obj['model'], self._obj['data']
        for name, field in model.__fields__.items():
            path = field.field_info.extra.get('path')
            if path and name == key:
                return search(path, data)
        return default


class BaseORMModel(BaseModel):
    """
    自定义 BaseModel，用于 pydantic 的 orm_mode

    example:
    class Project(BaseORMModel):
        id: str = Field(..., path="detail.id")
        url: str = Field(..., path="detail.url")
        author_name: str = Field(..., path="detail.authors[*].name")

    test_data = {
        "detail": {
            "id": "123",
            "url": "https://www.baidu.com",
            "authors": [
                {"name": "张三"},
                {"name": "李四"},
            ]
        }
    }
    project = Project.from_orm({"model": Project, "data": test_data}).dict()
    {'id': '123', 'url': 'https://www.baidu.com', 'author_name': ['张三', '李四']}
    """

    class Config:
        orm_mode = True
        getter_dict = Getter
