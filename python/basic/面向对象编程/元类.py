"""
使用type函数创建类,需要传递三个参数
1.class的名称
2.继承的父类的集合
3.class的方法名称与函数绑定
"""


def fn(self, name='World'):
    print('Hello', name)
Hello = type('Hello', (object,), dict(hello=fn))
h = Hello()
h.hello()
