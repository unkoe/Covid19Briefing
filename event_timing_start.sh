#!/bin/sh

. /etc/profile

echo "UPDATE CODES, `pwd`"
git pull
echo "START TIMING"
python3 main.py
