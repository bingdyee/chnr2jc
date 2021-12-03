import os
import shutil
import time


def full_capitalize(name, seps=('_', '-', ' ')):
    name = name.title()
    for sep in seps:
        name = name.replace(sep, '')
    return name

lower_first = lambda name: name[0].lower() + name[1:]


def format_time(fmt='%Y-%m-%d %H:%M:%S'):
    return time.strftime(fmt, time.localtime(time.time()))


def mkdirs(target):
    if not os.path.exists(target):
        os.makedirs(target)


def copy(src, dest):
    shutil.copytree(src, dest, ignore=None)


def rmdirs(target):
    if os.path.exists(target):
        shutil.rmtree(target)


def dirs(target):
    rs = []
    for root, _, files in os.walk(target):
        rs += [os.path.join(root, file) for file in files]
    return rs


