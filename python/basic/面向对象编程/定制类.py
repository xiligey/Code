# coding=utf-8
"""
看到类似__slots__这种形如__xxx__的变量或者函数名就要注意，这些在Python中是有特殊用途的。

__slots__我们已经知道怎么用了，__len__()方法我们也知道是为了能让class作用于len()函数。

除此之外，Python的class中还有许多这样有特殊用途的函数，可以帮助我们定制类
"""
# __str__返回用户看到的字符串, __repr__返回开发者看到的字符串


class Student(object):
    def __init__(self, name):
        self.name = name


print(Student('Michael'))


class Student2(Student):
    def __str__(self):
        return 'Student object (name: %s)' % self.name


print(Student2('Michael'))


class Student3(Student2):
    def __str__(self):
        return 'Student object (name: %s)' % self.name
    __repr__ = __str__


s = Student3('Michael')
print(s)

# __iter__
# 如果一个类想for ... in 循环, 则必须实现一个__iter__方法,该方法返回一个迭代对象


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def next(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 10000:
            raise StopIteration()
        return self.a


for i in Fib():
    print(i)

# __getitem__
# 添加[]索引功能


class Fib2(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a


f = Fib2()
print(f[4])


# 但是只能索引, 不能切片, 所以判断传入的参数n是int还是slice(切片对象)


class Fib3(object):
    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

f = Fib3()
print(f[3])
print(f[3:10])
"""
也没有对负数作处理，所以，要正确实现一个__getitem__()还是有很多工作要做的。

此外，如果把对象看成dict，__getitem__()的参数也可能是一个可以作key的object，例如str。

与之对应的是__setitem__()方法，把对象视作list或dict来对集合赋值。最后，还有一个__delitem__()方法，用于删除某个元素。

总之，通过上面的方法，我们自己定义的类表现得和Python自带的list、tuple、dict没什么区别，这完全归功于动态语言的“鸭子类型”，不需要强制继承某个接口。
"""

# __gerattr__
"""
正常情况下，当我们调用类的方法或属性时，如果不存在，就会报错
Python还有另一个机制，那就是写一个__getattr__()方法，动态返回一个属性
"""


class Student(object):
    """docstring for Student."""
    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, attr):
        if attr == 'score':
            return 99

s = Student()
print(s.name)
print(s.score)

# __call__
# 一个对象实例可以有自己的属性和方法，当我们调用实例方法时，我们用instance.method()来调用。能不能直接在实例本身上调用呢？类似instance()？在Python中，答案是肯定的。


class Student4(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s' % self.name)


s5 = Student4('Michael')
print(s5())
