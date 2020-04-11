#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
面向对象编程
定义类 和 对象

封装 、 继承、 多态
"""


# 定义类
class Student:
    # __init__是一个特殊方法用于在创建对象时进行初始化操作
    # 通过这个方法我们可以为学生对象绑定name和age两个属性
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 定义方法
    def study(self, course_name):
        print("{0}正在学习{1}".format(self.name, course_name))

    # PEP 8要求标识符的名字用全小写多个单词用下划线连接
    # 但是部分程序员和公司更倾向于使用驼峰命名法(驼峰标识)
    # 就是不用下划线等连接单词，用大写 如 my_name,驼峰写法：myName,或者MyName，类似java的写法
    def play_game(self):
        if self.age < 18:
            print("%s年方%s,只能玩qq飞车" % (self.name, self.age))
        else:
            print("%s年方%s,可以玩王者农药了" % (self.name, self.age))


# 定义对象
def main():
    # 创建对象
    student1 = Student('Pony马', 17)
    student2 = Student('Jack马', 22)
    # 给对象发study消息
    student1.study("数学")
    student2.study("英语")
    # 给对象发play_game消息
    student1.play_game()
    student2.play_game()


"""
访问权限问题
# python属性只有 公有 和 私有
# 私有属性前加 __
"""


class Test:
    # 初始化对象
    def __init__(self, foo):
        # 私有属性 foo
        self.__foo = foo

    # 私有的方法
    def __bar(self):
        print(self.__foo)
        print("__bar")


def main2():
    test = Test("Hello")  # foo = hello
    # __bar()是私有的方法，所以对象无权限访问
    # test.__bar()   # AttributeError: 'Test' object has no attribute '__bar'
    # Hello
    # __bar
    test._Test__bar()
    # 因为__foo是私有的属性，对象无权限访问该属性
    # print(test.__foo)   # AttributeError: 'Test' object has no attribute '__foo'
    # Hello
    print(test._Test__foo)


if __name__ == '__main__':
    main()
    main2()


"""
Python并没有从语法上严格保证私有属性或方法的私密性，它只是给私有的属性和方法换了一个名字来妨碍对它们的访问，事实上如果你知道更换名字的规则
仍然可以访问到它们，下面的代码就可以验证这一点。之所以这样设定，可以用这样一句名言加以解释，就是"We are all consenting adults here"。
因为绝大多数程序员都认为开放比封闭要好，而且程序员要自己为自己的行为负责。

在实际开发中，我们并不建议将属性设置为私有的，因为这会导致子类无法访问（后面会讲到）。所以大多数Python程序员会遵循一种命名惯例就是让属性名
以单下划线开头来表示属性是受保护的，本类之外的代码在访问这样的属性时应该要保持慎重。这种做法并不是语法上的规则，单下划线开头的属性和方法外界
仍然是可以访问的，所以更多的时候它是一种暗示或隐喻
"""
