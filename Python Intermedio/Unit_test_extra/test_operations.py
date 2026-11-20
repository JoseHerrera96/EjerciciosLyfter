import unittest

class TestOperations(unittest.TestCase):
    def test_average(self):
        #positive numbers
        numbers = [1, 2, 3, 4, 5]
        expected_average = sum(numbers) / len(numbers)
        self.assertEqual(expected_average, 3)
        #negative numbers
        numbers = [-1, -2, -3, -4, -5]
        expected_average = sum(numbers) / len(numbers)
        self.assertEqual(expected_average, -3)
        #Zeros
        numbers = [0, 0, 0, 0, 0]
        expected_average = sum(numbers) / len(numbers)
        self.assertEqual(expected_average, 0)
    

    def test_sum(self):
        #positive numbers
        numbers = [1, 2, 3, 4, 5]
        expected_sum = sum(numbers)
        self.assertEqual(expected_sum, 15)
        #negative numbers
        numbers = [-1, -2, -3, -4, -5]
        expected_sum = sum(numbers)
        self.assertEqual(expected_sum, -15)
        #Zeros
        numbers = [0, 0, 0, 0, 0]
        expected_sum = sum(numbers)
        self.assertEqual(expected_sum, 0)

    def test_max(self):
        #positive numbers
        numbers = [1, 2, 3, 4, 5]
        expected_max = max(numbers)
        self.assertEqual(expected_max, 5)
        #negative numbers
        numbers = [-1, -2, -3, -4, -5]
        expected_max = max(numbers)
        self.assertEqual(expected_max, -1)
        #Zeros
        numbers = [0, 0, 0, 0, 0]
        expected_max = max(numbers)
        self.assertEqual(expected_max, 0)

if __name__ == "__main__":
    unittest.main()