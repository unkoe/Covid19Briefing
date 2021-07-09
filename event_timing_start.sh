#!/bin/sh

. /etc/profile
cd /root/docker/Covid19Briefing
git config --global user.email "***REMOVED***"
git config --global user.name "unkoe"
echo "UPDATE ... `pwd`"
/usr/bin/git pull
echo "START TIMING"
/usr/bin/python3 main.py
