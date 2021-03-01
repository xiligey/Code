# coding=utf-8

# **kwargs允许不定长度的键值对作为参数传给函数
# greet 问候


def greet_me(**kwargs):
    for key, value in kwargs.items():
        print(key, value)
    print(type(kwargs))

greet_me(name1="Michael Jack", name2="Jon Snow")
