class People(object):
    def __init__(self):
        self.skin = 'yellow'


class Student(object):
    # __slots__ = ('id_', 'name', 'age', 'love')
    # 创建一个class实例后可以给该实例添加class中没有的属性和方法,
    # __slot__的作用是限制类可以添加的属性和方法,且仅对当前类有效,对子类无效
    def __str__(self):
        return 'Student object (stu_id=%s,name=%s,score=%s)' % (self.id, self.name, self.score)

    __repr__ = __str__

    def __init__(self, stu_id, name, score):
        # 一定要初始化的变量
        self.id = stu_id
        self.name = name
        self.__score = score  # 加上__变成了私有变量,不可以直接访问,但是可以通过_Student__score访问
        self.__gender__ = 1  # 左右两边都有__的是特殊变量,可以直接访问
        self._classroom = 203  # 可以被访问,但请将其当做私有变量,最好不要随意访问

    # ###############################################################
    # get 方法:外部访问私有变量__score

    def get_score(self):
        return self.__score

    # set 方法:外部修改私有变量__score
    def set_score(self, score):
        if not isinstance(score, int):
            raise ValueError("score must be integer!")
        if score < 0 or score > 100:
            raise ValueError("0<=score<=100")
        self.__score = score

    # ################################################################
    # 这一部分相当于上一部分的get set方法,同时将score方法转化成属性,可以通过s.score,s.core=10来get和set
    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, my_score):
        if not isinstance(my_score, int):
            raise ValueError("Score must be integer!")
        if my_score < 0 or my_score > 100:
            raise ValueError("0<=my_score<=100")
        self.__score = my_score

    # #################################################################

    def print_score(self):
        print(self.id, self.name, self.__score, sep=', ')

    def study(self):
        print(self.name, '正在学习')

    def __len__(self):
        return 100


class GoodStudent(Student, People):  # 继承学生类和人类

    def learn(self):
        print("Learning")


class BadStudent(Student):  # 继承学生类,获得了学生类的全部功能
    pass

    # @staticmethod
    def eat(self):
        print("I am running")


if __name__ == '__main__':
    s = Student(41162010, 'xilige', 99)
    s.print_score()
    print(s.id, s.name)
    # print(s.__score)  # __score不可从外部访问,所以这一行不可运行
    print(s._Student__score)

    g = GoodStudent(41162011, 'chen', 100)
    g.print_score()

    print(type(s), type(Student), type(Student(1, 2, 3)), type(g))
    print(isinstance(s, Student), isinstance(s, GoodStudent), isinstance(g, Student), isinstance(g, GoodStudent))
    print(isinstance(s, (Student, GoodStudent)))

    # 属性和方法的操作
    print(dir(s))
    print(len(s), s.__len__())
    print(hasattr(s, 'name'), s.name, getattr(s, 'name', 404), setattr(s, 'name', 'xiligey'), s.name)

    s.love = 1
    # s.like = 2  # 这一行不能执行,因为slots限制了实例可以添加的属性和方法的名字
    s.set_score(100)
    print(s.get_score())

    print(Student(1, 2, 3))
