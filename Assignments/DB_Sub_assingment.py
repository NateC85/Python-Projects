#imports sqlite, giving Python access to sqlite3's methods
import sqlite3


conn = sqlite3.connect('test1.db') #creates a variable that connects to the database, and holds the connection to the database

#create/save a database 
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files(ID INTEGER PRIMARY KEY AUTOINCREMENT,\
                col_fname TEXT)")
    conn.commit()

conn = sqlite3.connect('test1.db')

#creating a variable and assigning it a multiple-element tuple
fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')


#loops through each object in the tuple to find the files that end with '.txt'
for f in fileList:
    if f.endswith('.txt'):
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_files (col_fname) VALUES (?)", (f,))
            print(f)


#closes connection
conn.close()
