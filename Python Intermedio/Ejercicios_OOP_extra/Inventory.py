class Product:
    def __init__(self, name, price, qty):
        self.__name = name
        self.__price = price
        self.__qty = qty
    @property
    def get_name(self):
        return self.__name
    @property
    def get_price(self):
        return self.__price
    @property
    def get_qty(self):
        return self.__qty

class Inventory:
    def __init__(self):
        self.__products = []
    
    def add_product(self, product):
        self.__products.append(product)
    
    def get_total_price(self):
        total_price = 0
        for product in self.__products:
            total_price += product.get_price * product.get_qty
        return total_price
    
    def show_inventory(self):
        for product in self.__products:
            print(f"{product.get_name}: {product.get_qty} x {product.get_price} = {product.get_price * product.get_qty}")
        print(f"Total price: {self.get_total_price()}")
        print("-----------------")