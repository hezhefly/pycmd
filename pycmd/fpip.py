"""
@Time    : 2019/10/29 5:01 下午
@Author  : Haibei
@Site: http://www.haibei.online
@Software: PyCharm
@File: fast_pip.py
"""
import fire
from .cmd import run_cmd


class FastPip(object):
    def __init__(self, u=False):
        self.info, self.arg = ("升级", "-U ") if u else ("安装", "")
        self.mirror = "https://mirrors.huaweicloud.com/repository/pypi/simple"

    def install(self, name):
        mirror = f" -i {self.mirror}"
        print(f"开始{self.info}：{name}")
        if name.split(".")[-1] == "git":
            name = "git+" + name
            mirror = ""
        return run_cmd(
            f"pip install {self.arg}{name}{mirror} --no-cache-dir")


def main():
    fire.Fire(FastPip)
