# coding=utf-8
class Animal(object):

    def run(self):
        print "Animal is running."


class Dog(Animal):

    def eat(self):
        print "Dog is eating."

    def run(self):
        print "Dog is running."


class Cat(Animal):
    pass


dog = Dog()
dog.run()
dog.eat()
