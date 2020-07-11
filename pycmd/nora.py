"""
@Time    : 2020/7/11 9:27 下午
@Author  : Haibei
@Site: http://www.haibei.online
@Software: PyCharm
@File: nora.py
@Describe: 
"""
import fire
from pathlib2 import Path
from .cmd import run_cmd


class Nora(object):

    def pwd(self, path="."):
        print(Path(path).resolve())
        # mirror = f" -i {self.mirror}"
        # print(f"开始{self.info}：{name}")
        # if name.split(".")[-1] == "git":
        #     name = "git+" + name
        #     mirror = ""
        # return run_cmd(
        #     f"pip install {self.arg}{name}{mirror} --no-cache-dir")


def nora():
    fire.Fire(Nora)
