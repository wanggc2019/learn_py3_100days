#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
进程和线程

多线程
"""
from time import time
from multiprocessing import Process, Queue

"""
使用多进程对复杂任务进行“分而治之”。
1~100000000求和的计算密集型任务
"""


def main():
    start = time()
    total = 0
    num_list = [x for x in range(1, 100000001)]
    for num in num_list:
        total = total + num
    end = time()
    print("total = %d,spend_time = %ds" % (total, end - start))


"""
在上面的代码中，我故意先去创建了一个列表容器然后填入了100000000个数，这一步其实是比较耗时间的，所以为了公平起见，
当我们将这个任务分解到8个进程中去执行的时候，我们暂时也不考虑列表切片操作花费的时间，只是把做运算和合并运算结果的时间统计出来，代码如下所示。
"""


def task_handler(curr_list, result_queue):
    total = 0
    for number in curr_list:
        total += number
    result_queue.put(total)


def main2():
    processes = []
    number_list = [x for x in range(1, 100000001)]
    result_queue = Queue()
    index = 0
    # 启动8个进程将数据切片后进行运算
    for _ in range(8):
        p = Process(target=task_handler, args=(number_list[index:index + 12500000], result_queue))
        index += 12500000
        processes.append(p)
        p.start()
    # 开始记录所有进程执行完成花费的时间
    start = time()
    for p in processes:
        p.join()
    # 合并执行结果
    total = 0
    while not result_queue.empty():
        total += result_queue.get()
    print(total)
    end = time()
    print('Execution time: ', (end - start), 's', sep='')


if __name__ == '__main__':
    # main()
    main2()


