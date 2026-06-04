class Product:
    def __init__(self, product_name, price):
        self.product_name = product_name
        self.price = price

class Electronics(Product):
    def __init__(self, product_name, price, warranty):
        super().__init__(product_name, price)
        self.warranty = warranty

    def display(self):
        print(self.product_name)
        print(self.price)
        print(self.warranty)

e = Electronics("Laptop", 50000, "2 Years")
e.display()