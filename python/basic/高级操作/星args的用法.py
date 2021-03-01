# coding=utf-8

# *args主要用于函数定义,预先不知道会传递多少个参数,*args传递一个参数数量可变的元组类型给函数


def test_var_args(f_arg, *args):
    print("第一个参数为", f_arg)
    print(args)
    print(type(args))
    for arg in args:
        print("下一个参数为", arg)


test_var_args(1, 3, 3, 3, 4, 3, 1, 34, 4)
