# coding=utf-8
import pdb

"""
1.从命令行使用python debugger调试脚本
python -m pdb my_script.py
2.从脚本内部设置断点
import pdb:
    pdb.set_trace()
    c:继续执行
    w:显示正在执行的代码的上下文信息
    a:打印当前函数的参数列表
    s:执行当前代码行,并停留在第一个能停留的地方(相当于单步进入)
    n:继续执行到当前函数的下一行,或者在当前行直接返回(单步跳过)
    单步跳过和单步进入的区别在于:
        单步跳过会直接执行完当前行调用的函数,停在下一行
        而单步进入则会进入到当前调用的函数内,并停留在里面

更多pdb命令请参考官方文档 https://docs.python.org/2/library/pdb.html
"""


def make_bread(*args):
    pdb.set_trace()  # 脚本内部设置断点
    for arg in args:
        print(arg)
    return "I don't have time"


print(make_bread(1, 2, 3, 3, 4, 5, 5, 21, 1))
