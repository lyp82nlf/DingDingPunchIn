#!/bin/bash
# 说明 下面的所有坐标都需要自己设置一下 每个手机可以自己适配  延迟时间根据手机响应时间来
# 红米 邱凌
adb -s $1 shell input keyevent 223 #熄灭屏幕
sleep 3s
adb -s $1 shell input keyevent 224 #点亮屏幕
sleep 5s
adb -s $1 shell input swipe 300 1000 300 500
sleep 3s
adb -s $1 shell am start -n com.alibaba.android.rimet/.biz.LaunchHomeActivity
sleep 30s
adb -s $1 shell input tap 531  1842 #点击百家云图标
sleep 30s
adb -s $1 shell input tap 951  986 #点击考勤打卡图标
sleep 30s
adb -s $1 shell input tap 184 1140 #点击考勤打卡
sleep 30s
adb -s $1 shell input tap 826 1049 #点击考勤打卡
sleep 30s
adb shell am force-stop com.alibaba.android.rimet
sleep 30s
adb -s $1 shell input keyevent 223 #熄灭屏幕
