import unittest
from calc import add, sub, multiply, divide

class TestCalc(unittest.TestCase):
    #Assumes error handling from function returns None
    def test_add(self):
        self.assertEqual(add(1,2), 3)
        self.assertEqual(add(-1,2), 1)
        self.assertEqual(add(-1,-2), -3)

    def test_add_str(self):
        self.assertIsNone(add('1', 2))
        self.assertIsNone(add('1', '3'))
        self.assertIsNone(add('b', 'a'))

    def test_sub(self):
        self.assertEqual(sub(2, 1), 1)
        self.assertEqual(sub(1,-2), 3)
        self.assertEqual(sub(-1, 1), -2)
        self.assertEqual(sub(-1,-1), 0)

    def test_sub_char(self):
        self.assertIsNone(sub('1', 2))
        self.assertIsNone(sub('1', '3'))
        self.assertIsNone(sub('b', 'a'))
        
    def test_multiply(self):
        self.assertEqual(multiply(1, 2), 2)
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(2, -3), -6)
        self.assertEqual(multiply(-2, -3), 6)
        self.assertEqual(multiply(0, 1), 0)


    def test_multiply_char(self):
        self.assertIsNone(multiply('1', 2))
        self.assertIsNone(multiply('1', '3'))
        self.assertIsNone(multiply('b', 'a'))

    def test_divide(self):
        self.assertEqual(divide(2,1), 2)
        self.assertEqual(divide(-2,1), -2)
        self.assertEqual(divide(-2,-2), 1)
        self.assertEqual(divide(0,1), 0)

    def test_divide_zero(self):
        #Do not want to allow division by 0
        self.assertIsNone(divide(1,0))

    def test_divide_char(self):
        self.assertIsNone(divide('1', 2))
        self.assertIsNone(divide('1', '3'))
        self.assertIsNone(divide('b', 'a'))

if __name__ == "__main__":
    unittest.main(verbosity=2)