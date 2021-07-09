#!/bin/sh

. /etc/profile
cd /root/docker/Covid19Briefing
git config --global user.email "***REMOVED***"
git config --global user.name "unkoe"
git config --global http.proxy socks5://danted:imH8f6fzosB80@138.128.214.84:1080
echo "UPDATE ... `pwd`"
/usr/bin/git pull
echo "START TIMING"
/usr/bin/python3 main.py
