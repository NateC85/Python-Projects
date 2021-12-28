

import time
import os
import shutil
import datetime
from tkinter import Entry, messagebox
from tkinter import filedialog
from tkinter import *
import tkinter as tk


import FT_3

# Retreives current date and time
now = datetime.datetime.now()

# Using "timedelta to get the date and time 24 hours ago.
# A way of creating a measurement of time in specific units(days, seconds, hours, weeks, etc.)
before = now - datetime.timedelta(hours=24)


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # Master frame configuration
        self.master = master
        self.master.geometry("{}x{}".format(500, 300))
        self.master.title('File Transfer pt.3')



# Defining a function to move the files that have been modified in the last 24 hours.
def move_files():
    for fname in os.listdir(chooseSrc):
        # Gets the absolute path of the source file.
        src_fname = os.path.join(chooseSrc, fname)
        # Get the modification time in the mtime format.
        mtime = os.path.getmtime(fname)
        # Converts the mtime format to a proper datetime format.
        modtime = datetime.datetime.fromtimestamp(mtime)
        # Reurns the modification time of the file.

        # Calling the last_mod() function to check if the file was modified
        # within the last 24 hours.
        if move_files(src_fname) > before:
            # The shutil.move() method will move the file to the destination directory
            # if the file has been modified within the last 24 hours.
            shutil.move(src_fname, chooseDest)

        return modtime




def chooseSrc(self):
    self.sourceFolder =  filedialog.askdirectory()
    self.textField1.insert(0, self.sourceFolder)


def chooseDest(self):
    self.destFolder =  filedialog.askdirectory()
    self.textField2.insert(0, self.destFolder)


# Calling funtions
if __name__ == '__main__':
    root = Tk()
    move_files()
    root.mainloop()
