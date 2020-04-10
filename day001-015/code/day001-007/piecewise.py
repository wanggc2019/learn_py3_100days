#!/usr/bin/env python
# -*- coding:utf-8 -*-


"""
练习2 if
分段求值
        | 3x -1 (x < -1)
f(x) =  | x * 2 (-1 <= x < 1)
        | x (x >= 1)
"""


x = float(input('输入x：'))
if x < -1:
    f = 3 * x - 1
elif -1 < x < 1:
    f = x * 2
else:
    f = x
print('x = %.2f, f = %.2f' % (x, f))

"""
练习2 百分制成绩转换为等级
大于90 为A 80-90 为B 70-80为C 60-70 为D 60下为E
"""
score = float(input('请输入成绩: '))
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'E'
print("对应的等级是:%s" % grade)