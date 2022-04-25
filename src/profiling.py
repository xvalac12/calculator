#!/usr/bin/python3

##
# @file profiling.py
# @author Samuel Stolarik
# @date 2022-04-24
# @brief mathematical function to be profiled
##

from cmath import nan
from functions import power, root
from math import sqrt

def get_input() -> list:
    try:
        input_numbers = []
        while(True):
            #until eof, then input() raises exception
            input_numbers += list(map(int,input().split())) 
    except:
        return input_numbers


def avg(numbers: list) -> int:
    if len(numbers) == 0:
        return int(0)
    return sum(numbers)/len(numbers)


def inside_function(numbers:list):
    sum = 0
    for i in numbers:
        sum += power(i,2)
        
    sum-=len(numbers) * power(avg(numbers), 2)
    
    return sum


def expresion(numbers:list):
    try:
        partial = inside_function(numbers) / (len(numbers) - 1)

    except ZeroDivisionError:
        print("ERROR: Zero division occured.")
        return nan

    try:
        return root(partial, 2)

    except ValueError:
        print("ERROR: Sqrt of negative number. Number: ", partial,".")
        return nan
    

if __name__ == "__main__":
    input_numbers = get_input()
    print(expresion(input_numbers))
