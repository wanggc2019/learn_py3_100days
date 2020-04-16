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


if __name__ == '__main__':
    main()


"""
countdown:5
countdown:4
countdown:3
countdown:2
countdown:1
Countdown Over
"""