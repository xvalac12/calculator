import unittest
from calc import calculate_expression

class TestAddition(unittest.TestCase):

    def small_numbers(self):
        
        self.assertEqual(calculate_expression("1 + 2"), 3)
        self.assertEqual(calculate_expression("1.0 + 2.0"), 3)
        self.assertEqual(calculate_expression("1 + 2 + 3"), 6)
        self.assertEqual(calculate_expression("2 + 1"), 3)

        self.assertEqual(calculate_expression("1.5 + 3.5"), 5)


    def large_numbers(self):
        
        self.assertEqual(calculate_expression("2000 + 11100000"), 11102000)
        self.assertEqual(calculate_expression("2000.0 + 11100000.0"), 11102000)
        self.assertEqual(calculate_expression("2000 + 11100000 + 3212316"), 14314316)


    def negative_numbers(self):

        self.assertEqual(calculate_expression("-2 + 1"), -1)
        self.assertEqual(calculate_expression("-2 + -1"), -3)
        self.assertEqual(calculate_expression("2 + -1"), 1)

        self.assertEqual(calculate_expression("-2.0 + 1.0"), -1)
        self.assertEqual(calculate_expression("-2.0 + -1.0"), -3)
        self.assertEqual(calculate_expression("2.0 + -1.0"), 1)


class TestSubstratcion(unittest.TestCase):

    def small_numbers(self):

        self.assertEqual(calculate_expression("2 - 1"), 1)
        self.assertEqual(calculate_expression("5 - 2"), 3)
        self.assertEqual(calculate_expression("10 - 2 - 3 - 1"), 4)


    def large_numbers(self):        

        self.assertEqual(calculate_expression("2000000 - 1"), 1999999)
        self.assertEqual(calculate_expression("23213 + 6549"), 29762)
        self.assertEqual(calculate_expression("2000.25 + 32332.75 + 32.7 + 3.3 "), 34369)


    def negative_numbers(self):
        self.assertEqual(calculate_expression("-3 - -6"), 3)
        self.assertEqual(calculate_expression("5 - -7"), 11)
        self.assertEqual(calculate_expression("-6 - 10"), -16)
        self.assertEqual(calculate_expression("-3.5 - 3"), -6.5)



if __name__ == '__main__':
    unittest.main()