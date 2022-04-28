#!/usr/bin/python3

##
# @section description_profiling Description
# Defines GUI of calculator app and behavior of buttons.
#
# @section libraries_profiling Libraries/Modules
# - cmath python library
# - math python library
#
# @file profiling.py
# @brief
# @author Samuel Stolárik <xstola02@stud.fit.vutbr.cz>
# @date 28.4.2022

from cmath import nan
from functions import power, root
from math import sqrt


def get_input() -> list:
    """!
    @brief short description
    @return

    longer description (if needed)
    """
    try:
        input_numbers = []
        while True:
            # until eof, then input() raises exception
            input_numbers += list(map(int, input().split())) 
    except:
        return input_numbers


def avg(numbers: list) -> int:
    """!
    @brief short description
    @param numbers
    @return

    longer description (if needed)
    """
    if len(numbers) == 0:
        return int(0)
    return sum(numbers)/len(numbers)


def inside_function(numbers: list):
    """!
    @brief short description
    @param numbers
    @return

    longer description (if needed)
    """
    sum = 0
    for i in numbers:
        sum += power(i, 2)
        
    sum -= len(numbers) * power(avg(numbers), 2)
    
    return sum


def expression(numbers: list):
    """!
    @brief short description
    @param numbers
    @return

    longer description (if needed)
    """
    try:
        partial = inside_function(numbers) / (len(numbers) - 1)

    except ZeroDivisionError:
        print("ERROR: Zero division occured.")
        return nan

    try:
        return root(partial, 2)

    except ValueError:
        print("ERROR: Sqrt of negative number. Number: ", partial, ".")
        return nan
    

if __name__ == "__main__":
    input_numbers = get_input()
    print(expression(input_numbers))
