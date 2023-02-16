from uuid import uuid4


def gen_unique_id():
    return f"{uuid4().hex}"
