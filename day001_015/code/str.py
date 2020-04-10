#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
字符串
str = ''
单引号或者双引号包围起来的0个或多个字符串
反斜杠转义，或者r
+ 拼接；* 重复；
in，not in 成员运算（是否包含）；
[],[;] 切片运算（取出角标对应一个或多个元素）
"""

s1 = 'hello ' * 3
print(s1)  # hello hello hello
s2 = 'world'
s1 += s2
print(s1)  # hello hello hello world
print('ll' in s1)  # True
print('good' in s1)  # False
str2 = 'abc123456'
# 从字符串中取出指定位置的字符(下标运算)
print(str2[2])  # c
# 字符串切片(从指定的开始索引到指定的结束索引)
print(str2[2:5])  # c12
print(str2[2:])  # c123456
print(str2[2::2])  # c246
print(str2[::2])  # ac246
print(str2[::-1])  # 654321cba
print(str2[-3:-1])  # 45


str1 = 'hello,world!'
# 长度
print(len(str1))  # 12
# 字符串首字母大写
print(str1.capitalize())  # Hello,world!
# 获得字符串每个单词首字母大写的拷贝
print(str1.title())  # Hello,World!
# 获得字符串变大写后的拷贝
print (str1.upper())  # HELLO,WORLD!
# 从字符串中查找子串的位置，空格也算
print (str1.find('or'))  # 7
print (str1.index('or'))   # 7

# 检查字符串是以指定的字符开头
print (str1.startswith('he'))   # True
# 检查字符串是否以指定的字符串结尾
print (str1.endswith('ld!'))   # True
# 将字符串以指定的宽度居中并在两侧填充指定的字符
# *******************hello,world!*******************
print(str1.center(50, '*'))
# 将字符串以指定的宽度靠右放置左侧填充指定的字符
#                                       hello,world!
print (str1.rjust(50, ' '))

str2 = 'abc123456'
# 检查字符串是否由数字构成
print (str2.isdigit())  # False
# 检查字符串是否由字母构成
print (str2.isalpha())  # False
# 检查字符串是否以数字和字母构成
print (str2.isalnum())  # True

str3 = '  jackfrued@126.com '
# 获得字符串修剪左右两侧空格之后的拷贝
print(str3.strip())   # jackfrued@126.com

"""
格式化字符串
"""
# 用%格式化
a = 5
b = '个人'
print('%d %s' % (a, b))   # 5 个人
# 用format格式化
print('{0} {1}'.format(a, b))   # 5 个人




