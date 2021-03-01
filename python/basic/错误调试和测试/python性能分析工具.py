# coding=utf-8
import profile


def test():
    for i in range(10000):
        j = i*i
        print(j)
profile.run('test()')
