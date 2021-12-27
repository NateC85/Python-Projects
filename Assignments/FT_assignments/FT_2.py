

import time
import os
import shutil
import datetime


# Source of files to be transfered
source = '/Users/natec/OneDrive/Desktop/Folder_C/'

# Destination folder of the files transfered
destination = '/Users/natec/OneDrive/Desktop/Folder_D/'

# Retreives current date and time
now = datetime.datetime.now()

# Using "timedelta to get the date and time 24 hours ago.
# A way of creating a measurement of time in specific units(days, seconds, hours, weeks, etc.)
before = now - datetime.timedelta(hours=24)


# Defining a function that gets the modification time of a file.
def last_mod(fname):
    # Get the modification time in the mtime format.
    mtime = os.path.getmtime(fname)
    # Converts the mtime format to a proper datetime format.
    modtime = datetime.datetime.fromtimestamp(mtime)
    # Reurns the modification time of the file.
    return modtime

# Defining a function to move the files that have been modified in the last 24 hours.
def move_files():
    for fname in os.listdir(source):
        # Gets the absolute path of the source file.
        src_fname = os.path.join(source, fname)

        # Calling the last_mod() function to check if the file was modified
        # within the last 24 hours.
        if last_mod(src_fname) > before:
            # The shutil.move() method will move the file to the destination directory
            # if the file has been modified within the last 24 hours.
            shutil.move(src_fname, destination)

            
# Defining a function that allows user to manually initiate "filecheck" process.
def FileCheck(fname):
        try:
            open(fname, 'r')
            return 1
        except IOError:
            print("Error: File does not exist.")
            return 0

loop = 'y'
while loop == 'y':
    filename = input("Enter the name of the file that you would like to process: ")
    if FileCheck(filename) == 1:
        loop = 'n'
    else:
        print("File not found.")



# Calling funtion move_files()
if __name__ == '__main__':
    move_files()
