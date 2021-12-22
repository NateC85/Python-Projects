


from abc import ABC, abstractmethod

# Abstract Base Class
class Bank(ABC):
    def bank_info(self):
        print("Welcome!")

# Abstract Method
    @abstractmethod
    def interest(self):
        pass

# Child class
class NFCU(Bank):
    def balance(self):
        print("Current balance is $750.00")

# Sub class
class Int1(NFCU):
    def interest(self):
        print("The NFCU interest is 3.75%.")

# Invokes methods our classes
int = Int1()
int.bank_info()
int.balance()
int.interest()
