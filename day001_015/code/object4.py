#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
面向对象编程 进阶

静态方法和类方法
静态方法和类方法都是通过给类发消息来调用的
"""

from math import sqrt


"""
静态方法
"""


class Triangle(object):
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    # 定义静态方法
    @staticmethod
    def is_valid(a, b, c):
        """
        :param a: 三角形的边长
        :param b: 三角形的边长
        :param c: 三角形的边长
        :return: 3条边长需要满足条件才能构成三角形，否则构不成三角形
        """
        return a + b > c and a + c > b and b + c > a

    # 三角形周长
    def perimeter(self):
        return self._a + self._b + self._c

    # 三角形面积
    """
    三角形3边面积公式（海伦公式）
    p=(a+b+c)/2  p是周长的一半
    S=√[p(p-a)(p-b)(p-c)] = sqrt[p(p-a)(p-b)(p-c)]
    """
    def area(self):
        p = self.perimeter() / 2
        return sqrt(p * (p - self._a) * (p - self._b) * (p - self._c))


def main():
    a = 3
    b = 4
    c = 5
    # 静态方法和类方法都是通过给类发消息来调用的
    if Triangle.is_valid(a, b, c):
        # 创建对象
        triangle = Triangle(a, b, c)

        print(triangle.perimeter())
        print(triangle.area())

        # 也可以通过给类发消息来调用对象方法
        # 但是要传入接收消息的对象作为参数
        print(Triangle.perimeter(triangle))
        print(Triangle.area(triangle))
    else:
        print("无法构成三角形")


if __name__ == '__main__':
    main()

