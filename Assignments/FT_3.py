

import tkinter 
from tkinter import Entry, messagebox
from tkinter import filedialog



main_win = tkinter.Tk()
main_win.geometry("500x300")
main_win.sourceFolder = ''
main_win.sourceFile = ''

# Defining a function to browse and choose a specific folder that will contain files to be checked daily.
def chooseDir(main_win):
    main_win.sourceFolder =  filedialog.askdirectory( parent=main_win, initialdir= "/", title='Please select a directory')

btn_chooseDir = tkinter.Button(main_win, text = "Choose Folder", width = 10, height = 3, command = chooseDir)
btn_chooseDir.grid(row= 1, column= 0, padx= (30, 0), pady= (30, 0))
btn_chooseDir.width = 100

# Defining a function to browse and choose a specific folder that will recieve copied files.
def chooseFile(main_win):
    main_win.sourceFile = filedialog.askopenfilename(parent=main_win, initialdir= "/", title='Please select a directory')

btn_chooseFile = tkinter.Button(main_win, text = "Choose File", width = 10, height = 3, command = chooseFile)
btn_chooseFile.grid(row= 2, column= 0, padx= (30, 0), pady= (30, 0))
btn_chooseFile.width = 100


def FileCheck_btn(main_win):
    main_win.sourceFolder =  filedialog.askdirectory(parent=main_win, initialdir= "/", title='Please select a directory')

btn_FileCheck_btn = tkinter.Button(main_win, text = "Check for file.", width = 10, height = 3, command = chooseDir)
btn_FileCheck_btn.grid(row= 3, column= 0, padx= (30, 0), pady= (30, 0))
btn_FileCheck_btn.width = 100
btn_FileCheck_btn.text = Entry(main_win, text= 'filename', font= ('Helvetica', 12), fg= 'black', bg= 'white')
btn_FileCheck_btn.text.grid(row= 3, column= 2, padx= (30, 0), pady= (30, 0))
    





if __name__ == '__main__':
    main_win.mainloop()
    print(main_win.sourceFolder)
    print(main_win.sourceFile)
