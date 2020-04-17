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
协程 - 数据的消费者。

"""

from time import sleep
from functools import wraps


# 生成器 数据生产者
def countdown_gen(n, consumer):
    # 激活生成器,让生成器执行到有yield关键字的地方挂起，当然也可以通过next(consumer)来达到同样的效果。如果不愿意每次都用这样的代码来
    # “预激”生成器，可以写一个包装器来完成该操作
    consumer.send(None)
    while n > 0:
        consumer.send(n)
        n -= 1
    # 发送 None 会终止循环，导致协程结束，返回结果
    consumer.send(None)


def coroutine(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        gen = fn(*args, **kwargs)
        next(gen)
        return gen
    return wrapper


# 协程 - 数据消费者
def countdown_con():
    while True:
        n = yield
        if n:
            print(f'countdown {n}')
            sleep(1)
        else:
            print('countdown over')


def main():
    countdown_gen(5, countdown_con())


if __name__ == '__main__':
    main()
    # pass


"""
生产者 消费者 说明协程
"""


def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        sleep(1)
        r = '200 OK'


def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        sleep(1)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
        sleep(1)
    c.close()


# 创建生成器c，作为参数传入produce函数运行
c = consumer()
produce(c)

"""
代码分析：
def consumer():                                    #1
    r = ''                                         #2
    while True:                                    #3
        n = yield r                                #4
        if not n:                                  #5
            return                                 #6
        print('[CONSUMER] Consuming %s...' % n)    #7
        r = '200 OK'                               #8
                                                   #9
                                                   #10
def produce(c):                                    #11
    c.send(None)                                   #12
    n = 0                                          #13
    while n < 5:                                   #14
        n = n + 1                                  #15
        print('[PRODUCER] Producing %s...' % n)    #16
        r = c.send(n)                              #17
        print('[PRODUCER] Consumer return: %s' % r)#18
    c.close()                                      #19
                                           

c = consumer()                                     #22
produce(c)                                         #23
执行结果：

[PRODUCER] Producing 1...
[CONSUMER] Consuming 1...
[PRODUCER] Consumer return: 200 OK
[PRODUCER] Producing 2...
[CONSUMER] Consuming 2...
[PRODUCER] Consumer return: 200 OK
[PRODUCER] Producing 3...
[CONSUMER] Consuming 3...
[PRODUCER] Consumer return: 200 OK
[PRODUCER] Producing 4...
[CONSUMER] Consuming 4...
[PRODUCER] Consumer return: 200 OK
[PRODUCER] Producing 5...
[CONSUMER] Consuming 5...
[PRODUCER] Consumer return: 200 OK
理解代码：

line 22-23：创建生成器c，作为参数传入produce函数运行
line 12：c.send(None) 调用yield，向生成器c内发送数据，也就是参数None
line 4-6：跳转到consumer函数；yield得到发送来的值None 赋值给n，n为None；返回r =' ' 给调用者“c.send(None)” ；中断此次consumer函数；
line 13 - 17：跳转到produce函数； n = 1；打印“Producing 1...” ；r = c.send(n) 发送n = 1 给生成器c；
“注意 send和next不同之处在于：send函数带有一个参数，这个参数会覆盖consumer里上一个yield语句收到的n的值 就是第四行n这里不再是None而是1”

跳转到consumer函数，从第五行开始执行，此时n = 1，经过第五行if判断，打印“Consuming 1...”； r = '200 OK'；回到循环体开头，执行第四行
yield语句，返回r = '200 OK' n= yield r n值没有改变 仍然是1；中断此次consumer函数；第17行r值接收返回值变为'200 OK'；
line 18：跳转到produce函数；打印 Consumer return: 200 OK 回到循环体头部
line 15 - 17： n = 2，打印 Producing 2... 执行r = c.send(n) 发送n = 2 到生成器c
line 5：跳转到consumer函数，从上一个yield的下一条代码执行，n值被line 17 send函数发送改写成2；打印 Consuming 2...； r = '200 OK'；
回到循环体开头，执行第四行yield语句，返回r值给line 17的send函数，line 4的 n值不变，仍然是2；中断此次consumer函数
line 17：跳转到produce函数；打印 Consumer return: 200 OK；
重复上述循环······
至于在web编程中利用 gevent 配合 wsgi 服务器如 gunicorn 提高并发性能，可以通过 gevent 库配置。
"""
