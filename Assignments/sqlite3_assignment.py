


import sqlite3
connection = sqlite3.connect("C:/Users/natec/Desktop/test_database.db")

c = connection.cursor()
c.execute("CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT)")
