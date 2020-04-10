#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
while
猜数字游戏

"""

import random

answer = random.randint(1, 100)
count = 0

while True:
    count = count + 1
    num = int(input('输入猜测数字：'))
    if num < answer:
        print ('往大的猜')
    elif num > answer:
        print ('往小的猜')
    else:
        print ('猜中了')
        break
print('一共猜了%d次' % count)



