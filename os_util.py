import logging
import os
import shutil


def move(srcfile, destfile):
    if os.path.isfile(destfile):
        os.remove(destfile)
    if not os.path.isfile(srcfile):
        logging.warning("%s not exist!" % srcfile)
    else:
        fpath, fname = os.path.split(destfile)
        if not os.path.exists(fpath):
            os.makedirs(fpath)
        shutil.move(srcfile, destfile)
        logging.warning("move %s -> %s" % (srcfile, destfile))


def copy(srcfile, destfile):
    if os.path.isfile(destfile):
        os.remove(destfile)
    if not os.path.isfile(srcfile):
        logging.warning("%s not exist!" % srcfile)
    else:
        fpath, fname = os.path.split(destfile)
        if not os.path.exists(fpath):
            os.makedirs(fpath)
        shutil.copyfile(srcfile, destfile)
        logging.warning("copy %s -> %s" % (srcfile, destfile))
