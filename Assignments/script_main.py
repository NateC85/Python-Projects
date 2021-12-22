

from tkinter import *
import tkinter as tkinter

import script_gui
import script_func


# Parent class
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # Define master frame configuration
        self.master = master
        self.master.minsize(500, 300)
        self.master.maxsize(500,300)
        script_func.center_window(self,500,300)
        self.master.title("Script GUI")
        self.master.congigure(bg= "#F0F0F0)")
        self.master.protocol("WM_DELETE_WINDOW", lambda: script_func.ask_quit(self))
        arg = self.master

        script_gui.load_gui(self)

        # Instantiate Tkinter dropdown object
        menubar = Menu(self.master)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_separator()
        filemenu.add_command(label= "Exit", underline= 1, accelerator= "Ctrl+Q", command= lambda: script_func.ask_quit(self))
        menubar.add_cascade(label= "File", underline= 0, menu = filemenu)
        helpmenu = Menu(menubar, tearoff= 0)
        helpmenu.add_separator()
        helpmenu.add_command(label= "How to use this program")
        helpmenu.add_separator()
        helpmenu.add_command(label= "About this demo script")
        menubar.add_cascade(label= "Help", menu= helpmenu)

        self.master.config(menu= menubar, borderwidth= '1')


if __name__ == "__main__":
    #This Instantiates the Tk.() root frame (window) into being
    root = tk.Tk()
     #This instantiates our own class as an App object
    App = ParentWindow(root)
    root.mainloop()
