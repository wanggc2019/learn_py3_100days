#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
并发编程

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
"""

import asyncio


"""
async 用来声明一个函数为异步函数，异步函数的特点是能在函数执行过程中挂起，去执行其他异步函数，等到挂起条件（假设挂起条件是sleep(5)）消失后
也就是5秒到了再回来执行.
"""


async def fetch(host):
    """从指定的站点抓取信息(协程函数)"""
    print(f'Start fetching {host}\n')
    # 跟服务器建立连接
    '''
    wait 用来用来声明程序挂起，比如异步程序执行到某一步时需要等待的时间很长，就将此挂起，去执行其他的异步程序
    '''
    reader, writer = await asyncio.open_connection(host, 80)
    # 构造请求行和请求头
    writer.write(b'GET / HTTP/1.1\r\n')
    writer.write(f'Host: {host}\r\n'.encode())
    writer.write(b'\r\n')
    # 清空缓存区(发送请求)
    await writer.drain()
    # 接收服务器的响应(读取响应行和响应头)
    line = await reader.readline()
    while line != b'\r\n':
        print(line.decode().rstrip())
        line = await reader.readline()
    print('\n')
    writer.close()


def main():
    """主函数"""
    urls = ('www.sohu.com', 'www.douban.com', 'www.163.com')
    # 获取系统默认的事件循环
    loop = asyncio.get_event_loop()
    # 用生成式语法构造一个包含多个协程对象的列表
    tasks = [fetch(url) for url in urls]
    # 通过asyncio模块的wait函数将协程列表包装成Task（Future子类）并等待其执行完成
    # 通过事件循环的run_until_complete方法运行任务直到Future完成并返回它的结果
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()


if __name__ == '__main__':
    main()
