


import time
import os
import shutil
import datetime
from tkinter import Entry
from tkinter import filedialog
from tkinter import *
import tkinter as tk

import FT_3

# Retreives current date and time
now = datetime.datetime.now()
# Using "timedelta to get the date and time 24 hours ago.
# A way of creating a measurement of time in specific units(days, seconds, hours, weeks, etc.)
before = now - datetime.timedelta(hours=24)
print(before)

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        # Master frame configuration
        self.master = master
        self.master.geometry("{}x{}".format(400, 300))
        self.master.title('File Transfer pt.3')
        
        FT_3.load_gui(self);




# Defining a function to move the files that have been modified in the last 24 hours.
def move_files(self):
    source = self.textField1.get()
    destination = self.textField2.get()
    files = os.listdir(source)
    for fname in files:
        # Gets the absolute path of the source file.
        src_fname = os.path.join(source, fname)
        # Get the modification time in the mtime format.
        mtime = os.path.getmtime(fname)
        # Converts the mtime format to a proper datetime format.
        modtime = datetime.datetime.fromtimestamp(mtime)
        
        # Calling the last_mod() function to check if the file was modified
        # within the last 24 hours.
        if modtime < before:
            chooseDest = os.path.join(destination, fname)
            # The shutil.move() method will move the file to the destination directory
            # if the file has been modified within the last 24 hours.
            shutil.move(src_fname, chooseDest)
        # Reurns the modification time of the file.
        return modtime



# Defining a function to connect to the textfield1 button
def chooseSrc(self):
    self.sourceFolder =  filedialog.askdirectory()
    self.textField1.insert(0, self.sourceFolder)

# Defining a function to connect to the textfield1 button
def chooseDest(self):
    self.destFolder =  filedialog.askdirectory()
    self.textField2.insert(0, self.destFolder)


# Calling funtions
if __name__ == '__main__':
    root = Tk()  #This Instantiates the Tk.() root frame (window) into being
    App = ParentWindow(root) #This instantiates our own class as an App object
    root.mainloop()# This ensures the Tkinter class object, our window, to keep looping
                   # meaning, it will stay open until we instruct it to close