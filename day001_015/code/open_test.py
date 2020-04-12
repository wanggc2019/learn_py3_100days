#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
文件和异常

读写文件
"""
import json


# 读取文本文件
def main():
    """
    如果不愿意在finally代码块中关闭文件对象释放资源，也可以使用上下文语法，通过with关键字指定文件对象的上下文环境并在离开上下文环境时自动
    释放文件资源
    """
    # f = None
    try:
        with open("E://test.txt") as f:
            print(f.read())
        # f = open("E://test.txt", "r", encoding="utf-8")
        # print(f.read())
    except FileNotFoundError:
        print("无法打开指定的文件.")
    except LookupError:
        print("指定了未知的编码.")
    except UnicodeDecodeError:
        print("读取文件时解码错误.")
    # finally:
    #     if f:
    #         f.close()


"""
for-in循环逐行读取或者用readlines方法将文件按行读取到一个列表容器中
"""


def main2():
    # 一次性读取整个文件内容
    with open("E://test.txt") as f:
        print(f.read())

    # 通过for-in循环逐行读取
    with open("E://test.txt") as f:
        for line in f:
            print(line, end='')
    print()

    # 读取文件按行读取到列表中
    with open("E://test.txt") as f:
        lines = f.readlines()
    print(lines)


"""
将文本信息写入文本文件
如果要写入的文件不存在会自动创建文件而不是引发异常
"""


def main3():
    try:
        # f = open("E://test4.txt", "w", encoding="utf-8")
        # with open("E://test4.txt", "w", encoding="utf-8") as f1:
        with open("E://test4.txt", "a", encoding="utf-8") as f:
            # 将1-100的数字写入test4.txt
            # 追加内容将w改为a
            for num in range(1, 11):
                f.write(str(num) + '|')
    except IOError as ex:
        print(ex)
        print("写入文件错误.")
    # finally:
    #     f.close()
    print("完成.")


"""
读写二进制文件
"""


# 复制图片
def main4():
    try:
        with open("E://1583426325938.jpg", "rb") as f1:
            data = f1.read()
        with open("E://复制.jpg", "wb") as f2:
            f2.write(data)
    except FileNotFoundError as ex1:
        print(ex1)
    except IOError as ex2:
        print(ex2)
    print("完成.")


"""
读写json文件
把一个列表或者一个字典中的数据保存到文件中又该怎么做呢？答案是将数据以JSON格式进行保存
"""


def main5():
    """
    {
    "name": "骆昊",
    "age": 38,
    "qq": 957658,
    "friends": ["王大锤", "白元芳"],
    "cars": [
        {"brand": "BYD", "max_speed": 180},
        {"brand": "Audi", "max_speed": 280},
        {"brand": "Benz", "max_speed": 320}
    ]
    }
    :return:
    """
    mydict = {
        "name": "骆昊",
        "age": 38,
        "qq": 957658,
        "friends": ["王大锤", "白元芳"],
        "cars": [
            {"brand": "BYD", "max_speed": 180},
            {"brand": "Audi", "max_speed": 280},
            {"brand": "Benz", "max_speed": 320}
            ]
        }
    try:
        with open("E://data.json", "w", encoding="utf-8") as f:
            json.dump(mydict, f)
    except IOError as e:
        print(e)
    print("完成.")


if __name__ == '__main__':
    # main()
    # main2()
    # main3()
    # main4()
    main5()

"""
readlines():
['Collaborate on best practices, ask questions, find solutions, and maximize your Cloudera machine learning, 
analytics or cloud implementations.\n', 'Browse our technical and reference documentation for Cloudera Enterprise 
development, installation, security, migration, and more.\n', 'Browse our collection of Knowledge Articles to 
troubleshoot common and not so common issues in Cloudera Enterprise products.\n', '28736.83\n', '73487.37\n', '123']

json模块主要有四个比较重要的函数，分别是：

dump - 将Python对象按照JSON格式序列化到文件中
dumps - 将Python对象处理成JSON格式的字符串
load - 将文件中的JSON数据反序列化成对象
loads - 将字符串的内容反序列化成Python对象
"""