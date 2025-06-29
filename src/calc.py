#!/usr/bin/python3

"""! @brief Package containing mathematical functions"""
##
# @section description_calc Description
# This file contains mathematical functions.
# 
# @section libraries_calc Libraries/Modules
# - re
# - functions
# - typing
#
# @section notes_calc Notes
# 
# @file calc.py
# @brief File containing mathematical functions
# @author Jozef Michal Bukas <xbukas00@stud.fit.vutbr.cz>
# @date 28.4.2022

from typing import Union
import functions
import re


def power(number: Union[float, int], exponent: Union[float, int]) -> Union[float, int]:
    """!
    @brief Function which calculates n-th power number
    @param number number to be raised
    @param exponent number by which we raise
    @return str_for_calc result of operation
    """
    str_for_calc = str(number) + "^" + str(exponent)

    str_for_calc = functions.__find_all_expressions_power_d(str_for_calc)

    error = re.findall(r"j", str_for_calc)

    if bool(error):
        raise ArithmeticError("Root of negative number while exponent is even is not defined")

    error = re.findall(r"Arithmetic error", str_for_calc)

    if bool(error):
        raise OverflowError("Result is too big")

    return float(str_for_calc)

    


def root(number: Union[int, float], root: Union[int, float]) -> Union[float, int]:
    """!
    @brief Function which calculates n-th root of number
    @param number number which will be rooted
    @param root number by which we root
    @return str_for_calc result of operation
    """
    str_for_calc = str(root) + "√" + str(number)

    str_for_calc = functions.__find_all_expressions_power_d(str_for_calc)

    error = re.findall(r"j", str_for_calc)

    if bool(error):
        raise ArithmeticError("Root of negative number while exponent is even is not defined")

    error = re.findall(r"Arithmetic error", str_for_calc)

    if bool(error):
        raise OverflowError("Result is too big")

    return str_for_calc



def factorial(number: int) -> int:
    """!
    @brief Function which calculates factorial
    @param number number from which we will calculate factorial
    @return str_for_calc result
    """
    str_for_calc = str(number) + "!"

    if number < 0:
        raise ArithmeticError("Factorial of negative number is not defined")

    str_for_calc = functions.__find_all_expressions_factorial(str_for_calc)

    error = re.findall(r"Arithmetic error", str_for_calc)

    if bool(error):
        raise OverflowError("Result is too big")

    return int(str_for_calc)


def increment(number: Union[float, int]) -> Union[float, int]:
    """!
    @brief Function which increments given number
    @param number number to be incremented
    @return str_for_calc result
    """
    str_for_calc = "inc" + str(number)

    str_for_calc = functions.__find_all_expressions_inc(str_for_calc)

    return str_for_calc


def decrement(number: Union[float, int]) -> Union[float, int]:
    """!
    @brief Function which decrements given number
    @param number number to be decremented
    @return str_for_calc result
    """
    str_for_calc = "dec" + str(number)

    str_for_calc = functions.__find_all_expressions_inc(str_for_calc)

    return str_for_calc



def multiply(number1: Union[float, int], number2: Union[float, int]) -> Union[float, int]:
    """!
    @brief Function which multiplies two numbers
    @param number1 first operand
    @param number2 second operand
    @return number1 multiplied by number2
    """
    return number1 * number2


def division(number1: Union[float, int], number2: Union[float, int]) -> Union[float, int]:
    """!
    @brief Function which devides two numbers
    @param number1 first operand
    @param number2 second operand
    @return number1 devide by number2
    """
    if not number2:
        raise ZeroDivisionError

    return number1 / number2
    