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


class YouDict(object):
    """优词获取词根"""

    def __init__(self, word):
        self.word = word
        self.url = "https://www.youdict.com/root/search"
        self.tree = self.analysis(word)
        self.run()

    def analysis(self, word):
        while True:
            try:
                content = requests.get(self.url, params={"wd": word}).text
                break
            except:
                print("请求失败！")
        tree = etree.HTML(content, parser=etree.HTMLParser(encoding='utf-8'))
        return tree

    @staticmethod
    def reg(line):
        obj = re.match(r"(.*)[(（](.*)[）)]", line.strip())
        return obj.group(1), obj.group(2)

    def get_words(self):
        """获取词表"""
        pos = "//div[@class='content']/h2[3]/following-sibling::p[following::h2[2]]"
        xpath = f'{pos}/a/text()|{pos}/text()'
        nodes = self.tree.xpath(xpath)
        ch, remark = zip(*map(self.reg, nodes[1::2]))
        res = zip(nodes[0::2], ch, remark)
        return "".join(("## {0}：{1}\n{2}\n".format(*i) for i in res))

    def get_head(self):
        """获取标题"""
        xpath = "//*[@id='article']/h2[3]"
        nodes = self.tree.xpath(xpath)[0]
        return "# " + "".join(map(lambda x: x.replace(" ", ""), nodes.itertext())) + "\n"

    def run(self):
        head = self.get_head()
        words = self.get_words()
        with open(f"{self.word}.md", "w", encoding="utf-8") as f:
            f.write(head + words)
        print(f"{self.word}.md 保存成功！")


def you(word):
    YouDict(word)


def youdict():
    fire.Fire(you)
