# Write your imports here
from bills.item import *
'''

En el módulo denominado "Stats", en este módulo se deben crear la clase "Statistics", este sirve para realizar 
un análisis estadístico con la información de las facturas.

La clase Statistics tiene como atributo una lista de facturas, cuyo propósito es obtener información estadística 
del comercio de los productos.

'''

class OrderType:
    # Do not change this enum
    ASC = 0
    DES = 1


class Statistics:
    def __init__(self, bills: list[Bill]):
        # Do not change this method
        self.bills = bills

    '''
    find_top_sell_product(): Se trata de una función que permite buscar el producto más vendido, es decir, 
    el producto que aparece con mayor frecuencia en las facturas. El valor devolver es una tupla donde el primer 
    valor es tipo “Product” y el segundo es la cantidad de apariciones del producto. Por ejemplo:
    (<bills.item.Product object at 0x000002D8F6DE2DD0>, 6)
    '''

    def find_top_sell_product(self) -> (Product, int):
        # Write here your code
        products_count = {}
        #print("facturas: ", self.bills)
        for bill in self.bills:
            for product in bill.products:
                products_count[product] = products_count.get(product, 0) + 1
        if products_count:
            product_max = max(products_count, key=products_count.get)
            #print("producto mas vendido: ", product_max.product_id, product_max.name, ", ",products_count.get(product_max, 0))
        return product_max, products_count.get(product_max, 0)
    
    '''
    find_top_two_sellers(): Es una función para buscar a los 2 primeros vendedores con el mayor importe total de 
    ventas. Esta devuelve de una lista de entidades pertenecientes a la clase "Seller". Por ejemplo:
    [<bills.entity.Seller object at 0x000002D8F6983BD0>, <bills.entity.Seller object at 0x000002D8F6DE2F50>]
    '''

    def find_top_two_sellers(self) -> list:
        # Write here your code
        sellers_count = {}
        for bill in self.bills:
            sellers_count[bill.seller] = sellers_count.get(bill.seller, 0) + bill.calculate_total()
        #print("sellers count: ", sellers_count)
        return sorted(sellers_count, key=sellers_count.get, reverse=True)[:2]   # transformar en lista

    '''
    find_buyer_lowest_total_purchases(): Se trata de una función que permite buscar al comprador con el menor 
    importe total de compras. El valor a devolver es una tupla en donde el primer valor es una entidad de tipo 
    “Buyer” y el segundo el total de ventas.  Por ejemplo:
    (<bills.entity.Buyer object at 0x0000020A8789F190>, 53.5)
    '''

    def find_buyer_lowest_total_purchases(self) -> (Buyer, float):
        # Write here your code
        buyers_count = {}
        for bill in self.bills:
            buyers_count[bill.buyer] = buyers_count.get(bill.buyer, 0) + bill.calculate_total()
        #print("buyers count: ", buyers_count,"===================================")
        if buyers_count:
            buyer_min = min(buyers_count, key=buyers_count.get)
            #print("buyer with lowest total purchases: ", buyer_min.dni, ", ", buyers_count.get(buyer_min, 0))   
        return buyer_min, buyers_count.get(buyer_min, 0)

    '''
    order_products_by_tax(order_type:orderType): Se trata de una función que permite devolver una lista ordenada 
    de todos productos. El parámetro order_type, es un tipo de enumeración OrderType, nos permite identificar 
    si el orden es ascendente o descendente, y debe ordenar por la suma total de impuestos para un producto. 
    El valor a devolver es una lista de tuplas en donde cada tupla se compone de entidad tipo “Product” y la 
    suma total de impuestos. Por ejemplo:
    [(<bills.item.Product object at 0x000001A5B79D2A50>, 180.0), (<bills.item.Product object at 0x000001A5B79D2910>, 37.08)]
    '''

    def order_products_by_tax(self, order_type: OrderType) -> tuple:
        # Write here your code
        products_tax = {}
        for bill in self.bills:
            for product in bill.products:
                products_tax[product] = products_tax.get(product, 0) + product.calculate_total_taxes()
        #print("productos por impuestos: ", products_tax)
        if order_type == OrderType.ASC:
            return sorted(products_tax.items(), key=lambda x: x[1])
        else:
            return sorted(products_tax.items(), key=lambda x: x[1], reverse=True)

    def show(self):
        # Do not change this method
        print("Bills")
        for bill in self.bills:
            bill.print()
