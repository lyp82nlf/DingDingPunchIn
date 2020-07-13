import random
import subprocess
import schedule
import time

from ROOT_DIR import ROOT_DIR, CAL_POINT_ARRAY

if __name__ == '__main__':
    devList = CAL_POINT_ARRAY
    devices = subprocess.Popen("adb devices", shell=True, stdout=subprocess.PIPE)
    devices.wait()
    devices = str(devices.stdout.read(), encoding="utf-8")
    for dev in devList:
        print(ROOT_DIR + dev + "_offWork.sh " + dev)
        if dev in devices:
            print(subprocess.call(ROOT_DIR + dev + "_offWork.sh " + dev,
                                  shell=True))
            time.sleep(5)
        else:
            print(dev + " offline")
