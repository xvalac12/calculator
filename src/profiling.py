#!/usr/bin/python3

"""! @brief Package containing profiling of math library"""
##
# @section description_profiling Description
# Defines GUI of calculator app and behavior of buttons.
#
# @section libraries_profiling Libraries/Modules
# - cmath python library
# - math python library
#
# @file profiling.py
# @brief calcalating standard deviation for mathematical library profiling purposes
# @author Samuel Stolárik <xstola02@stud.fit.vutbr.cz>
# @date 28.4.2022

from cmath import nan
from calc import root, power

def get_input() -> list:
    """!
    @brief function to read unlimited amount of whitespace separated numbers from stdin
    @return list of numbers
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
    @brief calculate average value from @p numbers 
    @param numbers
    @return calculated value
    """
    if len(numbers) == 0:
        return int(0)
    return sum(numbers)/len(numbers)


def inside_function(numbers: list):
    """!
    @brief first part of the function to calculate the standard deviation
    @param numbers
    @return
    """
    sum = 0
    for i in numbers:
        sum += power(i, 2)
        
    sum -= len(numbers) * power(avg(numbers), 2)
    
    return sum



def expression(numbers: list):
    """!
    @brief calculate the whole standard deviation function of @p numbers
    @param numbers
    @return
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

