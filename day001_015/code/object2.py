#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
面向对象编程 进阶
虽然我们不建议将属性设置为私有的，但是如果直接将属性暴露给外界也是有问题的，比如我们没有办法检查赋给属性的值是否有效
之前的建议是将属性命名以单下划线开头，通过这种方式来暗示属性是受保护的，不建议外界直接访问，那么如果想访问属性可以通过属性的getter（访问器）
和setter（修改器）方法进行对应的操作。如果要做到这点，就可以考虑使用@property包装器来包装getter和setter方法，使得对属性的访问既安全又方便
类似java
"""

'''
getter和setter访问器方法
'''


# 定义类
class Person(object):
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
    person1 = Person('Pony马', 17)
    person2 = Person('Jack马', 22)
    # 给对象发study消息
    person1.study("数学")
    person2.study("英语")
    # 给对象发play_game消息
    person1.play_game()
    person2.play_game()
    '''
    pony也想玩农药，他就改了自己的年纪
    '''
    person1.age = 30
    person1.play_game()


if __name__ == '__main__':
    main()
