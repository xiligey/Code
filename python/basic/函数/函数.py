# 无参函数
def f1():
    return 'Hello World'

# 带普通参数
def f2(i):
    return i + 1


# 参数带默认值
def f3(i, j=1, k=2):
    return i + j + k


# 带*args参数
def f4(i, *array):
    return [i + j for j in array]


# 带**kwargs参数
def f5(i, **dict1):
    result = {}
    for d in dict1.keys():
        result[d] = dict1[d] + i
    return result


# 匿名函数
f6 = lambda x: x + 1

if __name__ == '__main__':
    print(f4(1, *[2, 3, 4]))
    print(f5(1, **{'a': 1, 'b': 2, 'c': 3}))
    print(f6(3))
