#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
进程和线程

多线程
"""

from random import randint
from threading import Thread
from time import time, sleep


def download_task(filename):
    print("开始下载 %s...." % filename)
    time2download = randint(5, 10)
    sleep(time2download)
    print("%s 下载完成,耗费%ds" % (filename, time2download))


def main():
    start_time = time()
    t1 = Thread(target=download_task, args=("快速赚钱100w.mp4", ))
    t1.start()
    t2 = Thread(target=download_task, args=("攻略指南.mp4", ))
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print("下载完成，共耗费%ds" % (end - start_time))


"""
通过继承Thread类的方式来创建自定义的线程类，然后再创建线程对象并启动线程
"""


class DownloadTask(Thread):
    def __init__(self, filename):
        super().__init__()
        self._filename = filename

    def run(self):
        print("开始下载 %s...." % self._filename)
        time2download = randint(5, 10)
        sleep(time2download)
        print("%s 下载完成,耗费%ds" % (self._filename, time2download))


def main2():
    start_time = time()
    t1 = DownloadTask("it苟如何提升魅力.pdf")
    t1.start()
    t2 = DownloadTask("论it苟跪舔的n种方式.pdf")
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print("下载完成，共耗费%ds" % (end - start_time))


if __name__ == '__main__':
    # main()
    main2()


"""
开始下载 快速赚钱100w.mp4....
开始下载 攻略指南.mp4....
攻略指南.mp4 下载完成,耗费6s
快速赚钱100w.mp4 下载完成,耗费9s
下载完成，共耗费9s
"""

"""
开始下载 it苟如何提升魅力.pdf....
开始下载 论it苟跪舔的n种方式.pdf....
it苟如何提升魅力.pdf 下载完成,耗费7s
论it苟跪舔的n种方式.pdf 下载完成,耗费9s
下载完成，共耗费9s
"""