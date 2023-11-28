from usepy.contrib.pydantic_ import BaseORMModel, Field

if __name__ == "__main__":

    class Project(BaseORMModel):
        id: str = Field(..., path="detail.id")
        url: str = Field(..., path="detail.url")
        author_name: list = Field(..., path="detail.authors[*].name")

    test_data = {
        "detail": {
            "id": "123",
            "url": "https://www.baidu.com",
            "authors": [
                {"name": "张三"},
                {"name": "李四"},
            ],
        }
    }
    project = Project.from_orm({"model": Project, "data": test_data}).dict()
    print(project)
