#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
面向对象编程 进阶

静态方法和类方法
静态方法和类方法都是通过给类发消息来调用的
"""

from time import sleep, time, localtime

"""
类方法
和静态方法比较类似，Python还可以在类中定义类方法，类方法的第一个参数约定名为cls，它代表的是当前类相关的信息的对象
（类本身也是一个对象，有的地方也称之为类的元数据对象），通过这个参数我们可以获取和类相关的信息并且可以创建出类的对象，
"""

# time.localtime([ sec ])
# 格式化时间戳为本地的时间,如果sec参数未输入，则以当前时间为转换标准
# sec -- 转换为time.struct_time类型的对象的秒数。

# time()
# 1586622469.346753
# localtime()
# time.struct_time(tm_year=2020, tm_mon=4, tm_mday=12, tm_hour=0, tm_min=28, tm_sec=10, tm_wday=6, tm_yday=103, tm_isdst=0)


class Clock(object):
    # 初始化
    def __init__(self, hour=0, minute=0, second=0):
        self._hour = hour
        self._minute = minute
        self._second = second

    # 定义类方法
    @classmethod
    def now(cls):
        ctime = localtime(time())
        return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)

    def run(self):
        self._second = self._second + 1
        if self._second == 60:
            self._second = 0
            self._minute = self._minute + 1
            if self._minute == 60:
                self._minute = 0
                self._hour = self._hour + 1
                if self._hour == 60:
                    self._hour = 0

    def show(self):
        print("%02d:%02d:%02d" % (self._hour, self._minute, self._second))


def main():
    # clock = Clock(23, 59, 55)
    # 通过类方法创建对象并获取系统时间
    clock = Clock.now()
    while True:
        print(clock.show())
        sleep(1)
        clock.run()


if __name__ == '__main__':
    main()
