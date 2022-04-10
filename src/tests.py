import unittest
from calc import calculate_expression

class TestAddition(unittest.TestCase):

    def small_numbers(self):
        self.assertEqual(calculate_expression("1 + 2"), 3)
        self.assertEqual(calculate_expression("1.0 +2.0"), 3)
        self.assertEqual(calculate_expression("1+2 + 3"), 6)
        self.assertEqual(calculate_expression("2 + 1"), 3)

        self.assertEqual(calculate_expression("1.5 +3.5"), 5)


    def large_numbers(self):
        self.assertEqual(calculate_expression("2000 + 11100000"), 11102000)
        self.assertEqual(calculate_expression("2000.0 + 11100000.0"), 11102000)
        self.assertEqual(calculate_expression("2000 + 11100000+ 3212316"), 14314316)


    def negative_numbers(self):
        self.assertEqual(calculate_expression("-2 + 1"), -1)
        self.assertEqual(calculate_expression("-2 + -1"), -3)
        self.assertEqual(calculate_expression("2 + -1"), 1)

        self.assertEqual(calculate_expression("-2.0 + 1.0"), -1)
        self.assertEqual(calculate_expression("-2.0 + -1.0"), -3)
        self.assertEqual(calculate_expression("2.0 + -1.0"), 1)


    def exceptions(self):
        self.assertRaises(SyntaxError, calculate_expression("+"))
        self.assertRaises(SyntaxError, calculate_expression("10 + "))
        self.assertRaises(SyntaxError, calculate_expression("+ 2"))
        self.assertRaises(SyntaxError, calculate_expression("10 + 2 +"))
        self.assertRaises(SyntaxError, calculate_expression("+ 10 + 2"))
        self.assertRaises(SyntaxError, calculate_expression("10 + + 2"))


class TestSubstratcion(unittest.TestCase):

    def small_numbers(self):
        self.assertEqual(calculate_expression("2- 1"), 1)
        self.assertEqual(calculate_expression("5 -2"), 3)
        self.assertEqual(calculate_expression("10-2 - 3 - 1"), 4)

        self.assertEqual(calculate_expression("10.5 - 2.5"), 8)


    def large_numbers(self):        
        self.assertEqual(calculate_expression("2000000 - 1"), 1999999)
        self.assertEqual(calculate_expression("23213 - 6549"), 16664)
        self.assertEqual(calculate_expression("2000.25 - 32332.75 - 32.7 - 3.8 "), -30369)


    def negative_numbers(self):
        self.assertEqual(calculate_expression("-3 - -6"), 3)
        self.assertEqual(calculate_expression("5 - -7"), 11)
        self.assertEqual(calculate_expression("-6 - 10"), -16)
        self.assertEqual(calculate_expression("-3.5 - 3"), -6.5)

    
    def exceptions(self):
        self.assertRaises(SyntaxError, calculate_expression("-"))
        self.assertRaises(SyntaxError, calculate_expression("10 - "))
        self.assertRaises(SyntaxError, calculate_expression("- 2"))
        self.assertRaises(SyntaxError, calculate_expression("10 - 2 -"))
        self.assertRaises(SyntaxError, calculate_expression("- 10 - 2"))
        self.assertRaises(SyntaxError, calculate_expression("10 - - 2"))


class IncrementDecrement(unittest.TestCase):
    
    def integers(self):
        self.assertEqual(calculate_expression("inc(2)"), 3)
        self.assertEqual(calculate_expression("inc(5)"), 6)

        self.assertEqual(calculate_expression("dec(2)"), 1)
        self.assertEqual(calculate_expression("dec(5)"), 4)


    def negative_numbers(self):
        self.assertEqual(calculate_expression("inc(-5)"), 4)

        self.assertEqual(calculate_expression("dec(-5)"), - 6)


    def exceptions(self):
        self.assertRaises(SyntaxError, calculate_expression("inc('This is a message')"))

        self.assertRaises(SyntaxError, calculate_expression("dec('This is a message')"))


if __name__ == '__main__':
    unittest.main()