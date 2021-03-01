# coding=utf8
from pprint import pprint

a = [1, 2, 3, 4]
b = dict(x=1, y=2, z=3, d=1.4, e=0.5)
pprint(a)
pprint(b)
print(b)
for value, keys in b.items():
    print(value, keys)
    if keys > 1:
        break
    else:
        print(value, keys)
