from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


class Code(BaseModel):
    code: str


@app.post("/code")
def read_item(code: Code):
    func_str = """from usepy.data import useAdDict

d = useAdDict({'a': 1, 'b': 2, 'c': {'d': 3, 'e': 4}})
assert d.a == 1
assert d.c.e == 4
"""
    namespace = {}
    fun = compile(func_str, '<string>', 'exec')
    exec(fun, namespace)
    # ret = namespace['run_demo']()
    # print("ret", ret)
    print("xxxxx")
    print(namespace)
    print("yyyyy")
    return {"res": None}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, port=8000)
