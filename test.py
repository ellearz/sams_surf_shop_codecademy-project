import sams_surf_shop
import unittest

class TestSamsShop(unittest.TestCase):

    def setUp(self):
        self.cart  = sams_surf_shop.ShoppingCart()

    def test_add_surfboards(self):
        for num in [2,3,4]:
            with self.subTest(num):
                expected_result = num *1
                self.assertEqual(self.cart.add_surfboards(num),expected_result,f'Succesfully addess {expected_result} to cart!')
    def test_add_surfboards(self):
        self.assertEqual(self.cart.add_surfboards(1), "Successfully added 1 surfboard to cart!")
    def test_add_surfboards(self):
        self.assertEqual(self.cart.add_surfboards(2),"Successfully added 2 surfboard to cart!")
    @unittest.skip
    def test_add_surfboards(self):
        self.assertRaises(sams_surf_shop.TooManyBoardsError, self.cart.add_surfboards(5))
  
    def test_apply_local_discount(self):
        m=self.cart.apply_locals_discount
        self.assertTrue(m, self.cart.apply_locals_discount())

unittest.main()
        
        
 


