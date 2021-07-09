#!/bin/sh

. /etc/profile

echo "UPDATE ... `pwd`"
/usr/bin/git pull
echo "START TIMING"
/usr/bin/python3 /root/docker/Covid19Briefing/main.py
