#!/bin/sh

. /etc/profile

echo "UPDATE ... `pwd`"
git pull
echo "START TIMING"
python3 main.py
