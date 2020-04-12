#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
正则表达式
"""
import re

"""
替换字符串中的不良内容
"""


def hexie():
    sentence = "你丫是傻叉吗? 我操你大爷的. Fuck you."
    purified = re.sub(r'[操肏艹]|fuck|shit|傻[比屄逼叉缺吊屌]|煞笔', r'*', sentence, flags=re.IGNORECASE)
    print(purified)


"""
拆分字符串
"""


def split_str():
    poem = '窗前明月光，疑是地上霜。举头望明月，低头思故乡。'
    sentence_list = re.split(r'[，。,.]', poem)
    while '' in sentence_list:
        sentence_list.remove('')

    print(sentence_list)


if __name__ == '__main__':
    hexie()
    split_str()
