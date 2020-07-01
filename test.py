import random
import subprocess
import schedule
import time

if __name__ == '__main__':
    devList = ['2b59a736', '5121a46c', 'GEOJKZFEA6YHVCGI','7a30cc17']
    devices = subprocess.Popen("adb devices", shell=True, stdout=subprocess.PIPE)
    devices.wait()
    devices = str(devices.stdout.read(), encoding="utf-8")
    for dev in devList:
        print("/Users/bjhl/Documents/PyCharmProjects/dingding/" + dev + "_offWork.sh " + dev)
        if dev in devices:
            print(subprocess.call("/Users/bjhl/Documents/PyCharmProjects/dingding/" + dev + "_offWork.sh " + dev, shell=True))
            time.sleep(5)
        else:
            print(dev + " offline")
