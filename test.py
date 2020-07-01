import random
import subprocess
import schedule
import time

from dingding import root_dir

if __name__ == '__main__':
    devList = ['2b59a736', '5121a46c', 'GEOJKZFEA6YHVCGI', 'QLXBBBA640771867']
    devices = subprocess.Popen("adb devices", shell=True, stdout=subprocess.PIPE)
    devices.wait()
    devices = str(devices.stdout.read(), encoding="utf-8")
    for dev in devList:
        print(root_dir + dev + "_Go2Work.sh " + dev)
        if dev in devices:
            print(subprocess.call(root_dir + dev + "_Go2Work.sh " + dev,
                                  shell=True))
            time.sleep(5)
        else:
            print(dev + " offline")
