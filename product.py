
class Product:
    def __init__(self,name,price,quanity):
        self.quantity = quanity
        self.name = name
        self.price = price

    def calculate_total(self):
        if self.quantity <= 0 or self.price <= 0:
            raise ValueError("quantity or price must be  positive integer")
        else:
            return self.quantity*self.price



