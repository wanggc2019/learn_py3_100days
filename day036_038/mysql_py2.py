#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
python操作mysql数据库

在Python 3中，我们通常使用纯Python的三方库PyMySQL来访问MySQL数据库，它应该是目前Python操作MySQL数据库最好的选择。

练习：模拟通讯录，添加查找删除更新联系人信息
事先要建好表：
-- 创建联系人表tb_contacter
create table wgc.tb_contacter
(
conid int auto_increment comment '编号',
conname varchar(31) not null comment '姓名',
contel varchar(15) default '' comment '电话',
conemail varchar(255) default'' comment '邮箱',
primary key (conid)
);

关于编码得问题 window下
程序执行时，插入汉字，出现乱码异常：Incorrect string value: '\\xE6\\x9D\\x8E\\xE5\\x9B\\x9B' for column 'conname' at row 1
这是mysql得编码设置问题
1、查看mysql编码
show variables where Variable_name like '%char%';
正确因该是：
character_set_client	utf8
character_set_connection	utf8
character_set_database	utf8
character_set_filesystem	binary
character_set_results	utf8
character_set_server	utf8
character_set_system	utf8
character_sets_dir	C:\Program Files\MySQL\MySQL Server 5.6\share\charsets\

如果不是修改：
配置文件里修改：
C:\Program Files\MySQL\MySQL Server 5.6
my-default.ini
添加：
[client]
default-character-set=utf8
在[mysqld]添加
character-set-server=utf8
重启mysql

如果还是不行，查看库和表得编码
show create database wgc;
show create table wgc.tb_contacter;
若不是utf8,修改：
修改库得编码：
alter database wgc default character set utf8;
重建该表，插入正常。
"""

import pymysql

INSERT_CONTACTER = """
insert into tb_contacter (conname, contel, conemail) values (%s, %s, %s)
"""
DELETE_CONTACTER = """
delete from tb_contacter where conid=%s
"""
UPDATE_CONTACTER = """
update tb_contacter set conname=%s, contel=%s, conemail=%s where conid=%s
"""
SELECT_CONTACTERS = """
select conid as id, conname as name, contel as tel, conemail as email 
from tb_contacter limit %s offset %s
"""
SELECT_CONTACTERS_BY_NAME = """
select conid as id, conname as name, contel as tel, conemail as email 
from tb_contacter where conname like %s
"""
COUNT_CONTACTERS = """
select count(conid) as total from tb_contacter
"""


class Contacter(object):
    def __init__(self, id, name, tel, email):
        self.id = id
        self.name = name
        self.tel = tel
        self.email = email


# 输入联系人信息，返回string类型
def input_contacter_info():
    name = input("姓名：")
    tel = input("手机：")
    email = input("邮箱：")

    return name, tel, email


# 添加联系人信息
def add_contacter(con):
    name, tel, email = input_contacter_info()
    try:
        with con.cursor() as cursor:
            if cursor.execute(INSERT_CONTACTER, (name, tel, email)) == 1:
                print("添加联系人成功.")
    except pymysql.MySQLError as err:
        print(err)
        print("添加联系人失败.")


# 删除联系人信息
def delete_contacter(con, contacter):
    try:
        with con.cursor() as cursor:
            if con.execute(DELETE_CONTACTER, (contacter.id, )) == 1:
                print("联系人已删除.")
    except pymysql.MySQLError as err:
        print(err)
        print("删除联系人失败.")


# 编辑联系人信息，就是更新下信息，修改某些信息
def edit_contacter(con, contacter):
    name, tel, email = input_contacter_info()
    contacter.name = name or contacter.name
    contacter.tel = tel or contacter.tel
    contacter.email = email or contacter.email
    try:
        with con.cursor() as cursor:
            if cursor.execute(UPDATE_CONTACTER, (contacter.name, contacter.tel, contacter.email)) == 1:
                print("编辑联系人成功.")
    except pymysql.MySQLError as err:
        print(err)
        print("编辑联系人失败.")


# 编辑联系人，修改或者删除，调用上面得方法
def show_contacter_detail(con, contacter):
    print('姓名:', contacter.name)
    print('手机号:', contacter.tel)
    print('邮箱:', contacter.email)
    choice = input("是否编辑联系人信息?(yes|no)")
    if choice == 'yes':
        edit_contacter(con, contacter)
    else:
        choice = input("是否删除联系人信息?(yes|no)")
        if choice == 'yes':
            delete_contacter(con, contacter)


def show_search_result(con, cursor):
    contacters_list = []
    for index, row in enumerate(cursor.fetchall()):
        contacter = Contacter(**row)
        contacters_list.append(contacter)
        print('[%d]: %s' % (index, contacter.name))
    if len(contacters_list) > 0:
        choice = input('是否查看联系人详情?(yes|no)')
        if choice.lower() == 'yes':
            index = int(input('请输入编号: '))
            if 0 <= index < cursor.rowcount:
                show_contacter_detail(con, contacters_list[index])


def find_all_contacter(con):
    page, size = 1, 5
    try:
        with con.cursor() as cursor:
            cursor.execute(COUNT_CONTACTERS)
            total = cursor.fetchone()['total']
            while True:
                cursor.execute(SELECT_CONTACTERS, (size, (page - 1) * size))
                show_search_result(con, cursor)
                if page * size < total:
                    choice = input("继续查看下一页?(yes|no)")
                    if choice == 'yes':
                        page += 1
                    else:
                        break
                else:
                    print("没有下一页记录.")
                    break
    except pymysql.MySQLError as err:
        print(err)


def find_contacter_by_name(con):
    name = input("输入联系人姓名：")
    try:
        with con.cursor() as cursor:
            cursor.execute(SELECT_CONTACTERS_BY_NAME, ('%' + name + '%'))
            show_search_result(con, cursor)
    except pymysql.MySQLError as err:
        print(err)


def find_contacter(con):
    while True:
        print('1. 查看所有联系人')
        print('2. 搜索联系人')
        print('3. 退出查找')
        choice = int(input('请输入: '))
        if choice == 1:
            find_all_contacter(con)
        elif choice == 2:
            find_contacter_by_name(con)
        elif choice == 3:
            break


def main():
    con = pymysql.connect(host='localhost', port=3306,
                          user='wgc', passwd='wgc',
                          db='wgc', charset='utf8',
                          autocommit=True,
                          cursorclass=pymysql.cursors.DictCursor)
    while True:
        print('=====通讯录=====')
        print('1. 新建联系人')
        print('2. 查找联系人')
        print('3. 退出系统')
        print('===============')
        choice = int(input('请选择: '))
        if choice == 1:
            add_contacter(con)
        elif choice == 2:
            find_contacter(con)
        elif choice == 3:
            con.close()
            print("再见.")
            break


if __name__ == '__main__':
    main()
