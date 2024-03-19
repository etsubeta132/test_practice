
class ShopingCart:
    def __init__(self):
        self.cart = []
    
    def addProduct(self,product):
        self.cart.append(product)
    
    def getCartTotal(self):
        return len(self.cart)


    
