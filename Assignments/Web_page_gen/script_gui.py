

from tkinter import *
import tkinter as tk

import script_main
import script_func


def load_gui(self):
    self.btn_browse = tk.Button(self.master, width= 12, height= 2, text= 'Browse', command= lambda: script_func.browse(self))
    self.btn_browse.grid(row= 2, column= 0, padx= (25,0), pady= (45,10), sticky= W)
    self.btn_open = tk.Button(self.master, width= 12, height= 4, text= 'Open File', command= lambda: script_function.open(self))
    self.btn_open.grid(row= 5, column= 0, padx= (25, 0), pady= (45, 10), sticky= W)
    self.btn_close = tk.Button(self.master, width= 12, height= 4, text= 'Close', command= lambda: script_func)
    