import random
import subprocess

import schedule
import time

from autoUi_go2Work import go2Work
from autoUi_offWork import offWork
# 自动找点 不需要算点 钉钉丧心病狂的话 是有可能被检测到的 原理是辅助功能
if __name__ == '__main__':

    schedule.every().day.at("21:01").do(go2Work)
    schedule.every().day.at("08:50").do(offWork)

    while True:
        schedule.run_pending()
        print("wait 1s  current time:" + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        time.sleep(1)
