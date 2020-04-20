#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
--解析动态内容

网站其内容或部分内容是通过JavaScript动态生成的，这就意味着在浏览器窗口中“查看网页源代码”时无法在HTML代码中找到这些内容，也就是说我们之前用
的抓取数据的方式无法正常运转了。解决这样的问题基本上有两种方案，一是JavaScript逆向工程；另一种是渲染JavaScript获得渲染后的内容。
1、JavaScript逆向工程
找到通过Ajax技术动态获取数据的接口

2、使用Selenium
尽管很多网站对自己的网络API接口进行了保护，增加了获取数据的难度，但是只要经过足够的努力，绝大多数还是可以被逆向工程的，但是在实际开发中，我
们可以通过浏览器渲染引擎来避免这些繁琐的工作，WebKit就是一个利用的渲染引擎。
"""

import requests

from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

'''
运行下面的程序，是没有任务输出的，因为页面的HTML代码上根本找不到<img>标签
'''


def main():
    resp = requests.get('https://v.taobao.com/v/content/live?catetype=704&from=taonvlang')
    soup = BeautifulSoup(resp.text, 'lxml')
    for img_tag in soup.select('img[src]'):
        print(img_tag.attrs['src'])


'''
使用Selenium来获取到页面上的动态内容，再提取主播图片
执行报错：selenium.common.exceptions.WebDriverException: Message: 'chromedriver' executable needs to be in PATH. Please 
see https://sites.google.com/a/chromium.org/chromedriver/home
解决：https://blog.csdn.net/weixin_43746433/article/details/95237254
1）下载对应chorm版本的驱动http://chromedriver.storage.googleapis.com/index.html?path=79.0.3945.36/
2）解压后将驱动chromedriver.exe放到selenium包目录下E:\PyProject\learn_py3_100days\venv\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe
查看chorm版本 chrome://version/
3）程序添加该驱动的路径
chrome_driver = r'E:\PyProject\learn_py3_100days\venv\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver)

实践：https://blog.csdn.net/One_of_them/article/details/82560880
'''


def main2():
    chrome_opt = Options()  # 创建参数设置对象.
    chrome_opt.add_argument('--headless')  # 无界面化.
    chrome_opt.add_argument('--disable-gpu')  # 配合上面的无界面化.
    driver_path = r'E:\PyProject\learn_py3_100days\venv\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe'
    # 创建Chrome对象.
    driver = webdriver.Chrome(executable_path=driver_path, options=chrome_opt)
    # get方式访问
    driver.get('https://v.taobao.com/v/content/live?catetype=704&from=taonvlang')
    soup = BeautifulSoup(driver.page_source, 'lxml')
    for img_tag in soup.select('img[src]'):
        # 打印加载的page code
        print(img_tag.attrs['src'])
    # 使用完, 记得关闭浏览器, 不然chromedriver.exe进程为一直在内存中.
    driver.quit()


if __name__ == '__main__':
    # main()
    main2()

