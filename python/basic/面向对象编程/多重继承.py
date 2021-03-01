# coding=utf-8
"""
按照哺乳动物和鸟类归类, 可以设计出这样的类的层次
           Animal
          /      \
       Mammal     Bird
      /      \   /    \
     Dog    Bat Parrot Ostrich
"""


class Animal(object):
    pass


# 大类
class Mammal(Animal):
    pass


class Bird(Animal):
    pass


# 各种动物
class Dog(Mammal):
    pass


class Bat(Mammal):
    pass


class Parrot(Bird):
    pass


class Ostrich(object):
    pass


# 给动物加上Runnable和Flyable的功能, 只需要先定义好这两个类
class Runnable(object):
    def run(self):
        print('Running...')


class Flyable(object):
    def fly(self):
        print('Flying...')


# 对于需要Runnable的动物, 就多继承一个Runnable,如DOg
class Dog2(Mammal, Runnable):
    pass


# 对于需要Flyable的动物, 就多集成一个Flyable, 如Bat
class Bat2(Mammal, Flyable):
    pass
# 通过多重继承, 一个I诶子类可以同时获取多个父类的所有功能
