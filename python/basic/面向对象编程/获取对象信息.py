# coding=utf-8
import types
# 获取对象类型
print type(123)
print type('123')
print type(None)
print type(type)
print type(map)

print isinstance(123, types.IntType)
print isinstance('123', types.StringType)
print isinstance(int, types.TypeType)  # 类型本身的类型是TypeType

# 获取一个对象的所有属性和方法
print dir(dir)

# getattr, setattr, hasattr


class A(object):

    def __init__(self):
        self.x = 9
        self.y = 10

    def power(self):
        return self.x**2


a = A()
print hasattr(a, 'x')
print hasattr(a, 'y')
print hasattr(a, 'z')

setattr(a, 'z', 11)
print hasattr(a, 'z')

print getattr(a, 'x')
print getattr(a, 'y')
print getattr(a, 'z')
