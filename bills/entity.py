from abc import ABC, abstractmethod
'''
En el módulo denominado "entity.py", se deben establecer las clases siguientes: "Person", "Buyer" y "Seller", 
las cuales representan a clientes y vendedores.
'''

'''
La clase "Person" es una clase abstracta que contiene el método abstracto "print()" y contiene los atributos 
comunes de las clases "Buyer" y "Seller". El alumno debe identificar estos atributos y crear un constructor 
con estos atributos.
'''

class Person:
    def __init__(self, dni: str, email: str, mobile: str):  # no detecto que seller tenga mobile
        # Write here your code
        self.dni = dni
        self.email = email  
        self.mobile = mobile
    @abstractmethod
    def print(self):
        pass

    def __eq__(self, another):
       # Do not change this method
       return hasattr(another, 'dni') and self.dni == another.dni
    
    def __hash__(self):
       # Do not change this method
       return hash(self.dni)

'''
La clase "Buyer" representa a un comprador, cuyos atributos son el dni(dni: str), el nombre completo 
(full_name: str), la edad (age: int), el correo electrónico (email: str), el teléfono móvil  (mobile: str) y 
su domicilio  (address: str). El alumno debe crear un constructor con estos atributos.
'''


class Buyer(Person):
    def __init__(self, dni: str, email: str, mobile: str, full_name: str, age: int, address: str):
        # Write here your code
        super().__init__(dni, email, mobile)
        self.full_name = full_name 
        self.age = age
        self.address = address

    def print(self):
        # Do not change this method
        print(f"Buyer: {self.dni}, email:{self.email}")

'''
La clase "Seller" representa a un comprador, cuyos atributos son el dni (dni: str), correo (email: str),
teléfono móvil (mobile: str), domicilio fiscal (bussines_name: str), razón social (bussines_address: str). 
El alumno debe crear un constructor con estos atributos.
'''


class Seller(Person):
    # Write the parameters in the next line
    def __init__(self, dni: str, email: str, mobile: str, bussines_name: str, bussines_address: str):
        # Write here your code
        super().__init__(dni, email, mobile)
        self.bussines_name = bussines_name
        self.bussines_address = bussines_address

    def print(self):
        # Do not change this method
        print(f"Seller: {self.dni} , email:{self.email} ")



#### cargatr datos de prueba
import util_package.bill_manager
#bill_manager = util_package.bill_manager.BillManager()