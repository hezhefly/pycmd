"""
@Time    : 2019/10/30 9:58 上午
@Author  : Haibei
@Site: http://www.haibei.online
@Software: PyCharm
@File: cmd.py
"""
import subprocess


class CommandException(Exception):
    pass


def run_cmd(command):
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    while p.poll() is None:
        line = p.stdout.readline()
        line = line.decode('ascii').strip()
        if line:
            print(line)
    if p.returncode != 0:
        raise CommandException("命令执行有误")
