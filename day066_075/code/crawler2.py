#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
****网络爬虫和相关工具****
PyQuery的使用
获取知乎发现上的问题链接
"""

from urllib.parse import urljoin

import re
import requests

from bs4 import BeautifulSoup


def main():
    headers = {'user-agent': 'Baiduspider'}
    proxies = {'http': 'http://122.114.31.177:808'}
    base_url = 'https://www.zhihu.com/'
    # urljoin拼接2个地址https://www.zhihu.com/explore
    seed_url = urljoin(base_url, 'explore')
    # https://www.zhihu.com/explore
    # print(seed_url)
    # 导入requests后，用get方法就可以直接访问url地址,<Response [200]>
    response = requests.get(seed_url, headers=headers, proxies=proxies)
    # print(response)
    # 状态码200只能说明这个接口访问的服务器地址是对的，并不能说明功能OK，一般要查看响应的内容，response.text是返回文本信息
    # BeautifulSoup4和 lxml 一样，是一个html/xml解析器
    # 构建beautifulsoup实例
    # soup = BeautifulSoup(html,'lxml')
    # 第一个参数是要匹配的内容
    # 第二个参数是beautifulsoup要采用的模块，即规则
    soup = BeautifulSoup(response.text, 'lxml')
    # print(soup)
    href_regex = re.compile(r'^/question')
    link_set = set()
    # 返回所有匹配到的结果，区别于find（find只返回查找到的第一个结果）
    # find_all(name, attrs, recursive, text, limit, **kwargs)
    # name查找的标签；attrs：基于attrs参数；
    # <a class="ExploreSpecialCard-contentTitle" data-za-detail-view-id="5794" href="/question/318814504" rel="noopener noreferrer" target="blank">如何修复肌肤屏障?</a>
    for a_tag in soup.find_all('a', {'href': href_regex}):
        # a_tag是所有匹配到正则式的a标签
        # print(a_tag)
        if 'href' in a_tag.attrs:
            href = a_tag.attrs['href']
            # href是所有的a标签的href内容
            # print(href)
            full_url = urljoin(base_url, href)
            link_set.add(full_url)
    print('Total %d question pages found.' % len(link_set))
    # for elem in link_set:
    #     print(elem)


if __name__ == '__main__':
    main()


"""
print(a_tag):
<a class="ExploreSpecialCard-contentTitle" data-za-detail-view-id="5794" href="/question/318814504" rel="noopener noreferrer" target="blank">如何修复肌肤屏障?</a>
<a class="ExploreSpecialCard-contentTitle" data-za-detail-view-id="5794" href="/question/388095682" rel="noopener noreferrer" target="blank">iPhone SE 二代突然上线</a>
<a class="ExploreSpecialCard-contentTitle" data-za-detail-view-id="5794" href="/question/388101050" rel="noopener noreferrer" target="blank">3299 元，苹果也打起了价格战</a>
<a class="ExploreSpecialCard-contentTitle" data-za-detail-view-id="5794" href="/question/375354846" rel="noopener noreferrer" target="blank">回顾历届冠军皮肤</a>
<a class="ExploreSpecialCard-contentTitle" data-za-detail-view-id="5794" href="/question/388257344" rel="noopener noreferrer" target="blank">最新 | 鲍毓明养女否认恋爱关系，称「2015 年就被性侵，被迫看色情视频」</a>
<a class="ExploreSpecialCard-contentTitle" data-za-detail-view-id="5794" href="/question/387410400" rel="noopener noreferrer" target="blank">李星星这 3 年为什么不逃走呢？第一次受伤害之后为什么不向老师和同学求助呢？</a>
<a class="ExploreSpecialCard-contentTitle" data-za-detail-view-id="5794" href="/question/386587388" rel="noopener noreferrer" target="blank">鲍毓明最终会受到什么样的惩罚？会承担刑事责任吗？</a>
<a class="ExploreRoundtableCard-questionTitle" data-za-detail-view-id="5800" href="/question/388305627" rel="noopener noreferrer" target="_blank">在知识产权行业的专业人员眼里，知识产权复合性人才需要具备哪些能力？</a>
<a class="ExploreRoundtableCard-questionTitle" data-za-detail-view-id="5800" href="/question/388291330" rel="noopener noreferrer" target="_blank">为什么对于科技创新型企业，专利堪称在市场竞争中的「核武器」？</a>
<a class="ExploreRoundtableCard-questionTitle" data-za-detail-view-id="5800" href="/question/340028913" rel="noopener noreferrer" target="_blank">关于知识产权工作，都有哪些业内人士才懂的段子？</a>
<a class="ExploreRoundtableCard-questionTitle" data-za-detail-view-id="5800" href="/question/21094483" rel="noopener noreferrer" target="_blank">留学生有哪些不为人知的苦？</a>
<a class="ExploreRoundtableCard-questionTitle" data-za-detail-view-id="5800" href="/question/27313498" rel="noopener noreferrer" target="_blank">如何做一名优秀而得体的留学生？</a>
<a class="ExploreRoundtableCard-questionTitle" data-za-detail-view-id="5800" href="/question/46349433" rel="noopener noreferrer" target="_blank">出国留学会对人的一生有多大的影响？</a>
<a class="ExploreRoundtableCard-questionTitle" data-za-detail-view-id="5800" href="/question/288806462" rel="noopener noreferrer" target="_blank">有哪些写进作文百用不腻的句子？</a>
<a class="ExploreRoundtableCard-questionTitle" data-za-detail-view-id="5800" href="/question/20590852" rel="noopener noreferrer" target="_blank">高中作文如何得到 50 以上的分数？</a>
<a class="ExploreRoundtableCard-questionTitle" data-za-detail-view-id="5800" href="/question/277208261" rel="noopener noreferrer" target="_blank">如何报考一级注册消防工程师？</a>
<a class="ExploreRoundtableCard-questionTitle" data-za-detail-view-id="5800" href="/question/264468321" rel="noopener noreferrer" target="_blank">30 岁前拿到一建、造价、消防工程师是怎样的体验？</a>
<a class="ExploreRoundtableCard-questionTitle" data-za-detail-view-id="5800" href="/question/316105397" rel="noopener noreferrer" target="_blank">趁着年轻要不要多考证呢？</a>

print(href):
/question/318814504
/question/388095682
/question/388101050
/question/375354846
/question/388257344
/question/387410400
/question/386587388
/question/388305627
/question/388291330
/question/340028913
/question/21094483
/question/27313498
/question/46349433
/question/288806462
/question/20590852
/question/277208261
/question/264468321
/question/316105397


link_set:
https://www.zhihu.com/question/277009843
https://www.zhihu.com/question/27313498
https://www.zhihu.com/question/277208261
https://www.zhihu.com/question/316105397
https://www.zhihu.com/question/388305627
https://www.zhihu.com/question/288806462
https://www.zhihu.com/question/387410400
https://www.zhihu.com/question/388095682
https://www.zhihu.com/question/386587388
https://www.zhihu.com/question/60533122
https://www.zhihu.com/question/388257344
https://www.zhihu.com/question/375354846
https://www.zhihu.com/question/388101050
https://www.zhihu.com/question/340028913
https://www.zhihu.com/question/388291330
https://www.zhihu.com/question/264468321
https://www.zhihu.com/question/21094483
https://www.zhihu.com/question/46349433
https://www.zhihu.com/question/318814504
"""