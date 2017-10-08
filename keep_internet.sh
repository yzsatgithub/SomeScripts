#!/bin/bash


while :
do
        ping www.baidu.com &
        sleep 30
        PID=$!
        kill -INT $PID
        sleep 270
done
