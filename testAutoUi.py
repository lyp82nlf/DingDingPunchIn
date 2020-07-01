import uiautomator2 as u2
import time

if __name__ == '__main__':
    d = u2.connect_usb('2b59a736')
    d.app_start('com.alibaba.android.rimet', stop=True)
    time.sleep(5)
    d(resourceId='com.alibaba.android.rimet:id/home_bottom_tab_text', text='百家云').click()
    print("点击百家云")
    time.sleep(5)
    d(text='考勤打卡').click()
    time.sleep(5)
    d(text='更新打卡').click()
    time.sleep(5)
    d(text='确定').click()
    d.app_stop('com.alibaba.android.rimet')
