# coding=utf-8
def a_new_decorator(a_func):

    def wrapthefunction():
        print("I'm doing some boring work before executing a_func()")

        a_func()

        print("I'm doing some boring work after executing a_func()")
    return wrapthefunction


def a_function_requiring_decoration():
    print("我是需要装饰的函数")

a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)
a_function_requiring_decoration()
# a_new_decorator(a_function_requiring_decoration)()


@a_new_decorator
def a_function_requiring_decoration2():
    print("我是需要装饰的函数2")
a_function_requiring_decoration2()
"""
蓝本规范
from functools import wraps

def decorator_name(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if can_not_run:
            return "Function will not run."
        :return f(*args, **kwargs)
    return decorated

@decorator_name
def func():
    return "Function is running"

can_run = True
print func()
can_run = False
print func()
"""