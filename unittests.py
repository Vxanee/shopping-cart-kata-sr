import unittest
from Shopping_cart_kata import calculate_subtotal

class TestCalculateSubtotal(unittest.TestCase):
    def test_valid_input(self):
         # testing with a valid shopping cart
        cart = [{"code": "A", "quantity": 2}, {"code": "B", "quantity": 1}]
        self.assertEqual(calculate_subtotal(cart), 135)

    def test_missing_product(self):
        # testing a shopping cart containing a missing product
        cart = [{"code": "A", "quantity": 2}, {"code": "X", "quantity": 1}]
        # ensures that function handles missing products 
        self.assertEqual(calculate_subtotal(cart), 100)

    def test_negative_quantity(self):
        # testing shopping cart containing negative quantity
        cart = [{"code": "B", "quantity": -1}, {"code": "C", "quantity": 1}]
        # ensures that function handles negative quantities
        self.assertEqual(calculate_subtotal(cart), 25)
    
    def test_special_price(self):
        # testing shopping cart containing special price bundles
        cart = [{"code": "A", "quantity": 3}, {"code": "B", "quantity": 2}]
        self.assertEqual(calculate_subtotal(cart), 200)
    
    def test_special_and_normal_price(self):
        # testing shopping cart with discount price bundle and normal price
        cart = [{"code": "A", "quantity": 3}, {"code": "B", "quantity": 3}]
        self.assertEqual(calculate_subtotal(cart),235)


if __name__ == "__main__":
    unittest.main()