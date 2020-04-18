#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
****网络爬虫****
并发下载
1、多线程和多进程回顾
threading.local类
concurrent.futures模块
分布式进程

2、协程和异步I/O
生成器 - 数据的生产者。
协程 - 数据的消费者。
"""
import asyncio
import aiohttp


'''
async和await,异步下载网页
aiohttp是第三方库，它实现了HTTP客户端和HTTP服务器的功能，对异步操作提供了非常好的支持
'''


async def download(url):
    print("Fetch: " + url)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print(url, '---->', response.status)
            print(url, '---->', response.cookies)
            print('\n\n', await response.text())


def main():
    loop = asyncio.get_event_loop()
    urls = ['https://www.baidu.com',
            'http://www.sohu.com/',
            'http://www.sina.com.cn/',
            'https://www.taobao.com/',
            'https://www.jd.com/'
    ]

    tasks = [download(url) for url in urls]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()


if __name__ == '__main__':
    main()
