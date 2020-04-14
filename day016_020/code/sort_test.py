#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
数据结构和算法
算法：解决问题的方法和步骤

排序算法（选择、冒泡和归并）
查找算法（顺序和折半）
"""

"""
选择排序

1. 算法步骤
首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置。
再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
重复第二步，直到所有元素均排序完毕。

https://codeplayer.vip/p/j7sbj
"""


def select_sort(items, comp=lambda x, y: x < y):
    items = items[:]
    for i in range(len(items) - 1):
        min_index = i
        for j in range(i+1, len(items)):
            if comp(items[j], items[min_index]):
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]
    # return items
    for elem in items:
        print(elem, end=' ')


"""
冒泡排序
算法描述
比较相邻的元素，如果前一个比后一个大，交换之。
第一趟排序第1个和第2个一对，比较与交换，随后第2个和第3个一对比较交换，这样直到倒数第2个和最后1个，将最大的数移动到最后一位。
第二趟将第二大的数移动至倒数第二位
......
因此需要n-1趟；
"""


def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(0, len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    # return arr
    for elem in arr:
        print(elem, end=' ')


"""
归并排序
归并排序：
    先分开再合并，分开成单个元素，合并的时候按照正确顺序合并
    
    假如我们有一个n个数的数列，下标从0到n-1
　　首先是分开的过程
    1 我们按照 n//2 把这个数列分成两个小的数列
    2 把两个小数列 再按照新长度的一半 把每个小数列都分成两个更小的
    。。。一直这样重复，一直到每一个数分开了
    比如：    6 5 4 3 2 1
        第一次 n=6 n//2=3 分成      6 5 4      3 2 1
        第二次 n=3 n//2=1 分成    6   5 4    3   2 1
        第三次 n=1的部分不分了
                n=2 n//2=1 分成     5   4      2  1
                
    之后是合并排序的过程：
    3 分开之后我们按照最后分开的两个数比较大小形成正确顺序后组合绑定
        刚刚举得例子 最后一行最后分开的数排序后绑定   变成     4 5     1 2
        排序后倒数第二行相当于把最新分开的数排序之后变成    6   4 5       3    12
    4 对每组数据按照上次分开的结果，进行排序后绑定
        6 和 4 5(两个数绑定了)  进行排序
        3 和 1 2(两个数绑定了)  进行排序
        排完后 上述例子第一行待排序的  4 5 6      1 2 3  两组数据
    5 对上次分开的两组进行排序
        拿着 4 5 6     1 2 3两个数组，进行排序，每次拿出每个数列中第一个(最小的数)比较，把较小的数放入结果数组。再进行下一次排序。
        每个数组拿出第一个数，小的那个拿出来放在第一位 1 拿出来了，   变成4 5 6    2 3
        每个数组拿出第一个书比较小的那个放在下一个位置  1 2被拿出来，  待排序 4 5 6      2
        每个数组拿出第一个书比较小的那个放在下一个位置  1 2 3 被拿出来，  待排序 4 5 6
        如果一个数组空了，说明另一个数组一定比排好序的数组最后一个大 追加就可以结果 1 2 3 4 5 6
    相当于我们每次拿到两个有序的列表进行合并，分别从两个列表第一个元素比较，把小的拿出来，在拿新的第一个元素比较，把小的拿出来
        这样一直到两个列表空了 就按顺序合并了两个列表
    
    结束
 
时间复杂度： 最好最坏都是 O( n log n )
稳定性：稳定
缺点：每次拆分数组都要开心的数组， 每次合并数组都要开新数组，空间复杂度很大
"""


def merge(items1, items2, comp=lambda x, y: x < y):
    """合并(将两个有序的列表合并成一个有序的列表)"""
    items = []
    index1, index2 = 0, 0
    # 比较传入的两个子序列，对两个子序列进行排序
    while index1 < len(items1) and index2 < len(items2):
        if comp(items1[index1], items2[index2]):
            items.append(items1[index1])
            index1 += 1
        else:
            items.append(items2[index2])
            index2 += 1
    # 将排好序的子序列合并
    items += items1[index1:]
    items += items2[index2:]
    return items


def merge_sort(items, comp=lambda x, y: x < y):
    # return _merge_sort(list(items), comp)
    lst = _merge_sort(list(items), comp)
    for elem in lst:
        print(elem, end=' ')


def _merge_sort(items, comp):
    """归并排序"""
    # 从递归中返回长度为1的序列
    if len(items) < 2:
        return items
    # 切分序列，整除
    mid = len(items) // 2
    # 递归调用本身，将序列向下切分为都是只有一个元素得序列
    # [4] [2]  [5] [7] [1] [3]
    left = _merge_sort(items[:mid], comp)
    right = _merge_sort(items[mid:], comp)
    # 调用merge对切分得子序列排序
    return merge(left, right, comp)


if __name__ == '__main__':
    need_sort = [4, 2, 5, 7, 1, 3, 9, 8]
    # select_sort(need_sort)
    # bubble_sort(need_sort)
    merge_sort(need_sort)



