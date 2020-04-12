#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
操作符
"""


"""
使用input()函数获取键盘输入(字符串)
使用int()函数将输入的字符串转换成整数
使用print()函数输出带占位符的字符串

Version: 0.1
Author: 骆昊
"""
# a = int(input('a = '))
# b = int(input('b = '))
# print('%d + %d = %d' % (a, b, a + b))
# print('%d - %d = %d' % (a, b, a - b))
# print('%d * %d = %d' % (a, b, a * b))
# print('%d / %d = %f' % (a, b, a / b))
# print('%d // %d = %d' % (a, b, a // b))  # 整除
# print('%d %% %d = %d' % (a, b, a % b))   # 模，因为%便是占位符，所以写成%%
# print('%d ** %d = %d' % (a, b, a ** b))  # **指数a^b

"""
比较运算符和逻辑运算符的使用
Version: 0.1
Author: 骆昊
"""
# flag0 = 1 == 1  # true，比较运算符优先级高于赋值运算符 1==1 为true 将true赋给flag0
# flag1 = 3 > 2   # true
# flag2 = 2 < 1   # false
# flag3 = flag1 and flag2  # flase
# flag4 = flag1 or flag2   # true
# flag5 = not (1 != 2)    # flase
# print('flag0 =', flag0)    # flag0 = True
# print('flag1 =', flag1)    # flag1 = True
# print('flag2 =', flag2)    # flag2 = False
# print('flag3 =', flag3)    # flag3 = False
# print('flag4 =', flag4)    # flag4 = True
# print('flag5 =', flag5)    # flag5 = False


'''
练习1 华氏温度转换为摄氏温度
华氏温度到摄氏温度的转换公式为：$C=(F - 32) \div 1.8$。
'''
f = float(input('输入华氏温度：'))
c = (f - 32) / 1.8
print ('华氏温度%f = 摄氏温度%f' % (f, c))  # 华氏温度89.000000 = 摄氏温度31.666667
print ('华氏温度%.1f = 摄氏温度%.1f' % (f, c))  # 小数点后保留一位

'''
练习2 输入圆得半径，计算圆得周长和面积
周长：L = 2 * pi * r
面积: S = pi * r ^ 2
'''

r = float(input('输入圆得半径：'))
l = 2 * 3.14 * r
s = 3.14 * r ** 2
print ('圆得周长=%.2f\n圆得面积=%.2f' % (l, s))  # 浮点数保留2位小数

'''
练习3 输入年份，判断是否是闰年
普通闰年：被4且不能被100整除
世纪闰年：被400整除
'''
y = int(input('输入年份：'))
leap_year = (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)
print ('{0}是闰年?(true or false):{1}'.format(y, leap_year))

