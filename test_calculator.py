import unittest
import calculator

class TestCalculatorMethods(unittest.TestCase):
    def test_addition(self):
        result = calculator.addition(4,6)
        self.assertEqual(result, 10)
    def test_subtraction(self):
        result = calculator.subtraction(7,9)
        self.assertEqual(result, -2)
    def test_multiplication(self):
        result = calculator.multiplication(5,6)
        self.assertEqual(result, 30)
    def test_division(self):
        result = calculator.division(3,6)
        self.assertEqual(result, .5)

if __name__ == "__main__":
    unittest.main(verbosity=2)