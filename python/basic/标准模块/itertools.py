# coding=utf-8

naturals = itertools.count(10)  # 自然数序列,从10开始
print(type(naturals))
# for n in naturals:
#     print(n)

cd = itertools.cycle('ABCDEFGHIJKLMNOPQRSTUVWXYZ')  # 无限循环
# for c in cd:
#     print(c)

ns = itertools.repeat('ABC', 10)  # 重复十次
for n in ns:
    print(n)

# 无限序列虽然可以一直迭代下去,但是我们可以通过takewhile()来截取
ns = itertools.takewhile(lambda x: x < 100, naturals)
print(list(ns))

# chain可以把一组迭代对象串联起来,形成一个更大的迭代器
for c in itertools.chain('ABC', 'DEF'):
    print(c)
