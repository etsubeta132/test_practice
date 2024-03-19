import unittest
from product import Product
from store import ShopingCart

class TestShopingCart(unittest.TestCase):
    def test_getChart(self):
        cart = ShopingCart()
        total = cart.getCartTotal()
        self.assertEqual(total,0)
    
    def test_getCartTotal_with_products(self):
        cart = ShopingCart()
        cart.addProduct(Product("x",12,3))
        cart.addProduct(Product("x",5,4))
        total = cart.getCartTotal()
        self.assertEqual(total,2)

# test class ......
if __name__ == '__main__':
    unittest.main()
