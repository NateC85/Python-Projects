

import time
import os
import shutil

seconds_in_day = 24 * 60 * 60

source = '/Users/natec/OneDrive/Desktop/Folder_C/'
destination = '/Users/natec/OneDrive/Desktop/Folder_D/'

now = time.time()
before = now - seconds_in_day


def last_mod(fname):
    return os.path.getmtime(fname)

    for fname in os.listdir(src):
        src_fname = os.path.join(source, fname)

        if last_mod(src_fname) > before:
            dst_fname = os.path.join(destination, fname)
            shutil.move(src_fname+1, dst_fname)


if __name__ == '__main__':
