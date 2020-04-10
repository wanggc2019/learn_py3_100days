#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
求1到100得和

"""
s = 0
# 0 1 2 ... 99 100
for i in range(101):
    s = s + i
print('1-100间的数之和是:%d' % s)

# 0 - 99 下面得2个等价,前开后闭区间
print(range(100))
print(range(0, 100))

# 1 - 100，步长为2 即 1 3 5 ...99
print(range(1, 100, 2))

# 100 98 ... 2 从100到1范围 以步长2递减
print(range(100, 1, -2))

"""
求1-100得偶数和
"""
s = 0
# 0 1 2 ... 99 100
for i in range(2, 101, 2):
    s = s + i
print('1-100间的偶数之和是：%d' % s)
