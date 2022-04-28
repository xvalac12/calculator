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
    @brief short description
    @param number
    @param exponent
    @return
    long description (if needed)
    """
    str_for_calc = str(number) + "^" + str(exponent)

    str_for_calc = functions.__find_all_expressions_power_d(str_for_calc)

    error = re.findall(r"j", str_for_calc)

    if bool(error):
        raise ArithmeticError("Root of negative number while exponent is even is not defined")

    return float(str_for_calc)


def root(number: Union[int, float], root: Union[int, float]) -> Union[float, int]:
    """!
    @brief short description
    @param number
    @param root
    @return
    long description (if needed)
    """
    str_for_calc = str(root) + "√" + str(number)

    str_for_calc = functions.__find_all_expressions_power_d(str_for_calc)

    error = re.findall(r"j", str_for_calc)

    if bool(error):
        raise ArithmeticError("Root of negative number while exponent is even is not defined")

    return str_for_calc


def factorial(number: int) -> int:
    """!
    @brief short description
    @param number
    @return
    long description (if needed)
    """
    str_for_calc = str(number) + "!"

    if number < 0:
        raise ArithmeticError("Factorial of negative number is not defined")

    str_for_calc = functions.__find_all_expressions_factorial(str_for_calc)

    return int(str_for_calc)


def increment(number: Union[float, int]) -> Union[float, int]:
    """!
    @brief short description
    @param number
    @return
    long description (if needed)
    """
    str_for_calc = "inc" + str(number)

    str_for_calc = functions.__find_all_expressions_inc(str_for_calc)

    return str_for_calc


def decrement(number: Union[float, int]) -> Union[float, int]:
    """!
    @brief short description
    @param number
    @return
    long description (if needed)
    """
    str_for_calc = "dec" + str(number)

    str_for_calc = functions.__find_all_expressions_inc(str_for_calc)

    return str_for_calc


def multiply(number1: Union[float, int], number2: Union[float, int]) -> Union[float, int]:
    """!
    @brief short description
    @param number1
    @param number2
    @return
    long description (if needed)
    """
    return number1 * number2


def division(number1: Union[float, int], number2: Union[float, int]) -> Union[float, int]:
    """!
    @brief short description
    @param number1
    @param number2
    @return
    long description (if needed)
    """
    if not number2:
        raise ZeroDivisionError

    return number1 / number2

