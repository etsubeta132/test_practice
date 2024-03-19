from product import Product
import unittest

class TestProduct(unittest.TestCase):
    def test_calculate_total(self):
        pdt = Product("x",12,2)
        result = pdt.calculate_total()
        self.assertEqual(result,24)

    def test_zero_quantity(self):
        pdt = Product("x",0,1)
        with self.assertRaises(ValueError):
            total = pdt.calculate_total()
        

    def test_negative_quantity(self):
        pdt = Product('x',-1,5)
        with self.assertRaises(ValueError):
            total = pdt.calculate_total()
        
    def test_negative_price(self):
        pdt = Product('x',9,-1)
        with self.assertRaises(ValueError):
            total = pdt.calculate_total()

# test class ......
if __name__ == '__main__':
    unittest.main()
