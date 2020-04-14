#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
数据结构和算法
算法：解决问题的方法和步骤
常用算法：
穷举法 - 又称为暴力破解法，对所有的可能性进行验证，直到找到正确答案。
例子：百鸡百钱
贪婪法 - 在对问题求解时，总是做出在当前看来，最好的选择，不追求最优解，快速找到满意解。
分治法 - 把一个复杂的问题分成两个或更多的相同或相似的子问题，再把子问题分成更小的子问题，直到可以直接求解的程度，最后将子问题的解进行合并得到原问题的解。
回溯法 - 回溯法又称为试探法，按选优条件向前搜索，当搜索到某一步发现原先选择并不优或达不到目标时，就退回一步重新选择。
动态规划 - 基本思想也是将待求解问题分解成若干个子问题，先求解并保存这些子问题的解，避免产生大量的重复运算
"""
from functools import wraps
from time import time

"""
贪婪法
假设小偷有一个背包，最多能装20公斤赃物，他闯入一户人家，发现如下表所示的物品。很显然，他不能把所有物品都装进背包，所以必须确定拿走哪些物品，留下哪些物品。
"""


class Thing(object):
    """物品"""

    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    @property
    def value(self):
        """价格重量比"""
        return self.price / self.weight


def input_thing():
    """输入物品信息"""
    name_str, price_str, weight_str = input().split()
    return name_str, int(price_str), int(weight_str)


def main():
    """主函数"""
    max_weight, num_of_things = map(int, input().split())
    all_things = []
    for _ in range(num_of_things):
        all_things.append(Thing(*input_thing()))
    all_things.sort(key=lambda x: x.value, reverse=True)
    total_weight = 0
    total_price = 0
    for thing in all_things:
        if total_weight + thing.weight <= max_weight:
            print(f'小偷拿走了{thing.name}')
            total_weight += thing.weight
            total_price += thing.price
    print(f'总价值: {total_price}美元')


"""
分治法例子：快速排序 

选择枢轴对元素进行划分，左边都比枢轴小右边都比枢轴大
快速排序算法思想：
https://wiki.jikexueyuan.com/project/easy-learn-algorithm/fast-sort.html
i=0 j=len(list)-1 ,i = 0 位置得数作为基准数
j先走，j得方向是从右往左（即从序列最后往前移动）
i后走，i得方向是从左往右（即从序列从前往后移动）
i找大于基准得数，找到停下，j找小于基准数，找到停下，然后交换各自位置得值，只要i和j未相遇则继续这个交换过程
直到i和j相遇，第一轮探测结束，此时在基准数左边是全部比他小得数，右边是全部比他大得数，然后以基准数为点拆分序列为2个序列
拆分得序列继续上面得过程

"""


def quick_sort(items, comp=lambda x, y: x <= y):
    items = list(items)[:]
    _quick_sort(items, 0, len(items) - 1, comp)
    for elem in items:
        print(elem, end=' ')
    return items


def _quick_sort(items, start, end, comp):
    if start < end:
        pos = _partition(items, start, end, comp)
        _quick_sort(items, start, pos - 1, comp)
        _quick_sort(items, pos + 1, end, comp)


def _partition(items, start, end, comp):
    pivot = items[end]
    i = start - 1
    for j in range(start, end):
        if comp(items[j], pivot):
            i += 1
            items[i], items[j] = items[j], items[i]
    items[i + 1], items[end] = items[end], items[i + 1]
    return i + 1


"""
装饰器
 ＠staticmethod、＠classmethod 和 @property等等 这是python内置得
 也可自定义装饰器函数
"""


# 输出函数执行时间的装饰器。
def record_time(func):
    """自定义装饰函数的装饰器"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        print('func.__name__%ds' % (time() - start))
        return result
    return wrapper


if __name__ == '__main__':
    # main()
    # need_sort = [4, 2, 5, 7, 1, 3, 9, 8]
    # quick_sort(need_sort)
    record_time


# 高阶函数
items1 = list(map(lambda x: x ** 2, filter(lambda x: x % 2, range(1, 10))))
print(items1)
items2 = [x ** 2 for x in range(1, 10) if x % 2]
print(items2)




