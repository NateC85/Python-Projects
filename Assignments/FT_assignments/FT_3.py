

import tkinter
from tkinter import *
from tkinter import Entry, Label, StringVar

import FT_2


def load_gui(self):

    self.lbl = Label(self.master, text= 'Choose Source')
    self.lbl.grid(row=1, column= 2, columnspan= 2, padx= (30, 0), pady= (30,0))

    self.textField1 = Entry(self.master, text = "")
    self.textField1.grid(row= 2, column= 2, columnspan= 3, padx= (30, 0), pady= (30, 0))

    self.btnSrc = Button(self.master, text = "Source", width = 10, height = 3, command= lambda: FT_2.chooseSrc(self))
    self.btnSrc.grid(row= 2, column= 0, padx= (30, 0), pady= (30, 0))

    self.lbl = Label(self.master, text= 'Destination')
    self.lbl.grid(row=3, column= 2, columnspan= 2, padx= (30, 0), pady= (30,0))

    self.textField2 = Entry(self.master, text = "")
    self.textField2.grid(row= 4, column= 2, columnspan= 3, padx= (30, 0), pady= (30, 0))

    self.btnDest = Button(self.master, text = "Destination", width = 10, height = 3, command= lambda: FT_2.chooseDest(self))
    self.btnDest.grid(row= 4, column= 0, padx= (30, 0), pady= (30, 0))

    self.btnFCheck = Button(self.master, text= "Check for file",width = 10, height = 3, command= lambda: FT_2.move_files(self))
    self.btnFCheck.grid(row= 5, column= 0, padx= (30, 0), pady= (30, 0))

   

   
if __name__ == '__main__':
   pass