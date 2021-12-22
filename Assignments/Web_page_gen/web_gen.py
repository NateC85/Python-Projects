

import tkinter
from tkinter import *
import webbrowser


class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)
        
        self.master = master
        self.master.geometry("{}x{}".format(500, 300))
        self.master.title('Web Page Generator')
        self.master.config(bg= 'skyblue')

        self.source = StringVar()

        self.text = Entry(self.master, text= self.source, font= ('Helvetica', 14), fg= 'black', bg= 'lightgrey')
        self.text.grid(row= 2, column= 3, columnspan= 3, padx= (30, 0), pady= (30, 0))

        self.btnOpen = Button(self.master, text= "Open", command = webbrowser, width= 10, height = 2)
        self.btnOpen.grid(row= 2, column= 2, padx= (0,0), pady= (30,0), sticky= NW)



    def webbrowser(self):
        f = open('index.html','w')
        message = """
        <html>
            <body>
                <h1>
                This is a test
                </h1>
            </body>
        </html>
        """

        f.write(message)
        f.close()
        webbrowser.open_new_tab('index.html')


if __name__ == ("__main__"):
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
