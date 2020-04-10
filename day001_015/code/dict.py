#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import time


# 创建字典的字面量语法
scores = {'骆昊': 95, '白元芳': 78, '狄仁杰': 82}
print(scores)

# 对字典中所有键值对进行遍历
for key in scores:
    print('{0}:{1}'.format(key, scores[key]))


"""
在屏幕上显示跑马灯文字
"""


def main():
    content = '北京欢迎你为你开天辟地…………'
    while True:
        # 清理屏幕上的输出
        os.system('cls')  # os.system('clear')
        print(content)
        # 休眠200毫秒
        time.sleep(2)
        content = content[1:] + content[0]


if __name__ == '__main__':
    main()


