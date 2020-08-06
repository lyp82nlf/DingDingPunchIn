import random
import subprocess

import schedule
import time
# GEOJKZFEA6YHVCGI  ql
# QLXBBBA640771867  mk
# 需要手动算点  不会被检查到  不会出问题
from ROOT_DIR import ROOT_DIR, CAL_POINT_ARRAY


def offWorkJob():
    sleepTime = random.randint(0, 100)
    print("sleepTime:" + str(sleepTime))
    time.sleep(sleepTime)
    devList = CAL_POINT_ARRAY
    devices = subprocess.Popen("adb devices", shell=True, stdout=subprocess.PIPE)
    devices.wait()
    devices = str(devices.stdout.read(), encoding="utf-8")
    if "offline" in devices:
        subprocess.Popen("adb kill-server", shell=True, stdout=subprocess.PIPE)
        time.sleep(10)
        subprocess.Popen("adb start-server", shell=True, stdout=subprocess.PIPE)
        time.sleep(10)
    for dev in devList:
        print(ROOT_DIR + dev + "_offWork.sh " + dev)
        if dev in devices:
            print(subprocess.call(ROOT_DIR + dev + "_offWork.sh " + dev,
                                  shell=True))
            time.sleep(5)
        else:
            print(dev + " offline")


def go2WorkJob():
    sleepTime = random.randint(0, 100)
    print("sleepTime:" + str(sleepTime))
    time.sleep(sleepTime)
    devList = CAL_POINT_ARRAY
    devices = subprocess.Popen("adb devices", shell=True, stdout=subprocess.PIPE)
    devices.wait()
    devices = str(devices.stdout.read(), encoding="utf-8")
    print("devices:" + devices)
    if "offline" in devices:
        subprocess.Popen("adb kill-server", shell=True, stdout=subprocess.PIPE)
        time.sleep(10)
        subprocess.Popen("adb start-server", shell=True, stdout=subprocess.PIPE)
        time.sleep(10)
    for dev in devList:
        print(ROOT_DIR + dev + "_Go2Work.sh " + dev)
        if dev in devices:
            print(subprocess.call(ROOT_DIR + dev + "_Go2Work.sh " + dev,
                                  shell=True))
            time.sleep(5)
        else:
            print(dev + " offline")


if __name__ == '__main__':
    #adb devices
    devices = subprocess.Popen("adb devices", shell=True, stdout=subprocess.PIPE)
    devices.wait()
    devices = str(devices.stdout.read(), encoding="utf-8")
    print("devices:" + devices)
    schedule.every().day.at("19:35").do(offWorkJob)
    schedule.every().day.at("08:35").do(go2WorkJob)
    while True:
        schedule.run_pending()
        print("wait 1s  current time:" + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        time.sleep(1)
