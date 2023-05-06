import time
import urllib.parse

import requests
from lxml import etree

from app.plugins.base import BaseSite


class Biquge(BaseSite):
    r"""笔趣阁

    """

    def __init__(self):
        super().__init__()
        self.site = "https://m.xbiquge.tw"
        self.sitename = "笔趣阁"
        self.safetime = 30
        self.lasttime = time.time()

    def search(self, keyword: str):
        baseurl = "https://m.xbiquge.tw/modules/article/search.php"
        # url = "https://m.xbiquge.tw/modules/article/search.php?searchtype=articlename&searchkey=%B7%B2%C8%CB
        # &t_btnsearch="
        url = baseurl + '?' + "searchtype=articlename&" + "searchkey={}&".format(
            urllib.parse.quote(keyword, encoding='gbk')) + "t_btnsearch="
        # 避免频繁访问
        if (time.time() - self.lasttime) < self.safetime:
            time.sleep(self.safetime)
        resp = requests.get(url)
        tree = etree.HTML(resp.content.decode("gbk"))
        titles = tree.xpath(
            '//table[@class="list-item"]/tr/td[2]/div[@class="article"]/a[1]/text()')
        authors = tree.xpath(
            '//table[@class="list-item"]/tr/td[2]/div[@class="article"]/p[1]/span[1]/text()')
        urls = tree.xpath(
            '//table[@class="list-item"]/tr/td[2]/div[@class="article"]/a[1]/@href')
        for title, url, author in zip(titles, urls, authors):
            print(title, author[3:], url)

    def parser(self):
        pass

    def detail(self, bid):
        pass

    def content(self):
        pass
