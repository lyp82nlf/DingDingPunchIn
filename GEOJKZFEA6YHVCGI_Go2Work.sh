#!/bin/bash
# 说明 下面的所有坐标都需要自己设置一下 每个手机可以自己适配  延迟时间根据手机响应时间来
# 红米 邱凌
adb -s $1 shell input keyevent 223 #熄灭屏幕
echo 设备$1开始
sleep 3s
adb -s $1 shell input keyevent 224 #点亮屏幕
echo 点亮屏幕
sleep 5s
adb -s $1 shell input swipe 300 1000 300 500
echo 解锁
sleep 3s
adb -s $1 shell am start -n com.alibaba.android.rimet/.biz.LaunchHomeActivity
echo 开启钉钉
sleep 30s
adb -s $1 shell input tap 531  1842 #点击百家云图标
echo 点击百家云图标
sleep 30s
adb -s $1 shell input tap 951  986 #点击考勤打卡图标
echo 点击考勤打卡图标
sleep 30s
adb -s $1 shell input tap 550 652 #点击考勤打卡
echo 点击考勤打卡
sleep 30s
adb -s $1 shell am force-stop com.alibaba.android.rimet
echo 关闭钉钉
sleep 30s
adb -s $1 shell input keyevent 223 #熄灭屏幕
echo 熄灭屏幕
