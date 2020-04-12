#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
面向对象编程 进阶

__slots__ 限定类可以绑定的属性
"""


# 定义类
class Person(object):
    # 限定Person对象只能绑定_name, _age和_gender属性
    __slots__ = ('_name', '_age', '_gender')

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
    def study(self, course_name):
        print("{0}正在学习{1}".format(self._name, course_name))

    # PEP 8要求标识符的名字用全小写多个单词用下划线连接
    # 但是部分程序员和公司更倾向于使用驼峰命名法(驼峰标识)
    # 就是不用下划线等连接单词，用大写 如 my_name,驼峰写法：myName,或者MyName，类似java的写法
    def play_game(self):
        if self.age < 18:
            print("%s年方%s,只能玩qq飞车" % (self._name, self._age))
        else:
            print("%s年方%s,可以玩王者农药了" % (self._name, self._age))


# 定义对象
def main():
    # 创建对象
    person = Person('Pony马', 17)
    # 给对象发study消息
    person.study("数学")
    # 给对象发play_game消息
    person.play_game()
    person._gender = '男'
    # print(person._gender)
    # AttributeError: 'Person' object has no attribute '_address'
    # person._address = '深圳'


if __name__ == '__main__':
    main()
