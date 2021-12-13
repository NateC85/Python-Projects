


from typing import AsyncGenerator


class User:
     def __init__(self, name, age=0):
         self._name = name
         self.__age = age

     def display(self):
         print(self._name)
         print(self.__age)

     def Name(self):
         self._name = ""
     
     def Age(self):
         print(self.__age)

     def getAge(self):
         print(self.__age)

     def setAge(self, age):
         self.__age = "Age is 7 years old"


user = User("Jovanni")
user.display()
user.setAge(7)
user.getAge()


     





   



        
    
