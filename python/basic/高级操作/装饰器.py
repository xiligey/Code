# coding=utf-8
import functools


def log1(func):
    def w(*args, **kw):
        print('call %s' % func.__name__)
        return func(*args, **kw)
    return w


@log1
def today():
    print('1')


today()


def log2(text=None):
    def d(func):
        @functools.wraps(func)  # 加不加好像都一样??TODO
        def w(*args, **kw):
            if text is not None:
                print(text)
            print('call %s' % func.__name__)
            return func(*args, **kw)
        return w
    return d


@log2('12411543')
def tomorrow():
    print(2)


tomorrow()
