#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
进程和线程

多线程
"""
from time import sleep
from threading import Thread, Lock

"""
线程通信
多个线程共享一个资源（如变量等），该资源称为“临界资源”，通过“锁”来保护“临界资源”，只有获得“锁”的线程才能访问“临界资源”，而其他没有得到“锁”
的线程只能被阻塞起来，直到获得“锁”的线程释放了“锁”，其他线程才有机会获得“锁”，进而访问被保护的“临界资源”
"""


# 100个线程向同一个银行账户转入1元
class Account(object):
    def __init__(self):
        self._balance = 0
        # 加锁
        self._lock = Lock()

    @property
    def balance(self):
        return self._balance

    def deposit(self, money):
        # 先获取锁，才可执行后面代码
        self._lock.acquire()
        try:
            # 计算存款后的余额
            new_balance = self._balance + money
            # 模拟受理业务需要的时间
            sleep(0.01)
            # 修改账户余额
            self._balance = new_balance
        finally:
            # 在finally中执行释放锁的操作保证正常异常锁都能释放
            self._lock.release()


class AddMoney2Account(Thread):
    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money

    def run(self):
        self._account.deposit(self._money)


def main():
    account = Account()
    threads = []
    # 创建100个存款的线程向同一个账户中存钱
    for _ in range(100):
        t = AddMoney2Account(account, 1)
        threads.append(t)
        t.start()
    # 等所有存款的线程都执行完毕
    for i in threads:
        t.join()
    print('账户余额为: ￥%d元' % account.balance)


if __name__ == '__main__':
    main()


