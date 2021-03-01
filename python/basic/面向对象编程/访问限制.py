# coding=utf-8


class Student(object):

    def __init__(self, name, score, phone, address):
        self.name = name
        self.score = score
        self.__phone = phone  # __开头表示私有变量, 内部可以访问, 外部不能
        self.__address = address

    def print_phone(self):
        print self.__phone


A = Student('xilige', 100, 10086, 'China')
A.print_phone()
# print A.__phone  # 这样访问不了,因为phone是私有变量
print A.name
print A._Student__phone  # 双下划线变量可以通过此方法来访问
