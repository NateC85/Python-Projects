

import tkinter 
from tkinter import Entry, messagebox
from tkinter import filedialog



main_win = tkinter.Tk()
main_win.geometry("500x300")
main_win.sourceFolder = ''
main_win.sourceFile = ''


def chooseDir():
    main_win.sourceFolder =  filedialog.askdirectory(parent=main_win, initialdir= "/", title='Please select a directory')

btn_chooseDir = tkinter.Button(main_win, text = "Chose Folder", width = 20, height = 3, command = chooseDir)
btn_chooseDir.grid(row= 1, column= 0, padx= (30, 0), pady= (30, 0))
btn_chooseDir.width = 100


def chooseFile():
    main_win.sourceFile = filedialog.askopenfilename(parent=main_win, initialdir= "/", title='Please select a directory')

btn_chooseFile = tkinter.Button(main_win, text = "Chose File", width = 20, height = 3, command = chooseFile)
btn_chooseFile.grid(row= 2, column= 0, padx= (30, 0), pady= (30, 0))
btn_chooseFile.width = 100


def FileCheck_btn():
    main_win.sourceFolder =  filedialog.askdirectory(parent=main_win, initialdir= "/", title='Please select a directory')

btn_chooseDir = tkinter.Button(main_win, text = "Check for file.", width = 20, height = 3, command = chooseDir)
btn_chooseDir.grid(row= 3, column= 0, padx= (30, 0), pady= (30, 0))
btn_chooseDir.width = 100
btn_chooseDir.text = Entry(main_win, text= 'filename', font= ('Helvetica', 12), fg= 'black', bg= 'white')
btn_chooseDir.text.grid(row= 3, column= 2, padx= (30, 0), pady= (30, 0))
    
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





if __name__ == '__main__':
    main_win.mainloop()
    print(main_win.sourceFolder)
    print(main_win.sourceFile )
