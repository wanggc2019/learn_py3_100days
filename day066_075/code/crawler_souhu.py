#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
****网络爬虫****
网络爬虫和相关工具
1、网络爬虫概念
也称网络蜘蛛
是按照一定规则自动浏览万维网并获取信息的机器人程序

应用领域：
搜索引擎、新闻聚合、社交应用、舆情监控、行业数据

2、合法性和背景调研
法律未完善，遵守Robots协议。

3、相关工具
HTTP协议：我们在网页上看到的内容通常是浏览器执行HTML语言得到的结果，而HTTP就是传输HTML数据的协议。HTTP和其他很多应用级协议一样是构建在TCP
（传输控制协议）之上的，它利用了TCP提供的可靠的传输服务实现了Web应用中的数据交换

Chrome Developer Tools：谷歌浏览器内置的开发者工具。
POSTMAN：功能强大的网页调试与RESTful请求工具
HTTPie：命令行HTTP客户端。
==

4、一个简单的爬虫
数据采集(网页下载)->数据分析（网页解析）->数据存储（将需要的信息持久化）

一般来说，爬虫的工作流程包括以下几个步骤：

1.设定抓取目标（种子页面/起始页面）并获取网页。
2.当服务器无法访问时，按照指定的重试次数尝试重新下载页面。
3.在需要的时候设置用户代理或隐藏真实IP，否则可能无法访问页面。
4.对获取的页面进行必要的解码操作然后抓取出需要的信息。
5.在获取的页面中通过某种方式（如正则表达式）抽取出页面中的链接信息。
6.对链接进行进一步的处理（获取页面并重复上面的动作）。
7.将有用的信息进行持久化以备后续的处理。
"""

from urllib.error import URLError
from urllib.request import urlopen

import re
import pymysql
import ssl

from pymysql import Error


# 从“搜狐体育”上获取NBA新闻标题和链接的爬虫
def decode_page(page_bytes, charsets=('utf-8',)):
    """通过指定的字符集对页面进行解码(不是每个网站都将字符集设置为utf-8)"""
    page_html = None
    for charset in charsets:
        try:
            page_html = page_bytes.decode(charset)
            break
        except UnicodeDecodeError:
            pass
            # logging.error('Decode:', error)
    return page_html


def get_page_html(seed_url, *, retry_times=3, charsets=('utf-8',)):
    """获取页面的HTML代码(通过递归实现指定次数的重试操作)"""
    page_html = None
    try:
        page_html = decode_page(urlopen(seed_url).read(), charsets)
    except URLError:
        # logging.error('URL:', error)
        if retry_times > 0:
            return get_page_html(seed_url, retry_times=retry_times - 1, charsets=charsets)
    return page_html


def get_matched_parts(page_html, pattern_str, pattern_ignore_case=re.I):
    """从页面中提取需要的部分(通常是链接也可以通过正则表达式进行指定)"""
    pattern_regex = re.compile(pattern_str, pattern_ignore_case)
    return pattern_regex.findall(page_html) if page_html else []


def start_crawl(seed_url, match_pattern, *, max_depth=-1):
    """开始执行爬虫程序并对指定的数据进行持久化操作"""
    conn = pymysql.connect(host='localhost', port=3306,
                           database='wgc', user='wgc',
                           password='wgc', charset='utf8')
    try:
        with conn.cursor() as cursor:
            url_list = [seed_url]
            # 通过下面的字典避免重复抓取并控制抓取深度
            visited_url_list = {seed_url: 0}
            while url_list:
                # pop弹出列表的第一个元素
                current_url = url_list.pop(0)
                depth = visited_url_list[current_url]
                if depth != max_depth:
                    # 尝试用utf-8/gbk/gb2312三种字符集进行页面解码
                    page_html = get_page_html(current_url, charsets=('utf-8', 'gbk', 'gb2312'))
                    links_list = get_matched_parts(page_html, match_pattern)
                    param_list = []
                    for link in links_list:
                        if link not in visited_url_list:
                            visited_url_list[link] = depth + 1
                            page_html = get_page_html(link, charsets=('utf-8', 'gbk', 'gb2312'))
                            headings = get_matched_parts(page_html, r'<h1>(.*)<span')
                            if headings:
                                param_list.append((headings[0], link))
                    cursor.executemany('insert into tb_result values (default, %s, %s)', param_list)
                    conn.commit()
    except Error:
        pass
        # logging.error('SQL:', error)
    finally:
        conn.close()


def main():
    """主函数"""
    ssl._create_default_https_context = ssl._create_unverified_context
    start_crawl('http://sports.sohu.com/nba_a.shtml',
                r'<a[^>]+test=a\s[^>]*href=["\'](.*?)["\']',
                max_depth=2)


if __name__ == '__main__':
    main()