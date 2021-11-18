import unittest
from Entities.Operations import Operation
import random

class BasicOperations(unittest.TestCase):
    def test_adition_of_2_numbers_is_correct(self):
        expected_result = 5
        operation = Operation(3, 2)
        actual_result = operation.add()

        self.assertEqual(expected_result, actual_result)

    def test_adition_of_2_random_numbers_is_correct(self):
        num1 = random.randint(0, 10)
        num2 = random.randint(0, 10)
        expected_result = num1 + num2

        operation = Operation(num1, num2)
        actual_result = operation.add()

        self.assertEqual(expected_result, actual_result)

    def test_subtraction_of_2_numbers_is_correct(self):
        num1 = random.randint(0, 10)
        num2 = random.randint(0, 10)
        expected_result = num1 - num2

        operation = Operation(num1, num2)
        actual_result = operation.subtract()

        self.assertEqual(expected_result, actual_result)

    def test_multiplication_of_2_numbers_is_correct(self):
        num1 = random.randint(0, 10)
        num2 = random.randint(0, 10)
        expected_result = num1 * num2

        operation = Operation(num1, num2)
        actual_result = operation.multiplication()

        self.assertEqual(expected_result, actual_result)

    def test_division_of_2_numbers_is_correct(self):
        num1 = random.randint(0, 10)
        num2 = random.randint(0, 10)
        expected_result = num1 / num2

        operation = Operation(num1, num2)
        actual_result = operation.division()

        self.assertEqual(expected_result, actual_result)

    def test_division_of_2_numbers_is_correct(self):
        num1 = random.randint(0, 10)
        num2 = random.randint(0, 10)
        expected_result = num1 / num2

        operation = Operation(num1, num2)
        actual_result = operation.division()

        self.assertEqual(expected_result, actual_result)

if __name__ == '__main__':
    unittest.main()

## Probando del pull request de la rama