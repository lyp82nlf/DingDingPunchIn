import random
import subprocess
import schedule
import time

from ROOT_DIR import ROOT_DIR

if __name__ == '__main__':
    devList = ['2b59a736', '5121a46c', '7a30cc17']
    devices = subprocess.Popen("adb devices", shell=True, stdout=subprocess.PIPE)
    devices.wait()
    devices = str(devices.stdout.read(), encoding="utf-8")
    for dev in devList:
        print(ROOT_DIR + dev + "_Go2Work.sh " + dev)
        if dev in devices:
            print(subprocess.call(ROOT_DIR + dev + "_Go2Work.sh " + dev,
                                  shell=True))
            time.sleep(5)
        else:
            print(dev + " offline")
