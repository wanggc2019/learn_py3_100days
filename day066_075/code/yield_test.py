#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
****网络爬虫****
并发下载
1、多线程和多进程回顾
threading.local类
concurrent.futures模块
分布式进程

2、协程和异步I/O
讨论yield关键字
带有 yield 的函数在 Python 中被称之为 generator（生成器）
https://www.jianshu.com/p/de796f35d590
https://www.jianshu.com/p/f85967d2e2c1
https://www.bbsmax.com/A/gGdXbLX7J4/
"""


# 通过`yield`来创建生成器
# 在Python 3中，range()与xrange()合并为range( )。
def func():
    for i in range(10):
        yield i


for n in func():
    print(n, end=' ')
print()

# 通过列表来创建生成器
list1 = [i for i in range(10)]
print(list1)


# 斐波那契（Fibonacci）数列是一个非常简单的递归数列，除第一个和第二个数外，任意一个数都可由前两个数相加得到。
def fab(m):
    n, a, b = 0, 0, 1
    while n < m:
        print(b, end=' ')
        a, b = b, a + b
        n += 1


fab(5)
print()


# 结果没有问题，但有经验的开发者会指出，直接在 fab 函数中用 print 打印数字会导致该函数可复用性较差，因为 fab 函数返回 None，其他函数无法
# 获得该函数生成的数列。要提高 fab 函数的可复用性，最好不要直接打印出数列，而是返回一个 List。以下是 fab 函数改写后的第二个版本：
def fab(m):
    n, a, b = 0, 0, 1
    list1 = []
    while n < m:
        # print(b)
        list1.append(b)
        a, b = b, a + b
        n += 1
    return list1


for i in fab(5):
    print(i, end=' ')
print()


# 改写后的 fab 函数通过返回 List 能满足复用性的要求，但是更有经验的开发者会指出，该函数在运行中占用的内存会随着参数 max 的增大而增大
# 如果要控制内存占用，最好不要用 List来保存中间结果，而是通过 iterable 对象来迭代
class Fab(object):
    def __init__(self, m):
        self.m = m
        self.n, self.a, self.b = 0, 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.n < self.m:
            r = self.b
            self.a, self.b = self.b, self.a + self.b
            self.n += 1
            return r
        raise StopIteration()


for i in Fab(5):
    print(i, end=' ')
print()


# 然而，使用 class 改写的这个版本，代码远远没有第一版的 fab 函数来得简洁。如果我们想要保持第一版 fab 函数的简洁性，同时又要获得
# iterable 的效果，yield 就派上用场了
def fab(m):
    n, a, b = 0, 0, 1
    while n < m:
        yield b
        a, b = b, a + b
        n += 1


for i in Fab(5):
    print(i, end=' ')
print()
"""
第四个版本的 fab 和第一版相比，仅仅把 print b 改为了 yield b，就在保持简洁性的同时获得了 iterable 的效果。
f = fab(5)
f.__next__()
1
f.__next__()
1
f.__next__()
2
f.__next__()
3
f.__next__()
5
"""




