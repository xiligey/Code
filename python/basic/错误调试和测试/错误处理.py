# coding=utf-8
import logging
# try except finally


def foo(n):
    """return 100/n"""
    return 100 / n


try:
    print(foo(0))
except ValueError, e:
    print 'ValueError:', e
except ZeroDivisionError, e:
    print 'ZeroDivisionError:', e
finally:
    print 'end'
# 异常类结构树https://docs.python.org/2/library/exceptions.html#exception-hierarchy

# 记录错误 logging模块可以记录错误信息
try:
    print(foo(0))
except StandardError, e:
    logging.exception(e)


# 抛出错误
"""
因为错误是class，捕获一个错误就是捕获到该class的一个实例。因此，错误并不是凭空产生的，而是有意创建并抛出的。Python的内置函数会抛出很多类型的错误，我们自己编写的函数也可以抛出错误。

如果要抛出错误，首先根据需要，可以定义一个错误的class，选择好继承关系，然后，用raise语句抛出一个错误的实例
"""


class FooError(StandardError):
    pass


def foo(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value: %s' % s)
    return 10 / n
