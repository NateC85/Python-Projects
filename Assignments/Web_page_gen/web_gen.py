

# Importing needed modules
import tkinter
from tkinter import *
import webbrowser


# Parent class
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self)

        # Defining the master frame configuration
        self.master = master
        self.master.geometry("{}x{}".format(500, 300))
        self.master.title('Web Page Generator')
        self.master.config(bg= 'skyblue')

        self.source = StringVar()

        """
        Defining widgets and their initial configuration,
        and placing them using grid geometry.
        """ 
        self.label = Label(self.master, text= "Enter text below.")
        self.label.grid(row= 1, column= 3, columnspan= 3, padx= (30, 0), pady= (30, 0))
        
        self.text = Entry(self.master, text= self.source, font= ('Helvetica', 14), fg= 'black', bg= 'lightgrey')
        self.text.grid(row= 2, column= 3, columnspan= 3, padx= (30, 0), pady= (30, 0))

        self.btnOpen = Button(self.master, text= "Open", width= 10, height = 2, command=lambda: web_browser(self))
        self.btnOpen.grid(row= 2, column= 2, padx= (0,0), pady= (30,0), sticky= NW)


# Defining a function to create, open and write an
# html file that opens in a new browser tab.
def web_browser(self):
                    
    message = """
    <html>
        <body>
            <h1>
                Stay tuned for our amazing summer sale!
            </h1>

    """
    message2 = self.text.get()
    message3 = """
        </body>
    </html>
    """
    # Open function, opens and writes to the file displayed in the browser.
    with open("index.html", "w") as f:
        f.write(message + message2 + message3)
    url = "index.html"
    webbrowser.open_new_tab(url) # Opens the file in a new tab on default browser


if __name__ == ("__main__"):
    root = Tk() #This Instantiates the Tk.() root frame (window) into being
    App = ParentWindow(root) #This instantiates our own class as an App object
    root.mainloop()
