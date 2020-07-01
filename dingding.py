import random
import subprocess

import schedule
import time


# GEOJKZFEA6YHVCGI  邱凌

def offWorkJob():
    sleepTime = random.randint(0, 5)
    print("sleepTime:" + str(sleepTime))
    time.sleep(sleepTime)
    devList = ['2b59a736', '5121a46c', 'GEOJKZFEA6YHVCGI']
    devices = subprocess.Popen("adb devices", shell=True, stdout=subprocess.PIPE)
    devices.wait()
    devices = str(devices.stdout.read(), encoding="utf-8")
    for dev in devList:
        print("/Users/bjhl/Documents/PyCharmProjects/dingding/" + dev + "_offWork.sh " + dev)
        if dev in devices:
            print(subprocess.call("/Users/mac/Documents/PycharmPro/dingding/" + dev + "_offWork.sh " + dev,
                                  shell=True))
            time.sleep(5)
        else:
            print(dev + " offline")


def go2WorkJob():
    sleepTime = random.randint(0, 100)
    print("sleepTime:" + str(sleepTime))
    time.sleep(sleepTime)
    devList = ['2b59a736', '5121a46c', 'GEOJKZFEA6YHVCGI']
    devices = subprocess.Popen("adb devices", shell=True, stdout=subprocess.PIPE)
    devices.wait()
    devices = str(devices.stdout.read(), encoding="utf-8")
    print("devices:"+devices)
    for dev in devList:
        print("/Users/bjhl/Documents/PyCharmProjects/dingding/" + dev + "_Go2Work.sh " + dev)
        if dev in devices:
            print(subprocess.call("/Users/mac/Documents/PycharmPro/dingding/" + dev + "_Go2Work.sh " + dev,
                                  shell=True))
            time.sleep(5)
        else:
            print(dev + " offline")


schedule.every().day.at("22:28").do(offWorkJob)
schedule.every().day.at("08:48").do(go2WorkJob)

#
while True:
    schedule.run_pending()
    print("wait 1s  current time:"+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    time.sleep(1)
