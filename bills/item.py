from enum import Enum
import datetime
from bills.entity import *

'''
En el módulo denominado "Item", se deben establecer las clases siguientes: "Product", "Tax", las cuales 
representan las facturas, los productos e impuestos.
'''

# Do not change the value of ISD_FACTOR var
ISD_FACTOR = 0.25


class TaxType(Enum):
    # Do not change this enum
    IVA = 1
    ISD = 2

'''
La clase denominada "Tax" se refiere a los impuestos que se derivan de cada producto. Los tipos de impuestos
que se presentan son los siguientes: el impuesto al valor agregado (IVA) y el impuesto a la salida de divisas 
(ISD). Los dos impuestos representan un porcentaje de gravamen en función del precio por la cantidad. 
Sus atributos son el identificador del impuesto (tax_id: str), tipo impuesto (tax_type: TaxType) y 
porcentaje de retención (percentage: float). Nótese existe un parámetro tipo enumeración TaxType, cuya 
función es identificar el tipo de impuesto.  El alumno debe crear un constructor con los atributos señalados.
'''



class Tax:
    # Write the parameters in the next line
    def __init__(self, tax_id: str, tax_type: TaxType, percentage: float):
        # Write here your code
        self.tax_id = tax_id
        self.tax_type = tax_type
        self.percentage = percentage

'''
La clase "Product" representa a un producto, cuyos atributos son el identificador (product_id: str), 
el nombre (name: str), la fecha de caducidad (expiration_date: datetime), el código de barras (bar_code: str), 
la cantidad (quantity: int), el precio (price: float) y una lista de impuestos (taxes: list[Tax]). 
El alumno debe crear un constructor para estos atributos.
'''




class Product:
     # Write the parameters in the next line
    def __init__(self, product_id: str, name: str, expiration_date: datetime, bar_code: str, quantity: int, price: float, taxes: list[Tax]):
        # Write here your code
        self.product_id = product_id
        self.name = name        
        self.expiration_date = expiration_date
        self.bar_code = bar_code
        self.quantity = quantity
        self.price = price
        self.taxes = taxes

    '''
    calculate_tax(tax:Tax): Se trata de una función que permite calcular el valor total del impuesto se calcula 
    mediante la multiplicación de la cantidad por el precio y posteriormente multiplicar por el porcentaje 
    de ese impuesto. El parámetro "tax" permite la filtración de la lista en función del tipo de impuesto, 
    sea IVA o ISD. Para el cálculo del ISD se debe multiplicar por un valor factor constante (ISD_FACTOR) 
    igual a 0.25. El valor a retornar es un número de tipo “float”.
    '''

    def calculate_tax(self, tax: Tax) -> float:
        # Write here your code
        self.tax = tax
        if tax.tax_type == TaxType.ISD:
            return self.quantity * self.price * tax.percentage * ISD_FACTOR
        return self.quantity * self.price * tax.percentage
   
    '''
    calculate_total_taxes(): Se trata de una función que posibilita la determinación de la suma total de los 
    impuestos depositados en una factura, es decir, todos aquellos que se encuentran incluidos en la lista de 
    impuestos, para esto se debe hacer uso de la función “calculate_tax(tax)”. El valor a retornar es un número 
    de tipo “float”.
    
    '''

    def calculate_total_taxes(self) -> float:
        # Write here your code
        for tax in self.taxes:
            self.calculate_tax(tax)
        return sum(self.calculate_tax(tax) for tax in self.taxes)

    '''
    calculate_total(): Permite calcular el total de un producto de la siguiente manera: se debe multiplicar el 
    valor total por la cantidad y luego se deberá sumar con el total de impuestos “calculate_total_taxes”.
    El valor a retornar es un número de tipo “float”.
    '''


    def calculate_total(self) -> float:
        # Write here your code
        return sum(self.quantity * self.price for tax in self.taxes) + self.calculate_total_taxes()

    def __eq__(self, another):
        # Do not change this method
        return hasattr(another, 'product_id') and self.product_id == another.product_id

    def __hash__(self):
        # Do not change this method
        return hash(self.product_id)

    def print(self):
        # Do not change this method
        print(
            f"Product Id:{self.product_id} , name:{self.name}, quantity:{self.quantity}, price:{self.price}")
        for tax in self.taxes:
            print(f"Tax:{tax.tax_type} , percentage:{tax.percentage}")

'''
La clase “Bill” se refiere a una factura y representa una transacción realizada entre un comerciante y un 
comprador; además, contiene los productos que se vendieron en una transacción. Los atributos son 
el id factura(bill_id:str), fecha de emisión(sale_date: datetime), un vendedor (seller: Seller), 
un comprador (buyer: Buyer), y una lista de productos(products: list[Product]). Esta debe incluir el siguiente 
método:
calculate_total(): Es una función que sirve para calcular el total de la factura de la siguiente manera: se debe
 sumar el total individual de cada factura. El valor a retornar es un número de tipo “float”.
'''



class Bill:
    def __init__(self, bill_id: str, sale_date: datetime, seller: Seller, buyer: Buyer, products: list[Product]):
        # Write here your code
        self.bill_id = bill_id
        self.sale_date = sale_date
        self.seller = seller
        self.buyer = buyer
        self.products = products

    def calculate_total(self) -> float:
        # Write here your code
        print("seller in bill: ", self.seller.dni, "buyer in bill: ", self.buyer.dni)
        for product in self.products:
            print("producto en factura: ", product.product_id, product.name, ", ", product.calculate_total())
        return sum(product.calculate_total() for product in self.products)

    def print(self):
        # Do not change this method
        self.buyer.print()
        self.seller.print()
        for product in self.products:
            product.print()