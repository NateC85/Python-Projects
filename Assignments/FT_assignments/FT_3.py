
import tkinter
from tkinter import *

from tkinter import Entry, Label, StringVar, messagebox
from tkinter import filedialog

from FT_2 import chooseDest, chooseSrc, move_files


def load_gui(self):

    self.lbl = Label(self.master, text= 'Choose Source')
    self.lbl.grid(row=1, column= 2, columnspan= 2, padx= (30, 0), pady= (30,0))

    self.textField1 = Entry(self.master, text =self.sourceFolder)
    self.textField1.grid(row= 2, column= 2, columnspan= 3, padx= (30, 0), pady= (30, 0))

    self.btnSrc = Button(self.master, text = "Source", width = 10, height = 3, command= lambda: chooseSrc(self))
    self.btnSrc.grid(row= 2, column= 0, padx= (30, 0), pady= (30, 0))

    self.lbl = Label(self.master, text= 'Choose Destination')
    self.lbl.grid(row=3, column= 2, columnspan= 2, padx= (30, 0), pady= (30,0))

    self.textField2 = Entry(self.master, text =self.destFolder)
    self.textField2.grid(row= 4, column= 2, columnspan= 3, padx= (30, 0), pady= (30, 0))

    self.btnDest = Button(self.master, text = "Destination", width = 10, height = 3, command= lambda: chooseDest(self))
    self.btnDest.grid(row= 4, column= 0, padx= (30, 0), pady= (30, 0))

    self.btnFCheck = Button(self.master, text= "File Check",width = 10, height =  3, command= lambda: move_files())
    self.btnFCheck.grid(row= 5, column= 0, padx= (30, 0), pady= (30, 0))

   

   



    


if __name__ == '__main__':
   pass
