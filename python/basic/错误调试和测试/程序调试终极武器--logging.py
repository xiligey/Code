import logging
logging.basicConfig(level=logging.INFO)
"""
调试的几种方法:
"""


# 1.打印:把可能出错的变量打印出来


def foo(s):
    n = int(s)
    print('>>>n = %d' % n)
    return 10 / n
# 但是打印最大的坏处就是将来还要删掉他,而且到处都是print就会有很多垃圾信息

# 2.断言:凡是用print辅助查看的地方,都可以用assert代替


def foo2(s):
    n = int(s)
    assert n != 0  # 断言失败,程序就会抛出AssertionError异常
    return 10/n
# 和打印差不多,到处都是assert.不过python3 -0 **.py 可以忽略assert,将assert视为pass


# 3.日志:logging.info("What do you want to show")


def foo3(s):
    n = int(s)
    logging.info('n == %d' % n)
    return 10/n
# logging的好处在于它允许你配置指定信息的记录级别,有debug,info,warning,error

# 4.pdb 略
if __name__ == '__main__':
    # foo('0')
    # foo2('0')
    foo3('0')
