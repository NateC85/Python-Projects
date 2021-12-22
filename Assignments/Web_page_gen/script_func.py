

import os
import webbrowser
from tkinter import *
import tkinter as tk

import script_main
import script_gui


def center_window(self, w, h):
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    # Calculate x and y coordinates to paint the app centered on the user's screen
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo

def open(self):
    file_html = open('index.html', 'w')
    html_template = """
    <html>
        <body>
            <h1 input("")
            </h1>
        </body>
    </html>
    """
    file_html.write(html_template)
    file_html.close()
    webbrowser.open('index.html')
    

def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        self.master.destroy()
        os._exit(0)


if __name__ == "__main__":
    pass