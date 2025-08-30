# test_calc.py
import unittest
import calc

class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(2, 3), 5)
        self.assertEqual(calc.add(-1, 1), 0)

    def test_sub(self):
        self.assertEqual(calc.sub(5, 3), 2)
        self.assertEqual(calc.sub(0, 4), -4)

if __name__ == "__main__":
    unittest.main()
