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
        self.assertEqual(calculate_expression("inc2"), 3)
        self.assertEqual(calculate_expression("inc5"), 6)

        self.assertEqual(calculate_expression("dec2"), 1)
        self.assertEqual(calculate_expression("dec5"), 4)


    def negative_numbers(self):
        self.assertEqual(calculate_expression("inc-5"), 4)

        self.assertEqual(calculate_expression("dec-5"), - 6)


    def exceptions(self):
        self.assertRaises(SyntaxError, calculate_expression("inc"))

        self.assertRaises(SyntaxError, calculate_expression("dec"))


class TestMultiplication(unittest.TestCase):
    
    def integers(self):
        self.assertEqual(calculate_expression("2 * 2"), 4)
        self.assertEqual(calculate_expression("3*7"), 21)
        self.assertEqual(calculate_expression("5 *5"), 25)
        self.assertEqual(calculate_expression("3* 7"), 21)
        
        self.assertEqual(calculate_expression("0 * 7"), 0)
        self.assertEqual(calculate_expression("3 * 0"), 0)


    def negative_numbers(self):
        self.assertEqual(calculate_expression("2 * -2"), -4)
        self.assertEqual(calculate_expression("-3*7"), -21)
        self.assertEqual(calculate_expression("-5 *-5"), 25)
        self.assertEqual(calculate_expression("3* -7"), -21)
    

class TestDivision(unittest.TestCase):
    def integers(self):
        self.assertEqual(calculate_expression("2 / 2"), 1)
        self.assertEqual(calculate_expression("21/7"), 3)
        self.assertEqual(calculate_expression("5 /5"), 1)
        self.assertEqual(calculate_expression("14/ 7"), 2)

        self.assertEqual(calculate_expression("0 / 7"), 0)


    def negative_numbers(self):
        self.assertEqual(calculate_expression("2 / -2"), -1)
        self.assertEqual(calculate_expression("-21/7"), -3)
        self.assertEqual(calculate_expression("-5 /-5"), 1)
        self.assertEqual(calculate_expression("14/ -7"), -2)


    def exceptions(self):
        self.assertRaises(ArithmeticError, calculate_expression("3 / 0"))


class TestPower(unittest.TestCase):
    def integers(self):
        self.assertEqual(calculate_expression("2 ^ 1"), 2)
        self.assertEqual(calculate_expression("3^3"), 27)
        self.assertEqual(calculate_expression("1 ^28964"), 1)
        self.assertEqual(calculate_expression("2 ^3"), )

        self.assertEqual(calculate_expression("0 ^ 7"), 0)
        self.assertEqual(calculate_expression("1 ^ 0"), 1)
        self.assertEqual(calculate_expression("0 ^ 0"), 1)

        self.assertEqual(calculate_expression("4^0.5"), 2)


    def negative_numbers(self):
        self.assertEqual(calculate_expression("2 ^ -1"), -0.5)
        self.assertEqual(calculate_expression("-4^3"), -64)
        self.assertEqual(calculate_expression("-5 ^-1"), -0.2)
        self.assertEqual(calculate_expression("-4^ 0.5"), 2)


class TestRoot(unittest.TestCase):
    def integers(self):
        self.assertEqual(calculate_expression("2 √ 4"), 2)
        self.assertEqual(calculate_expression("3√16"), 2)
        self.assertEqual(calculate_expression("4√ 256"), 4)
        self.assertEqual(calculate_expression("1 √3"), 3)
        self.assertEqual(calculate_expression("2 √ 0"), 0)


    def negative_numbers(self):
        self.assertEqual(calculate_expression("-2 √ 4"), 0.5)
        self.assertEqual(calculate_expression("3√-8"), -2)
        self.assertEqual(calculate_expression("-3 √ -8"), 0.25)
    

    def exceptions(self):
        self.assertRaises(ArithmeticError, calculate_expression("2000√-4"))
        self.assertRaises(ArithmeticError, calculate_expression("0√4"))


class TestFactorial(unittest.TestCase):
    def integers(self):
        self.assertEqual(calculate_expression("2!"), 2)
        self.assertEqual(calculate_expression("5!"), 120)
    

    def exceptions(self):
        self.assertRaises(SyntaxError, calculate_expression("-5!"))
        self.assertRaises(SyntaxError, calculate_expression("2!5"))


class Excpeptions(unittest.TestCase):
    def syntax(self):
        
        # Lone symbols
        self.assertRaises(SyntaxError, calculate_expression("+"))
        self.assertRaises(SyntaxError, calculate_expression("-"))
        
        # Hanging symbols
        self.assertRaises(SyntaxError, calculate_expression("+ 2 + 5"))
        self.assertRaises(SyntaxError, calculate_expression("5 * 6 /"))

        # Repating symbols
        self.assertRaises(SyntaxError, calculate_expression("2 + + 5"))
        self.assertRaises(SyntaxError, calculate_expression("5!!"))

        # Text
        self.assertRaises(SyntaxError, calculate_expression("Heyo"))
        self.assertRaises(SyntaxError, calculate_expression("increment"))
        self.assertRaises(SyntaxError, calculate_expression("Minca"))
        self.assertRaises(SyntaxError, calculate_expression("codec"))



if __name__ == '__main__':
    unittest.main()
# "In this you rejoice, though now for a little while, if necessary, you have been grieved by various trials"
# - 1 Peter 1:6
