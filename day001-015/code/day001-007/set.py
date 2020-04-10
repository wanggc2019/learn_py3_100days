#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
集合 set = {}
不允许有重复元素，而且可以进行交集、并集、差集等运算
"""

"""
添加、更新、删除
"""
# 定义集合
set1 = {1, '张三', 'hello', 20}
# set(['张三', 1, 20, 'hello'])
# 1、添加
print(set1)
set1.add('我是add的')
# set(['张三', 1, 20, 'hello', '我是add的'])
print(set1)
# 更新
set1.update([2, '我是updata的'])
# set([1, 2, '我是updata的', '张三', 20, '我是add的', 'hello'])
print(set1)
# 删除
set1.remove(1)
#  set([2, '我是updata的', '张三', 20, '我是add的', 'hello'])
print(set1)

"""
集合的 交集 并集 差集 成员 运算
"""
set2 = {2, '李四', True, 'hello'}
# 1、交集
# set([2, 'hello'])
print(set1 & set2)
# 2、并集
# set(['张三', '李四', 2, '我是updata的', 20, '我是add的', True, 'hello'])
# print(set1.intersection(set2))
print(set1 | set2)
# 3、差集
# set(['张三', '我是updata的', 20, '我是add的'])
# print(set1.union(set2))
print(set1 - set2)
# 4、成员
# set(['李四', True, '我是updata的', '张三', 20, '我是add的'])
# print(set1.difference(set2))
print(set1 ^ set2)
# print(set1.symmetric_difference(set2))

