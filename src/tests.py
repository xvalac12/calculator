"""! @brief Tests for our library"""
##
# @section description_tests Description
# Test for our library
#
# @section libraries_test Libraries/Modules
# - unittest
# - functions
#
# @file tests.py
# @brief tests
# @author Adam Bezak <xbezak02@stud.fit.vutbr.cz>
# @date 28.4.2022

import unittest
from functions import calculate_expression, get_random_number


class TestAddition(unittest.TestCase):
    """!
    @brief Tests for simple addition
    """

    def test_small_numbers(self):
        """!
        @brief Tests for addition with small integers. Using both floats and ints.
        """
        self.assertEqual(calculate_expression("1 + 2"), 3)
        self.assertEqual(calculate_expression("1.0 +2.0"), 3)
        self.assertEqual(calculate_expression("1+2 + 3"), 6)
        self.assertEqual(calculate_expression("2 + 1"), 3)

        self.assertEqual(calculate_expression("1.5 +3.5"), 5)

    def test_large_numbers(self):
        """!
        @brief Testing addition with large integers
        """
        self.assertEqual(calculate_expression("2000 + 11100000"), 11102000)
        self.assertEqual(calculate_expression("2000.0 + 11100000.0"), 11102000)
        self.assertEqual(calculate_expression("2000 + 11100000+ 3212316"), 14314316)

    def test_negative_numbers(self):
        """!
        @brief Testing if addition works with negative numbers
        """
        self.assertEqual(calculate_expression("-2 + 1"), -1)
        self.assertEqual(calculate_expression("-2 + -1"), -3)
        self.assertEqual(calculate_expression("2 + -1"), 1)

        self.assertEqual(calculate_expression("-2.0 + 1.0"), -1)
        self.assertEqual(calculate_expression("-2.0 + -1.0"), -3)
        self.assertEqual(calculate_expression("2.0 + -1.0"), 1)

    def test_exceptions(self):
        """!
        @brief Testing if hanging symbols are properly dealt with
        """
        self.assertTrue(calculate_expression("+").startswith("Syntax error"))
        self.assertTrue(calculate_expression("10 + ").startswith("Syntax error"))
        self.assertTrue(calculate_expression("10 + 2 +").startswith("Syntax error"))


class TestSubtraction(unittest.TestCase):
    """!
    @brief Tests for simple subtraction
    """
    def test_small_numbers(self):
        """!
        @brief Testing subtraction using small numbers
        """
        self.assertEqual(calculate_expression("2- 1"), 1)
        self.assertEqual(calculate_expression("5 -2"), 3)
        self.assertEqual(calculate_expression("10-2 - 3 - 1"), 4)

        self.assertEqual(calculate_expression("10.5 - 2.5"), 8)

    def test_large_numbers(self):
        """!
        @breif Testing subtraction using large numbers
        """
        self.assertEqual(calculate_expression("2000000 - 1"), 1999999)
        self.assertEqual(calculate_expression("23213 - 6549"), 16664)
        self.assertEqual(calculate_expression("2000.25 - 32332.75 - 32.7 - 3.8 "), -30369)

    def test_negative_numbers(self):
        """!
        @breif Testing if subtraction works with negative numbers
        """
        self.assertEqual(calculate_expression("-3 - -6"), 3)
        self.assertEqual(calculate_expression("5 - -7"), 12)
        self.assertEqual(calculate_expression("-6 - 10"), -16)
        self.assertEqual(calculate_expression("-3.5 - 3"), -6.5)

    def test_exceptions(self):
        """!
        @brief Testing if subtraction raises exceptions in the correct circumstances
        """
        self.assertTrue(calculate_expression("-").startswith("Syntax error"))
        self.assertTrue(calculate_expression("10 - ").startswith("Syntax error"))
        self.assertTrue(calculate_expression("10 - 2 -").startswith("Syntax error"))


class IncrementDecrement(unittest.TestCase):
    """!
    @brief Tests on the increment and decrement operations
    """
    def test_integers(self):
        """!
        @brief Testing increment and decrement using small numbers
        """
        self.assertEqual(calculate_expression("inc2"), 3)
        self.assertEqual(calculate_expression("inc5"), 6)
        self.assertEqual(calculate_expression("incinc5"), 7)

        self.assertEqual(calculate_expression("dec2"), 1)
        self.assertEqual(calculate_expression("dec5"), 4)
        self.assertEqual(calculate_expression("decdec5"), 3)
        self.assertEqual(calculate_expression("decinc5"), 5)

    def test_negative_numbers(self):
        """!
        @brief Testing increment and decrement using negative numbers
        """
        self.assertEqual(calculate_expression("inc-5"), -4)

        self.assertEqual(calculate_expression("dec-5"), - 6)

    def test_exceptions(self):
        """!
        @brief Testing if increment and decrement raise exceptions in the proper circumstances
        """
        self.assertTrue(calculate_expression("inc").startswith("Syntax error"))

        self.assertTrue(calculate_expression("dec").startswith("Syntax error"))


class TestMultiplication(unittest.TestCase):
    """!
    @brief Tests on multiplication
    """
    def test_integers(self):
        """!
        @brief Testing multiplication with small integers
        """
        self.assertEqual(calculate_expression("2 * 2"), 4)
        self.assertEqual(calculate_expression("3*7"), 21)
        self.assertEqual(calculate_expression("5 *5"), 25)
        self.assertEqual(calculate_expression("3* 7"), 21)

        self.assertEqual(calculate_expression("0 * 7"), 0)
        self.assertEqual(calculate_expression("3 * 0"), 0)

    def test_negative_numbers(self):
        """!
        @brief Testing multiplication with negative numbers
        """
        self.assertEqual(calculate_expression("2 * -2"), -4)
        self.assertEqual(calculate_expression("-3*7"), -21)
        self.assertEqual(calculate_expression("-5 *-5"), 25)
        self.assertEqual(calculate_expression("3* -7"), -21)


class TestDivision(unittest.TestCase):
    """!
    @brief Tests on division
    """
    def test_integers(self):
        """!
        @brief Testing division with whole numbers
        """
        self.assertEqual(calculate_expression("2 / 2"), 1)
        self.assertEqual(calculate_expression("21/7"), 3)
        self.assertEqual(calculate_expression("5 /5"), 1)
        self.assertEqual(calculate_expression("14/ 7"), 2)

        self.assertEqual(calculate_expression("0 / 7"), 0)

    def test_negative_numbers(self):
        """!
        @brief Testing division with negative numbers
        """
        self.assertEqual(calculate_expression("2 / -2"), -1)
        self.assertEqual(calculate_expression("-21/7"), -3)
        self.assertEqual(calculate_expression("-5 /-5"), 1)
        self.assertEqual(calculate_expression("14/ -7"), -2)

    def test_exceptions(self):
        """!
        @brief Testing if we properly catch division by zero
        """
        self.assertTrue(calculate_expression("3 / 0").startswith("Arithmetic error"))


class TestPower(unittest.TestCase):
    """!
    @brief Tests on power operation
    """
    def test_positive_numbers(self):
        """!
        @brief Testing if power works in most cases for positive numbers
        """
        self.assertEqual(calculate_expression("2 ^ 1"), 2)
        self.assertEqual(calculate_expression("3^3"), 27)
        self.assertEqual(calculate_expression("1 ^28964"), 1)
        self.assertEqual(calculate_expression("2 ^3"), 8)

        self.assertEqual(calculate_expression("0 ^ 7"), 0)
        self.assertEqual(calculate_expression("1 ^ 0"), 1)
        self.assertEqual(calculate_expression("0 ^ 0"), 1)

        self.assertEqual(calculate_expression("4^0.5"), 2)

    def test_negative_numbers(self):
        """!
        @brief Testing if power works properly with negative numbers
        """
        self.assertEqual(calculate_expression("2 ^ -1"), 0.5)
        self.assertEqual(calculate_expression("-4^3"), -64)
        self.assertEqual(calculate_expression("-5 ^-1"), -0.2)


class TestRoot(unittest.TestCase):
    """!
    @brief Tests for the root operation
    """
    def test_integers(self):
        """!
        @brief Testing the root operation with simple integers
        """
        self.assertEqual(calculate_expression("2 √ 4"), 2)
        self.assertEqual(calculate_expression("3√8"), 2)
        self.assertEqual(calculate_expression("4√ 256"), 4)
        self.assertEqual(calculate_expression("1 √3"), 3)
        self.assertEqual(calculate_expression("2 √ 0"), 0)

    def test_negative_numbers(self):
        """!
        @brief Testing if the root operation correctly deals with negative numbers
        """
        self.assertEqual(calculate_expression("-2 √ 4"), 0.5)
        self.assertEqual(calculate_expression("3√-8"), -2)
        self.assertEqual(calculate_expression("-3 √ -8"), -0.5)

    def test_exceptions(self):
        """!
        @brief Testing if root properly catches errors
        """
        self.assertTrue(calculate_expression("2000√-4").startswith("Arithmetic error"))
        self.assertTrue(calculate_expression("0√4").startswith("Syntax error"))


class TestFactorial(unittest.TestCase):
    """!
    @brief Testing the factorial operation
    """
    def test_integers(self):
        """!
        @brief Testing factorial on simple integers
        """
        self.assertEqual(calculate_expression("2!"), 2)
        self.assertEqual(calculate_expression("5!"), 120)

    def test_exceptions(self):
        """!
        @brief Testing if factorial correctly deals with negative numbers
        """
        self.assertTrue(calculate_expression("-5!").startswith("Arithmetic error"))
        self.assertTrue(calculate_expression("2!5").startswith("Syntax error"))


class Exceptions(unittest.TestCase):
    """!
    @brief Tests for finding all the edge cases
    """
    def test_syntax(self):
        """!
        @brief Testing if we properly catch syntax errors
        """
        # Lone symbols
        self.assertTrue(calculate_expression("+").startswith("Syntax error"))
        self.assertTrue(calculate_expression("-").startswith("Syntax error"))

        # Hanging symbols
        self.assertTrue(calculate_expression("5 * 6 /").startswith("Syntax error"))

        # Repeating symbols
        self.assertTrue(calculate_expression("5!!").startswith("Syntax error"))

        # Text
        self.assertTrue(calculate_expression("Heyo").startswith("Syntax error"))
        self.assertTrue(calculate_expression("increment").startswith("Syntax error"))
        self.assertTrue(calculate_expression("Minca").startswith("Syntax error"))
        self.assertTrue(calculate_expression("codec").startswith("Syntax error"))


class TestRandomness(unittest.TestCase):
    """!
    @brief Tests for the get_random_number function
    """

    def test_returns(self):
        """!
        @brief Testing if get_random_number returns an int

        We can't properly test randomness as that would take too long.
        Considering that the random number generator under the hood is a combination of multiple lcgs,
        a bruteforce periodicity test would take hours.
        """
        self.assertEqual(type(get_random_number()), int)


if __name__ == '__main__':
    unittest.main()
# "In this you rejoice, though now for a little while, if necessary, you have been grieved by various trials"
# - 1 Peter 1:6
