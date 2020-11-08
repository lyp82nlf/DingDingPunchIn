#!/bin/sh
screnDir=$(pwd)/screen
echo $screnDir
screenPng="$screnDir/`date +%Y-%m-%d`-$2.png"
echo $screenPng

adb -s $1 shell screencap -p | sed 's/\r$//' >  $screenPng
sleep 3s