# https://github.com/runiformity173/lab11-EH-JM
import unittest

import calculator
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(calculator.add(2, 3), 5)
        self.assertEqual(calculator.add(-1, 1), 0)
        self.assertEqual(calculator.add(0, 0), 0)

    def test_subtract(self): # 3 assertions
        self.assertEqual(calculator.subtract(10, 4), 6)
        self.assertEqual(calculator.subtract(0, 5), -5)
        self.assertEqual(calculator.subtract(-3, -2), -1)

    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(calculator.mul(5,4),20)
        self.assertEqual(calculator.mul(-8,2),-16)
        self.assertAlmostEqual(calculator.mul(5.4,-5),-27.0)

    def test_divide(self): # 3 assertions
        self.assertAlmostEqual(calculator.div(5.0,-5),-1.0)
        self.assertAlmostEqual(calculator.div(5.4,2),2.7)
        self.assertAlmostEqual(calculator.div(-100.0,-5),20.0)
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            calculator.div(5, 0)

    def test_logarithm(self): # 3 assertions
        self.assertAlmostEqual(calculator.logarithm(2, 8), 3.0)
        self.assertAlmostEqual(calculator.logarithm(10, 100), 2.0)
        self.assertAlmostEqual(calculator.logarithm(4, 64), 3.0)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            calculator.logarithm(1, 5)

    # ##########################
    
    ####### Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            calculator.logarithm(0, 5)

    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(calculator.hypotenuse(3,4),5.0)
        self.assertAlmostEqual(calculator.hypotenuse(-6,-8),10.0)
        self.assertAlmostEqual(calculator.hypotenuse(-5,12),13.0)

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
           calculator.square_root(-5)
        # Test basic function
        self.assertAlmostEqual(calculator.square_root(4),2.0)
        self.assertAlmostEqual(calculator.square_root(6.25),2.5)
    #########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()