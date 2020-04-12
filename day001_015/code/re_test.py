#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
正则表达式
"""
import re

"""
练习
验证输入用户名和QQ号是否有效并给出对应的提示信息
要求：用户名必须由字母、数字或下划线构成且长度在6~20个字符之间，QQ号是5~12的数字且首位不能为0
"""

# {M,N}	匹配至少M次至多N次	\w{3,6}
# \d	匹配数字
# []	匹配来自字符集的任意单一字符
# match(pattern, string, flags=0)	用正则表达式匹配字符串 成功返回匹配对象 否则返回None
# $	匹配字符串的结束	.exe$	可以匹配.exe结尾的字符串
# ^	匹配字符串的开始	^The	可以匹配The开头的字符串


def check_qq_number():
    username = input("输入用户名：")
    qq = input("输入qq号：")
    # 用户名的匹配
    m1 = re.match(r'^[0-9a-zA-Z_]{6, 20}$', username)
    if not m1:
        print("请输入有效的用户名.")
    # QQ号的匹配
    m2 = re.match(r'^[1-9]\d{4, 11}$', qq)
    if not m2:
        print("请输入有效的qq号.")
    if m1 and m2:
        print("输入的用户名和qq号正确.")


if __name__ == '__main__':
    check_qq_number()

