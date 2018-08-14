# !/usr/bin/env python
# !-*-coding:utf-8 -*-
# !@Time   : 2018/5/28 12:24
# !@Author : xuqh
# !@Email  : xqhjay@foxmail.com
# !@File   : run.py
from proxypool.scheduler import Scheduler
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def main():
    try:
        s = Scheduler()
        s.run()
    except:
        main()


if __name__ == '__main__':
    main()
