from usepy import chunk
from usepy.list import chunk as chunk_list

print(chunk([1, 2, 3, 4, 5], 2))
print(chunk_list([1, 2, 3, 4, 5], 2))


from usepy import AdDict

d = AdDict({"a": 1, "b": 2, "c": {"d": 3, "e": 4}})
print(d.a)
print(d.c.e)


from usepy import camel_case

print(camel_case("hello_world"))
