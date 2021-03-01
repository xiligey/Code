# coding=utf-8


class Student(object):
    __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称


s = Student()
s.name = 'xilige'
s.age = 12
# s.sex = 'female'  # 加上这行会报错, 因为slots限制了可以添加的属性

# 子类定义的属性是自身的slots加上父类的slots
