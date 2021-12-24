

import time
import os
import shutil

seconds_in_day = 24 * 60 * 60

# Source of files to be transfered
source = '/Users/natec/OneDrive/Desktop/Folder_C/'

# Destination folder of the files transfered
destination = '/Users/natec/OneDrive/Desktop/Folder_D/'

now = time.time()
before = now - seconds_in_day

# Defining a function that checks for recently modified files
def last_mod(fname):
    
    for fname in os.listdir(src):
        src_fname = os.path.join(source, fname)

        if last_mod(src_fname) > before:
            dst_fname = os.path.join(destination, fname)
            shutil.copy(src_fname+i, dst_fname)
            shutil.move(src_fname+i, dst_fname)
            
        return os.path.getmtime(fname)

        
if __name__ == '__main__':
    copy = last_mod(fname)
    last_mod.fname
    move = last_mod(fname)
