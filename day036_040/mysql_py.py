#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
python操作mysql数据库

在Python 3中，我们通常使用纯Python的三方库PyMySQL来访问MySQL数据库，它应该是目前Python操作MySQL数据库最好的选择。

具体得步骤是
1、创建数据库连接对象
con = pymysql.connect(host='localhost', port=3306,
                          database='wgc', charset='utf8',
                          user='wgc', password='wgc')

2、通过连接对象获取游标
with con.cursor() as cursor:

3. 通过游标执行SQL并获得执行结果
cursor.execute(sql)

4、 操作成功提交事务
con.commit()
进行insert，update，delete的时候是需要commit的，否则不生效。当然这仅针对拥有事务的InnoDB存储引擎，对于MySIAM则是非必须的，但是带上也没有错。

5、关闭连接释放资源
con.close()
"""
import pymysql


# 创建表
def create_table():
    # 1、创建数据库连接对象
    con = pymysql.connect(host='localhost', port=3306,
                          database='wgc', charset='utf8',
                          user='wgc', password='wgc')
    try:
        # 2. 通过连接对象获取游标
        with con.cursor() as cursor:
            # 3. 通过游标执行SQL并获得执行结果
            result = cursor.execute("create table if not exists tb_dept  (dno  int not null comment '编号',"
                                    "dname varchar(10) not null comment '名称',"
                                    "dloc  varchar(20) not null comment '所在地',"
                                    "primary key (dno));")
            print(result)
        # 建表成功，返回0,如果加了if not exists，表存在也会返回0，会抛出告警，如果不加，表存在会直接抛出异常
        if result == 0:
            print("表创建成功.")
        # 4. 操作成功提交事务
        con.commit()
    finally:
        # 5. 关闭连接释放资源
        con.close()


def insert_table():
    no = int(input('编号: '))
    name = input('名字: ')
    loc = input('所在地: ')
    # 1. 创建数据库连接对象
    con = pymysql.connect(host='localhost', port=3306,
                          database='wgc', charset='utf8',
                          user='wgc', password='wgc')
    try:
        # 2. 通过连接对象获取游标
        with con.cursor() as cursor:
            # 3. 通过游标执行SQL并获得执行结果
            result = cursor.execute(
                'insert into tb_dept values (%s, %s, %s)',
                (no, name, loc)
            )
            # print(result)
        # 添加成功返回1
        if result == 1:
            print('添加成功!')
        # 4. 操作成功提交事务
        con.commit()
    finally:
        # 5. 关闭连接释放资源
        con.close()


if __name__ == '__main__':
    # create_table()
    insert_table()



