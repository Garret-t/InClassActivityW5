import unittest
from calc import add, sub, multiply, divide

class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1,2), 3)
        self.assertEqual(add(-1,2), 1)
        self.assertEqual(add(-1,-2), -3)
        self.assertEqual(add(.5, 1.5), 2)
        self.assertEqual(add(-.5, 1.5), 1)
        self.assertEqual(add(-.5, -1.5), -2)

if __name__ == "__main__":
    unittest.main(verbosity=2)