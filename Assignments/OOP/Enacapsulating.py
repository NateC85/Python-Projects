

#Initializing the class and setting the protected and private variables
class User:
     def __init__(self, name, age=7):
         self._name = name
         self.__age = age

# Accessing variables
     def display(self):
         print("Name: ", self._name)
         print("Age: ", self.__age)


     def Name(self):
         self._name = ""
     
     def Age(self):
         print(self.__age)

# defining the getter method
     def getAge(self):
         print(self.__age)

# defining the setter method
     def setAge(self, age):
         self.__age = ""

# Calling the functions
user = User("Jovanni")
user.display()
user.setAge(7)
user.getAge()


     





   



        
    
