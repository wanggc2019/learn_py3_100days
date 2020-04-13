#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
进程和线程

多进程
"""

from random import randint
from time import time, sleep
from multiprocessing import Process
from os import getpid


"""
未使用多进程
顺序下载，耗费时间是2个任务之和
"""


def download_task(filename):
    print("开始下载 %s...." % filename)
    time2download = randint(5, 10)
    sleep(time2download)
    print("%s 下载完成,耗费%ds" % (filename, time2download))


def main():
    start_time = time()
    download_task("如何套取富婆欢心.pdf")
    download_task("如何暴富.pdf")
    end = time()
    print("下载完成，共耗费%ds" % (end - start_time))


"""
使用多进程
“同时开始”，耗费时间是最后完成的任务的时间
"""


def download_task2(filename):
    print("启动下载进程,pid=[%d]." % getpid())
    print("开始下载 %s...." % filename)
    time2download = randint(5, 10)
    sleep(time2download)
    print("《%s》下载完成,耗费%ds" % (filename, time2download))


# 使用多进程
def main2():
    start = time()
    # 通过Process类创建了进程对象，通过target参数传入一个函数来表示进程启动后要执行的代码，后面的args是一个元组，它代表了传递给函数的参数
    p1 = Process(target=download_task2, args=("如何泡上白富美.pdf", ))
    # Process对象的start方法用来启动进程
    p1.start()
    p2 = Process(target=download_task2, args=("如何让妹子爱上我.pdf", ))
    p2.start()
    # join方法表示等待进程执行结束
    p1.join()
    p2.join()
    end = time()
    print("共耗费了%ds" % (end - start))


if __name__ == '__main__':
    # main()
    main2()

"""
开始下载《如何套取富婆欢心.pdf》....
《如何套取富婆欢心.pdf》下载完成,耗费10s
开始下载《如何暴富.pdf》....
《如何暴富.pdf》下载完成,耗费10s
下载完成，共耗费20s
"""

"""
启动下载进程,pid=[23800].
开始下载 如何泡上白富美.pdf....
启动下载进程,pid=[1308].
开始下载 如何让妹子爱上我.pdf....
《如何泡上白富美.pdf》下载完成,耗费7s
《如何让妹子爱上我.pdf》下载完成,耗费7s
共耗费了7s
"""

