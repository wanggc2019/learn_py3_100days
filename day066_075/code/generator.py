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


生成器 - 数据的生产者。

讨论yield关键字
带有 yield 的函数在 Python 中被称之为 generator（生成器）
"""

from time import sleep


def countdown(n):
    while n > 0:
        yield n
        n -= 1


def main():
    for num in countdown(5):
        print('countdown:%d' % num)
        sleep(1)
    print('Countdown Over')


"""
生成器还可以叠加来组成生成器管道
"""


# 斐波那契数列生成器Fibonacci
def fib():
    a, b = 0, 1
    while True:
        a, b = b, a + b
        yield b


# 偶数生成器
def even(gen):
    for val in gen:
        if val % 2 == 0:
            yield val


def main2():
    gen = even(fib())
    for _ in range(10):
        print(next(gen))


if __name__ == '__main__':
    main()
    main2()


"""
countdown:5
countdown:4
countdown:3
countdown:2
countdown:1
Countdown Over
"""