from enum import Enum, unique

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))


print(Month.Jan, type(Month.__members__), type(Month.__members__.items()))  # 引用这个常量
for name, member in Month.__members__.items():
    # value属性是自动赋给成员的int常量,默认从1开始计数
    print(name, '=>', member, member.value)

# 如果需要更精准的控制枚举类型,可以从Enum派生出自定义类


@unique  # 保证没有重复值
class Weekday(Enum):
    Sun, Mon, Tue, Wed, Thu, Fri, Sat = range(7)

# 访问枚举类型的方法:
day1 = Weekday.Mon
print(day1, Weekday.Thu, Weekday['Tue'], Weekday.Thu.value, Weekday(1), sep='|')
