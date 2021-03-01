# coding=utf-8

# 类


class Student(object):
    pass


# 类的实例
jack = Student()
print(jack, Student)

# 可以自由的给一个实例绑定属性
jack.name = 'jack'
jack.sex = 'male'
jack.age = 22


# 由于类可以起到模板的作用, 因此在创建实例的时候,可以吧一些必须绑定的属性强制写进去, 通过__init__方法
class Student2(object):

    def __init__(self, name, sex, age, grade):
        self.name = name
        self.sex = sex
        self.age = age
        self.grade = grade


tom = Student2('tom', 'mail', 23, 89)
print(tom.name)

# 数据封装


class Student3(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print self.score

    def get_grade(self):
        if self.score < 60:
            return 'C'
        elif self.score < 90:
            return 'B'
        else:
            return 'A'


s = Student3('xilige', 88)
print(s.get_grade())
