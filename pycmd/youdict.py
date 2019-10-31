"""
@Time    : 2019/10/30 11:02 下午
@Author  : Haibei
@Site: http://www.haibei.online
@Software: PyCharm
@File: youdict.py
"""

import re
import fire
import requests
from lxml import etree
from requests.exceptions import SSLError


class YouDict(object):
    """优词获取词根"""

    def __init__(self, word, ind):
        self.word = word
        self.ind = ind
        self.base_xpath = "//div[@id='article']/h2"
        self.url = "https://www.youdict.com/root/search"
        self.tree = self.analysis(word)
        self.h2_num = int(self.tree.xpath(f"count({self.base_xpath})"))
        self.run()

    def analysis(self, word):
        print(f"正在解析{self.url}")
        while True:
            try:
                content = requests.get(self.url, params={"wd": word}).text
                break
            except SSLError:
                print("通讯请求失败！")
        tree = etree.HTML(content, parser=etree.HTMLParser(encoding='utf-8'))
        return tree

    def get_words(self):
        """获取词表"""
        print("正在获取单词...")
        diff = self.h2_num - self.ind
        end = "*" if diff == 0 else f"h2[{diff}]"
        pos = f"{self.base_xpath}[{self.ind}]/following-sibling::p[following::{end}]"
        # pos = "//div[@class='content']/h2[3]/following-sibling::p[following::h2[3]]"
        xpath = f'{pos}/a/text()|{pos}/text()'
        nodes = self.tree.xpath(xpath)
        ch, remark = zip(*self.search(nodes[1::2]))
        res = zip(nodes[0::2], ch, remark)
        return "".join(("## {0}：{1}\n{2}\n".format(*i) for i in res))

    def search(self, nodes):
        for i in nodes:
            ind = self.rfind(i, "（")
            if ind is None:
                ind = self.rfind(i, "(")
                if ind is None:
                    yield i, ""
                    continue
            yield i[:ind], re.sub(r'[()（）]', "", i[ind:], re.M | re.I)

    @staticmethod
    def rfind(string, target):
        if target in string:
            ind = string.rfind(target)
            return ind
        else:
            return None

    def get_head(self):
        """获取标题"""
        print("正在获取标题")
        xpath = f"{self.base_xpath}[{self.ind}]"
        nodes = self.tree.xpath(xpath)[0]
        return "# " + "".join(map(lambda x: x.replace(" ", ""), nodes.itertext())) + "\n"

    def run(self):
        head = self.get_head()
        words = self.get_words()
        with open(f"{self.word}.md", "w", encoding="utf-8") as f:
            f.write(head + words)
        print(f"{self.word}.md 保存成功！")


def you(word, ind):
    YouDict(word, ind)


def youdict():
    fire.Fire(you)

#
# if __name__ == '__main__':
#     YouDict("point", 2)
