#!/bin/sh

. /etc/profile

echo "UPDATE ... `pwd`"
git pull
echo "START TIMING"
/bin/python3 /root/docker/Covid19Briefing/main.py
