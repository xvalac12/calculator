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
    @brief short description

    long description (if needed)
    """

    def test_small_numbers(self):
        """!
        @brief short description
        @param self

        long description (if needed)
        """
        self.assertEqual(calculate_expression("1 + 2"), 3)
        self.assertEqual(calculate_expression("1.0 +2.0"), 3)
        self.assertEqual(calculate_expression("1+2 + 3"), 6)
        self.assertEqual(calculate_expression("2 + 1"), 3)

        self.assertEqual(calculate_expression("1.5 +3.5"), 5)

    def test_large_numbers(self):
        """!
        @brief short description
        @param self

        long description (if needed)
        """
        self.assertEqual(calculate_expression("2000 + 11100000"), 11102000)
        self.assertEqual(calculate_expression("2000.0 + 11100000.0"), 11102000)
        self.assertEqual(calculate_expression("2000 + 11100000+ 3212316"), 14314316)

    def test_negative_numbers(self):
        """!
        @brief short description
        @param self

        long description (if needed)
        """
        self.assertEqual(calculate_expression("-2 + 1"), -1)
        self.assertEqual(calculate_expression("-2 + -1"), -3)
        self.assertEqual(calculate_expression("2 + -1"), 1)

        self.assertEqual(calculate_expression("-2.0 + 1.0"), -1)
        self.assertEqual(calculate_expression("-2.0 + -1.0"), -3)
        self.assertEqual(calculate_expression("2.0 + -1.0"), 1)

    def test_exceptions(self):
        """!
        @brief short description
        @param self

        long description (if needed)
        """
        self.assertTrue(calculate_expression("+").startswith("Syntax error"))
        self.assertTrue(calculate_expression("10 + ").startswith("Syntax error"))
        self.assertTrue(calculate_expression("10 + 2 +").startswith("Syntax error"))


class TestSubtraction(unittest.TestCase):
    """!
    @brief short description

    long description (if needed)
    """
    def test_small_numbers(self):
        """!
        @brief short description
        @param self

        long description (if needed)
        """
        self.assertEqual(calculate_expression("2- 1"), 1)
        self.assertEqual(calculate_expression("5 -2"), 3)
        self.assertEqual(calculate_expression("10-2 - 3 - 1"), 4)

        self.assertEqual(calculate_expression("10.5 - 2.5"), 8)

    def test_large_numbers(self):
        """!
        @brief short description
        @param self

        long description (if needed)
        """
        self.assertEqual(calculate_expression("2000000 - 1"), 1999999)
        self.assertEqual(calculate_expression("23213 - 6549"), 16664)
        self.assertEqual(calculate_expression("2000.25 - 32332.75 - 32.7 - 3.8 "), -30369)

    def test_negative_numbers(self):
        """!
        @brief short description
        @param self

        long description (if needed)
        """
        self.assertEqual(calculate_expression("-3 - -6"), 3)
        self.assertEqual(calculate_expression("5 - -7"), 12)
        self.assertEqual(calculate_expression("-6 - 10"), -16)
        self.assertEqual(calculate_expression("-3.5 - 3"), -6.5)

    def test_exceptions(self):
        """!
        @brief short description
        @param self

        long description (if needed)
        """
        self.assertTrue(calculate_expression("-").startswith("Syntax error"))
        self.assertTrue(calculate_expression("10 - ").startswith("Syntax error"))
        self.assertTrue(calculate_expression("10 - 2 -").startswith("Syntax error"))


class IncrementDecrement(unittest.TestCase):
    """!
    @brief short description

    long description (if needed)
    """
    def test_integers(self):
        """!
        @brief short description
        @param self

        long description (if needed)
        """
        self.assertEqual(calculate_expression("inc2"), 3)
        self.assertEqual(calculate_expression("inc5"), 6)

        self.assertEqual(calculate_expression("dec2"), 1)
        self.assertEqual(calculate_expression("dec5"), 4)

    def test_negative_numbers(self):
        """!
        @brief short description
        @param self

        long description (if needed)
        """
        self.assertEqual(calculate_expression("inc-5"), -4)

        self.assertEqual(calculate_expression("dec-5"), - 6)

    def test_exceptions(self):
        """!
        @brief short description
        @param self

        long description (if needed)
        """
        self.assertTrue(calculate_expression("inc").startswith("Syntax error"))

        self.assertTrue(calculate_expression("dec").startswith("Syntax error"))


class TestMultiplication(unittest.TestCase):
    """!
    @brief short description

    long description (if needed)
    """
    def test_integers(self):
        """!
        @brief short description
        @param self

        long description (if needed)
        """
        self.assertEqual(calculate_expression("2 * 2"), 4)
        self.assertEqual(calculate_expression("3*7"), 21)
        self.assertEqual(calculate_expression("5 *5"), 25)
        self.assertEqual(calculate_expression("3* 7"), 21)

        self.assertEqual(calculate_expression("0 * 7"), 0)
        self.assertEqual(calculate_expression("3 * 0"), 0)

    def test_negative_numbers(self):
        """!
        @brief short description
        @param self

        long description (if needed)
        """
        self.assertEqual(calculate_expression("2 * -2"), -4)
        self.assertEqual(calculate_expression("-3*7"), -21)
        self.assertEqual(calculate_expression("-5 *-5"), 25)
        self.assertEqual(calculate_expression("3* -7"), -21)


class TestDivision(unittest.TestCase):
    """!
    @brief short description

    long description (if needed)
    """
    def test_integers(self):
        """!
        @brief short description
        @param self

        long description (if needed)
        """
        self.assertEqual(calculate_expression("2 / 2"), 1)
        self.assertEqual(calculate_expression("21/7"), 3)
        self.assertEqual(calculate_expression("5 /5"), 1)
        self.assertEqual(calculate_expression("14/ 7"), 2)

        self.assertEqual(calculate_expression("0 / 7"), 0)

    def test_negative_numbers(self):
        """!
        @brief short description
        @param self

        long description (if needed)
        """
        self.assertEqual(calculate_expression("2 / -2"), -1)
        self.assertEqual(calculate_expression("-21/7"), -3)
        self.assertEqual(calculate_expression("-5 /-5"), 1)
        self.assertEqual(calculate_expression("14/ -7"), -2)

    def test_exceptions(self):
        """!
        @brief short description
        @param self

        long description (if needed)
        """
        self.assertTrue(calculate_expression("3 / 0").startswith("Arithmetic error"))


class TestPower(unittest.TestCase):
    """!
    @brief short description

    long description (if needed)
    """
    def test_integers(self):
        """!
        @brief short description
        @param self

        long description (if needed)
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
        @brief short description
        @param self

        long description (if needed)
        """
        self.assertEqual(calculate_expression("2 ^ -1"), 0.5)
        self.assertEqual(calculate_expression("-4^3"), -64)
        self.assertEqual(calculate_expression("-5 ^-1"), -0.2)


class TestRoot(unittest.TestCase):
    """!
    @brief short description

    long description (if needed)
    """
    def test_integers(self):
        """!
        @brief short description
        @param self

        long description (if needed)
        """
        self.assertEqual(calculate_expression("2 √ 4"), 2)
        self.assertEqual(calculate_expression("3√8"), 2)
        self.assertEqual(calculate_expression("4√ 256"), 4)
        self.assertEqual(calculate_expression("1 √3"), 3)
        self.assertEqual(calculate_expression("2 √ 0"), 0)

    def test_negative_numbers(self):
        """!
        @brief short description
        @param self

        long description (if needed)
        """
        self.assertEqual(calculate_expression("-2 √ 4"), 0.5)
        self.assertEqual(calculate_expression("3√-8"), -2)
        self.assertEqual(calculate_expression("-3 √ -8"), -0.5)

    def test_exceptions(self):
        """!
        @brief short description
        @param self

        long description (if needed)
        """
        self.assertTrue(calculate_expression("2000√-4").startswith("Arithmetic error"))
        self.assertTrue(calculate_expression("0√4").startswith("Syntax error"))


class TestFactorial(unittest.TestCase):
    """!
    @brief short description

    long description (if needed)
    """
    def test_integers(self):
        """!
        @brief short description
        @param self

        long description (if needed)
        """
        self.assertEqual(calculate_expression("2!"), 2)
        self.assertEqual(calculate_expression("5!"), 120)

    def test_exceptions(self):
        self.assertTrue(calculate_expression("-5!").startswith("Arithmetic error"))
        self.assertTrue(calculate_expression("2!5").startswith("Syntax error"))


class Exceptions(unittest.TestCase):
    """!
    @brief short description

    long description (if needed)
    """
    def test_syntax(self):
        """!
        @brief short description
        @param self

        long description (if needed)
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
    @brief short description

    long description (if needed)
    """

    # We're not testing for randomness we don't have the proper tools.
    # Nor are we required to.
    def test_returns(self):
        """!
        @brief short description
        @param self

        long description (if needed)
        """
        self.assertEqual(type(get_random_number()), int)


if __name__ == '__main__':
    unittest.main()
# "In this you rejoice, though now for a little while, if necessary, you have been grieved by various trials"
# - 1 Peter 1:6
