import subprocess

import uiautomator2 as u2
import time

from ROOT_DIR import AUTO_PUNCH_ARRAY


def go2Work():
    devices = AUTO_PUNCH_ARRAY
    currentDevices = subprocess.Popen("adb devices", shell=True, stdout=subprocess.PIPE)
    currentDevices.wait()
    currentDevices = str(currentDevices.stdout.read(), encoding="utf-8")
    for device in devices:
        if device not in currentDevices:
            print(device + " offline")
            continue
        d = u2.connect_usb(device)
        d.implicitly_wait(30)
        d.screen_off()  # turn off the screen
        d.screen_on()  # turn on the screen
        d.swipe(300, 1000, 300, 500)
        d.app_start('com.alibaba.android.rimet', stop=True)
        x, y = d(resourceId='com.alibaba.android.rimet:id/home_bottom_tab_button_work').center()
        print(x, y)
        d.click(x, y)
        print("点击百家云")
        info = d.xpath('考勤打卡').info
        d.click(info['bounds']['left'] + 20, info['bounds']['top'] - 50)
        print("点击考勤打卡")
        devices = d.info
        d.click(devices['displayWidth'] / 2, devices['displayHeight'] * 428 / 1184)
        print("点击打卡")
        d.app_stop('com.alibaba.android.rimet')
        d.screen_off()  # turn off the screen
