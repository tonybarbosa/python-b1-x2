from abc import ABC, abstractmethod

class Person:
    def __init__(self, dni: str, email: str, mobile: str):
        # Write here your code
        pass

    @abstractmethod
    def print(self):
        pass

    def __eq__(self, another):
       # Do not change this method
       return hasattr(another, 'dni') and self.dni == another.dni
    
    def __hash__(self):
       # Do not change this method
       return hash(self.dni)

class Buyer(Person):
    def __init__(self, dni: str, email: str, mobile: str, full_name: str, age: int, address: str):
        # Write here your code
        pass

    def print(self):
        # Do not change this method
        print(f"Buyer: {self.dni}, email:{self.email}")

class Seller(Person):
    # Write the parameters in the next line
    def __init__():
        # Write here your code        
        pass
        
    def print(self):
        # Do not change this method
        print(f"Seller: {self.dni} , email:{self.email} ")
