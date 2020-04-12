#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
数据结构
字典 dict = {key:value}
键值对
"""

import os
import time

# 创建字典的字面量语法
scores = {'骆昊': 10, '白元芳': 78, '狄仁杰': 95}
# {'骆昊': 10, '白元芳': 78, '狄仁杰': 95}
print(scores)

"""
查找、更新、删除、遍历
"""
# 1、查找
# 95
print(scores['狄仁杰'])
# 78
print(scores.get('白元芳'))

# 2、更新
scores['骆昊'] = 90
# {'骆昊': 90, '白元芳': 78, '狄仁杰': 95}
print(scores)
# get
# 90
print(scores.get('骆昊'))

# 3、插入
# 可以通过键更新旧有的值，也可以插入新的键值对
scores.update(狄仁杰=99, 武则天=99)
# {'骆昊': 90, '白元芳': 78, '狄仁杰': 99, '武则天': 99}
print(scores)

# 3、遍历
# 骆昊:90
# 白元芳:78
# 狄仁杰:99
# 武则天:99
for key in scores:
    # % 符格式化
    print('%s : %s' % (key, scores[key]))
    # format 格式化
    print('{0} : {1}'.format(key, scores[key]))
    # py3 格式化的新写法
    print(f'{key} : {scores[key]}')

# 4、删除
# ('武则天', 99)
print(scores.popitem())   # 删除最后一个元素
# {'骆昊': 90, '白元芳': 78, '狄仁杰': 99}
print(scores)
print(scores.pop('骆昊'))
# {'白元芳': 78, '狄仁杰': 99}
print(scores)


"""
练习
在屏幕上显示跑马灯文字
"""


def main():
    content = '北京欢迎你为你开天辟地…………'
    while True:
        # 清理屏幕上的输出
        os.system('cls')  # os.system('clear')
        print(content)
        # 休眠500毫秒
        time.sleep(0.5)
        # 1：京欢迎你为你开天辟地…………北
        # 2：欢迎你为你开天辟地…………北京
        content = content[1:] + content[0]


if __name__ == '__main__':
    main()


