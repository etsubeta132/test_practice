
from product import Product
from store import ShopingCart

class TestShopingCart:
    def test_getChart(self):
        cart = ShopingCart()
        total = cart.getCartTotal()
        return total == 0
    
    def test_getCartTotal_with_products(self):
        cart = ShopingCart()
        cart.addProduct(Product("x",12,3))
        cart.addProduct(Product("x",5,4))
        total = cart.getCartTotal()
        return total == 2

# test class ......
test = TestShopingCart()
if test.test_getChart() and test.test_getCartTotal_with_products():
    print(True)
else:
    print(False)
