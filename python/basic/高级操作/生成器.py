# coding=utf-8
import time

"""
生成器(Generators):要理解生成器,得知道以下几个概念:
    1.可迭代对象iterable:
        python中任意的对象,只要他定义了可以返回一个迭代器的__iter__方法,
        或者定义了可以支持下标索引的__getitem__方法,那它就是一个可迭代对象.
        简单地说,可迭代对象就是能提供迭代器的任意对象
    2.迭代器Iterator
        任意对象,只要定义了next(python2)或者__next__方法,那它就是一个迭代器
    3.迭代Iteration
        从某一个地方(比如一个列表)取出一个元素的过程.当我们使用一个循环来遍历某个东西时,这过程本身叫做迭代
    4.生成器Generators
        生成器也是一种迭代器,但是只能对其迭代一次.因为它们并没有把所有的值存储在内存中,而是运行时生成值.
"""


def generator_function():
    # 1.定义一个生成器:大多数时候用函数定义生成器,这里generator_function()就是一个生成器
    for x in range(10):
        yield x


# 2.迭代取出生成器中的元素
for item in generator_function():
    print(item)


# 3.生成器比函数使用更少的内存,拿菲波那切数列举例


def fibon_func(n):
    a = b = 1
    result = []
    for i in range(n):
        result.append(a)
        a, b = b, a + b
    return result


def fibon_gen(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b


if __name__ == '__main__':
    start_gen = time.time()
    for i in fibon_gen(10000):
        print(i)
    end_gen = time.time()
    start_func = time.time()
    for i in fibon_func(10000):
        print(i)
    end_func = time.time()

    print("gen", end_gen - start_gen)
    print("func", end_func - start_func)
