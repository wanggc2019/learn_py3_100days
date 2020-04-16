#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
并发编程
进程池 和 线程池
ThreadPoolExecutor：线程池，提供异步调用
ProcessPoolExecutor: 进程池，提供异步调用
https://www.jianshu.com/p/4fab1ffe8665
https://mp.weixin.qq.com/s/Xdggv8YkhTuuQieLTapqHA

从Python3.2开始一个叫做concurrent.futures被纳入了标准库，而在Python2它属于第三方的futures库，需要手动安装.
这个模块中有2个类：ThreadPoolExecutor和ProcessPoolExecutor，也就是对threading和multiprocessing的进行了高级别的抽象， 暴露出统一的
接口，帮助开发者非常方便的实现异步调用
主要提供两个方法map() 和submit()。
map() 方法主要用来针对简化执行相同的方法


1、多线程：Python中通过threading模块的Thread类并辅以Lock、Condition、Event、Semaphore和Barrier等类来支持多线程编程。Python解释器通过
GIL（全局解释器锁）来防止多个线程同时执行本地字节码，这个锁对于CPython（Python解释器的官方实现）是必须的，因为CPython的内存管理并不是线
程安全的。因为GIL的存在，Python的多线程并不能利用CPU的多核特性。

2、多进程：使用多进程可以有效的解决GIL的问题，Python中的multiprocessing模块提供了Process类来实现多进程，其他的辅助类跟threading模块中的
类类似，由于进程间的内存是相互隔离的（操作系统对进程的保护），进程间通信（共享数据）必须使用管道、套接字等方式，这一点从编程的角度来讲是比较
麻烦的，为此，Python的multiprocessing模块提供了一个名为Queue的类，它基于管道和锁机制提供了多个进程共享的队列。

3、异步编程（异步I/O）：所谓异步编程是通过调度程序从任务队列中挑选任务，调度程序以交叉的形式执行这些任务，我们并不能保证任务将以某种顺序去
执行，因为执行顺序取决于队列中的一项任务是否愿意将CPU处理时间让位给另一项任务。异步编程通常通过多任务协作处理的方式来实现，由于执行时间和顺
序的不确定，因此需要通过钩子函数（回调函数）或者Future对象来获取任务执行的结果。目前我们使用的Python 3通过asyncio模块以及await和async关
键字（Python 3.5中引入，Python 3.7中正式成为关键字）提供了对异步I/O的支持。

用下面的命令运行程序并查看执行时间，例如：
time python3 example06.py
real    0m20.657s
user    1m17.749s
sys     0m0.158s
使用多进程后实际执行时间为20.657秒，而用户时间1分17.749秒约为实际执行时间的4倍
这就证明我们的程序通过多进程使用了CPU的多核特性，而且这台计算机配置了4核的CPU
"""
import concurrent.futures
import math
import time


PRIMES = [
    1116281,
    1297337,
    104395303,
    472882027,
    533000389,
    817504243,
    982451653,
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419
] * 5


def is_prime(num):
    """判断素数"""
    # assert 断言 ：用于判断一个表达式，在表达式条件为 false 的时候触发异常。
    # 断言可以在条件不满足程序运行的情况下直接返回错误，而不必等待程序运行后出现崩溃的情况，例如我们的代码只能在 Linux 系统下运行，可以先判断当前系统是否符合条件
    assert num > 0
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return num != 1


# 进程池
# COST: 9.419977903366089s
def main():
    """主函数"""
    start = time.time()
    # 进程池，不用去创建线程池或者进程池，以及队列了,使用concurrent.futures和ProcessPoolExecutor来替代线程和进程
    with concurrent.futures.ProcessPoolExecutor() as executor:
        # zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的对象，这样做的好处是节约了不少的内存。
        # 我们可以使用 list() 转换来输出列表。如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。
        # 提交的任务的函数是一样的，就可以简化成map
        for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print('%d is prime: %s' % (number, prime))
    print('COST: {}s'.format(time.time() - start))


# 线程池
# COST: 32.69093632698059s
def main2():
    """主函数"""
    start = time.time()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print('%d is prime: %s' % (number, prime))
    print('COST: {}s'.format(time.time() - start))


"""
除了用map，另外一个常用的方法是submit。如果你要提交的任务的函数是一样的，就可以简化成map。但是假如提交的任务函数是不一样的，或者执行的过程
之可能出现异常（使用map执行过程中发现问题会直接抛出错误）就要用到submit.
"""


# COST: 9.257672309875488s
def main3():
    start = time.time()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        future_to_num = {executor.submit(is_prime, num): num for num in PRIMES}
        for future in concurrent.futures.as_completed(future_to_num):
            number = future_to_num[future]
            try:
                prime = future.result()
            except Exception as e:
                print("raise an exception: {}".format(e))
            else:
                print('%d is prime: %s' % (number, prime))
    print('COST: {}s'.format(time.time() - start))


if __name__ == '__main__':
    # main()
    # main2()
    main3()
