#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
数据结构
list 列表
list = [] 值的有序序列
可通过索引标识，[],[:] 取出对应的一个或多个元素，可以修改元素
"""

import sys


'''
索引，遍历，添加，移除
'''
list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
# ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
print(list1)

# 1、索引
# 1.1、正数索引
print(list1[0])   # orange
print(list1[:])   # ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
# orange
# apple
# zoo
# internationalization
# blueberry
print(list1[2:5])   # list1是0-4 ，5明显超过了list的角标，但是不会报错
# print list1[5]     # 但是索引某个角标越界时报错：IndexError: list index out of range
# blueberry
# 1.2、负数索引
print(list1[-1])   # 也可以用-index来索引，表示从最后一位元素开始 -1就是最后一位元素，-2就是倒数第二位

# 2、遍历
# 2.1、循环下标遍历元素
# orange
# apple
# zoo
# internationalization
# blueberry
for index in range(len(list1)):
    print(list1[index])
# 2.2、直接循环遍历元素
for elem in list1:
    print(elem)
# 通过enumerate函数处理列表之后再遍历可以同时获得元素索引和值
# (0, 'orange')
# (1, 'apple')
# (2, 'zoo')
# (3, 'internationalization')
# (4, 'blueberry')
for index, elem in enumerate(list1):
    print(index, elem)

# 3、添加
# 3.1、追加
list1.append('我是追加的')
# ['orange', 'apple', 'zoo', 'internationalization', 'blueberry', '我是追加的']
print(list1)
# 3.1、插入
list1.insert(1, '我是插入的')
# ['orange', '我是插入的', 'apple', 'zoo', 'internationalization', 'blueberry', '我是追加的']
print(list1)
# 3.3、extend() 函数用于在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
# 3.3、合并
# 把list2合并到list1
list2 = [1, 2, 3]
list1.extend(list2)
# ['orange', '我是插入的', 'apple', 'zoo', 'internationalization', 'blueberry', '我是追加的', 1, 2, 3]
print(list1)

# 4、删除
# 4.1、pop 按索引删
list1.pop(0)
# ['我是插入的', 'apple', 'zoo', 'internationalization', 'blueberry', '我是追加的', 1, 2, 3]
print(list1)
# 4.2、remove 按值删
list1.remove('zoo')
# ['我是插入的', 'apple', 'internationalization', 'blueberry', '我是追加的', 1, 2, 3]
print(list1)


''''
成员运算
'''
# 4.1、判断元素是否在list
if 3 in list2:
    print('3 in list2')
else:
    print('3 not in list2')
if 'apple' not in list1:
    print('apple not in list1')
else:
    print('apple in list1')


'''
排序
'''
# sorted函数返回列表排序后的拷贝不会修改传入的列表
# 函数的设计就应该像sorted函数一样尽可能不产生副作用
# 排序默认按字母顺序
list2 = sorted(list1)
# ['apple', 'blueberry', 'internationalization', 'orange', 'zoo']
print(list2)
# reverse :True为降序，默认值为False
list3 = sorted(list1, reverse=True)
# ['zoo', 'orange', 'internationalization', 'blueberry', 'apple']
print(list3)
# 通过key关键字参数指定根据字符串长度进行排序而不是默认的字母表顺序
# list4 = sorted(list1, key=len)
# ['zoo', 'apple', 'orange', 'blueberry', 'internationalization']
# print list4
# 给列表对象发出排序消息直接在列表对象上进行排序
list1.sort(reverse=True)
# ['zoo', 'orange', 'internationalization', 'blueberry', 'apple']
print(list1)


"""
生成式和生成器
使用列表的生成式语法来创建列表
"""
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# x 是生成规则 x in range()表示x再范围内取值
f = [x for x in range(1, 10)]
print(f)
# ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'C1', 'C2', 'C3', 'C4', 'C5',
# 'C6', 'C7', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7']
f = [x + y for x in 'ABCDE' for y in '1234567']
print(f)
# 用列表的生成表达式语法创建列表容器
# 用这种语法创建列表之后元素已经准备就绪所以需要耗费较多的内存空间
f = [x ** 2 for x in range(1, 1000)]
print(sys.getsizeof(f))  # 查看对象占用内存的字节数
print(f)
# for val in f:
#     print(val)
