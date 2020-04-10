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


"""
正整数的反转
思路：就是用以上的取位数的方法，对10取模，取到最后位上的数字，然后左移
"""
num = int(input('num = '))
reversed_num = 0
# 只要num大于0 就一直进行下面的循环
while num > 0:
    # 比如1234
    # 第一次循环：个位数字4，0*0 + 4 = 4 ，小数点往左移动一位，123
    # 第二次循环：个位数字3，4*10 + 3=43 ，小数点再往左移动一位，12
    # 第三次循环：个位数字2，43 * 10 + 2 = 432，小数点左移，1
    # 第四次循环：各位数字1，432 * 10 + 1 = 4321，num =0结束循环
    reversed_num = reversed_num * 10 + num % 10
    num = num // 10
print(reversed_num)


