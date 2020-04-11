#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
数据结构练习
list、set、tuple、dict
"""

from random import randrange, randint, sample

'''
练习 双色球选号
游戏规则:
从33个红球（01-33）中选至少6个，再从16个篮球（01-16）中选至少1个。 
自选或机选 每注6+1（红球+篮球）2元  
也可复式投注（如7+1、9+4、12+16等等）
'''

# sample(序列a，n)
# 功能：从序列a中随机抽取n个元素，并将n个元素生以list形式返回。

# random.randint(n,m)
# 产生 n 到 m 的一个整数型随机数


# 选择号码
def random_select():
    # 生成1-33的列表，红球
    # red_balls = [1, 2, 3, 4,...,33]
    red_balls = [x for x in range(1, 34)]
    # 在33个红球中随机选6个
    selected_balls = sample(red_balls, 6)
    # 红球数字排序
    selected_balls.sort()
    # 在16个蓝球中随机选一个
    selected_balls.append(randint(1, 16))
    # print(selected_balls)
    return selected_balls


# 展示号码
def display_selected(balls):
    for index, ball in enumerate(balls):
        if index == len(balls) - 1:
            print('|', end=' ')
        print('%02d' % ball, end=' ')
    print()


# 机选
def main():
    # random_select()
    n = int(input('机选几注： '))
    for _ in range(n):
        display_selected(random_select())


if __name__ == '__main__':
    main()

"""
机选几注： 3
08 14 16 22 30 32 | 12 
13 14 27 29 30 31 | 03 
02 03 20 26 30 33 | 04 
"""

