#!/bin/bash

echo "UPDATE CODES, "  pwd
git pull
echo "START TIMING"
python3 main.py
curr_pwd = `pwd`
corntab * * * * * sh $curr_pwd/event_timing_start.sh

