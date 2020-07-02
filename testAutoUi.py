import uiautomator2 as u2
import time
import autoUi_offWork

if __name__ == '__main__':
    d = u2.connect_usb('QLXBBBA640771867')
    # # d.screen_off()  # turn off the screen
    # # time.sleep(3)
    # d.screen_on()  # turn on the screen
    # time.sleep(5)
    # d.app_start('com.alibaba.android.rimet', stop=True)
    # time.sleep(5)
    # d(resourceId='com.alibaba.android.rimet:id/home_bottom_tab_text', text='工作台').click()
    # print("点击百家云")
    # time.sleep(5)
    # test = d(text='考勤打卡').info
    # d.click(test['bounds']['left'] + 20, test['bounds']['top'] - 50)
    # time.sleep(5)
    # d.xpath('更新打卡').click()
    # time.sleep(5)
    # d.xpath('确定').click()
    # time.sleep(5)
    # d.app_stop('com.alibaba.android.rimet')
    # time.sleep(5)
    # d.screen_off()  # turn off the screen
