
class Product:
    def __init__(self,name,price,quanity):
        self.quantity = quanity
        self.name = name
        self.price = price

    def calculate_total(self):
        if self.quantity <= 0:
            raise ValueError("quantity must be  positive integer")

        if self.price < 0:
           raise ValueError("price must be positive integer or zero")
        
        return self.quantity*self.price



