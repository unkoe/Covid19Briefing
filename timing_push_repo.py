import logging
import os
import time

commit_success_reply = "changed"
commit_noting_reply = "nothing to commit"

push_done = "done."
push_over = "up-to-date"
current_path = os.getcwd()


def commit():
    os.system("git add .")
    return os.popen(
        "git commit -am 'Covid-19 简报更新  ---> update time: " + time.strftime("%Y-%m-%d %H:%M:%S",
                                                                           time.localtime()) + "'").read()


def push():
    os.system("git pull")
    info = os.popen("git push --force origin master").read()
    logging.warning("git info"+info)
    return info


def start(path=""):
    if len(path) == 0:
        os.chdir(current_path)
    else:
        try:
            os.chdir(path)
        except Exception:
            os.chdir(current_path)

    reply = commit()
    if commit_success_reply in reply:
        logging.warning("commit success, start push, try again 3 times ")
        count = 1
        while push_over not in push():
            if count > 3:
                logging.warning("retried 3 times , break")
                break
            logging.warning("push fail, retry " + str(count))
            count += 1
    elif commit_noting_reply in reply:
        logging.warning("noting commit...")
    else:
        logging.warning("no expected work..." + str(reply))
