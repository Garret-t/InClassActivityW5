import unittest
from calc import add, sub, multiply, divide

class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1,2), 3)
        self.assertEqual(add(-1,2), 1)
        self.assertEqual(add(-1,-2), -3)

    def test_sub(self):
        self.assertEqual(sub(2, 1), 1)
        self.assertEqual(sub(1,-2), 3)
        self.assertEqual(sub(-1, 1), -2)
        self.assertEqual(sub(-1,-1), 0)

    def test_multiply(self):
        self.assertEqual(multiply(1, 2), 2)
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(2, -3), -6)
        self.assertEqual(multiply(-2, -3), 6)
        self.assertEqual(multiply(0, 1), 0)

    def test_divide(self):
        self.assertEqual(divide(2,1), 2)
        self.assertEqual(divide(-2,1), -2)
        self.assertEqual(divide(-2,-2), 1)

if __name__ == "__main__":
    unittest.main(verbosity=2)