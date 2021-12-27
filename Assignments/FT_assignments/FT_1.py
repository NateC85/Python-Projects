

import shutil
import os


# Source of files to be transfered
source = '/Users/natec/OneDrive/Desktop/Folder_A/'

# Folder destination of the files to transfer
destination = '/Users/natec/OneDrive/Desktop/Folder_B/'
files = os.listdir(source)

for i in files:
    # Telling the computer to move the files represented by 'i' to their new destination
        shutil.move(source+i, destination)


if __name__ == "__main__":
        pass
