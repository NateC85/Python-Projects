

import tkinter
from tkinter import *
import webbrowser


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self)
        
        self.master = master
        self.master.geometry("{}x{}".format(500, 300))
        self.master.title('Web Page Generator')
        self.master.config(bg= 'skyblue')

        self.source = StringVar()

        self.label = Label(self.master, text= "Enter text here.")
        self.label.grid(row= 1, column= 3, columnspan= 3, padx= (30, 0), pady= (30, 0))
        
        self.text = Entry(self.master, text= self.source, font= ('Helvetica', 14), fg= 'black', bg= 'lightgrey')
        self.text.grid(row= 2, column= 3, columnspan= 3, padx= (30, 0), pady= (30, 0))

        self.btnOpen = Button(self.master, text= "Open", width= 10, height = 2, command=lambda: web_browser(self))
        self.btnOpen.grid(row= 2, column= 2, padx= (0,0), pady= (30,0), sticky= NW)



def web_browser(self):
                    
    message = """
    <html>
        <body>
            <h1>
                This is a test
            </h1>

    """
    message2 = self.text.get()
    message3 = """
        </body>
    </html>
    """
    with open("index.html", "w") as f:
        f.write(message + message2 + message3)
    url = "index.html"
    webbrowser.open_new_tab(url)


if __name__ == ("__main__"):
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
