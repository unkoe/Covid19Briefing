import os

import os_util
import timing_push_repo
import logging

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


src_file = "/root/docker/qq-robot/download/pipline/covid/covid-19.json"
dest_file = os.getcwd() + "/covid19/covid-19.json"
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    logging.basicConfig(filename='log/debug.log', level=logging.INFO)
    os_util.copy(src_file, dest_file)
    timing_push_repo.start(dest_file)
