# 在绑定属性时, 如果直接暴露属性, 可能导致成绩可以随便更改


class Student1(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score


s = Student1('xilige', 100)
print(s.score)
s.score = 99999
print(s.score)
# 上面这样随便改成绩可不行, score<=100, 于是, 做修改如下


class Student2(Student1):

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0~100')
        self.score = value


# 现在不可以随心所欲的设置score了
s2 = Student2('xilige', 98)
s2.set_score(10)
print(s2.score)
# s2.set_score(101)

# 但是, 上面的方法略复杂, 没有直接用属性这么简单
# @property 将方法变成属性调用


class Student3(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0-100!')
        self._score = value


s3 = Student3()
s3._score = 60
print(s3._score)
