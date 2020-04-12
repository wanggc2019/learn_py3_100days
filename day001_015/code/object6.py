#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
面向对象编程 进阶

继承和多态
和java类似
"""
"""
继承
子类除了继承父类提供的属性和方法，还可以定义自己特有的属性和方法，所以子类比父类拥有的更多的能力
"""


# 定义父类
class Person(object):
    # 限定Person对象只能绑定_name, _age和_gender属性
    # __slots__ = ('_name', '_age', '_gender')

    # __init__是一个特殊方法用于在创建对象时进行初始化操作
    # 通过这个方法我们可以为对象绑定name和age两个属性
    def __init__(self, name, age):
        self._name = name
        self._age = age

    '''
    name的getter和setter
    '''
    # 访问器 - getter方法
    @property
    def name(self):
        return self._name

    # 修改器 - setter方法
    @name.setter
    def name(self, name):
        self._name = name

    '''
    age的getter 和 setter
    '''
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    # 定义方法
    def study(self):
        print("%d岁的%s在学习" % (self._age, self._name))

    def play_game(self):
        if self.age < 18:
            print("%s年方%s,只能玩qq飞车" % (self._name, self._age))
        else:
            print("%s年方%s,可以玩王者农药了" % (self._name, self._age))


# 定义子类
class Student(Person):
    # 子类自己的属性gender
    def __init__(self, name, age, gender):
        super().__init__(name, age)
        self._gender = gender

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, gender):
        self._gender = gender

    # 子类自己的方法
    def do_homework(self, course):
        print("%d岁的学生%s%s做%s家庭作业" % (self._age, self._gender, self._name, course))


# 定义子类
class Teacher(Person):
    def __init__(self, name, age, money):
        super().__init__(name, age)
        self._money = money

    @property
    def money(self):
        return self._money

    @money.setter
    def money(self, money):
        self._money = money

    def work(self, course):
        print("%d岁的老师%s上%s课且收了%d元钱" % (self._age, self._name, course, self.money))


def main():
    student = Student("poney马", 16, '男')
    # 调用父类的方法
    student.study()
    student.play_game()
    # 调用自己的方法
    student.do_homework("数学")

    teacher = Teacher('jack马', 20, 30000)
    # 调用父类的方法
    teacher.study()
    teacher.play_game()
    # 调用自己的方法
    teacher.work("英语")


if __name__ == '__main__':
    main()
