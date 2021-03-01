"""Python运行代码时不强制执行函数和变量的类型注解，但这些注解可用于类型检查器、IDE、静态检查器等第三方工具，也方便于他人阅读你的代码"""

from typing import List
from typing import NewType


# 1、简单例子
# say_something函数中，参数something的类型是str，返回类型是None


def say_something(something: str) -> None:
    print(something)


# 2、类型别名
# 把类型赋予别名，这里的T和List[float]等价，可互换
T = List[float]


def say_numbers(numbers: T) -> None:
    for number in numbers:
        print(number)


# 如下调用方式会触发mypy报错
say_numbers([1, 3, 4, 5, 6, "str"])

# 3、NewType
# NewType()是一个辅助函数，用于创建不同的新类型
UserId = NewType('UserId', int)  # 这里UserId类型是int型的子类
some_id = UserId(9527)


def print_user_id(id_: UserId) -> None:
    print(id_)


# 调用print_user_id时，传入int不能通过类型检查(但不影响程序运行😅)，传some_id可以
print_user_id(9527)
print_user_id(some_id)

# 3、可调对象Callable
# TODO: 类型提示(https://docs.python.org/zh-cn/3/library/typing.html)
