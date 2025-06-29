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


def inside_function(numbers:list, count:int):
    if len(numbers) < count:
        raise(IndexError)

    sum = 0
    for i in numbers[0:count]:
        sum += power(i,2)
        
    sum-=len(numbers) * power(avg(numbers), 2)
    
    return sum


def expresion(numbers:list, count:int):
    try:
        partial = inside_function(numbers, count) / (len(numbers) - 1)

    except IndexError:
        print("ERROR: Not enough numbers for profiling. Required: ", count,". Got: ", len(numbers), ".")
        return nan

    except ZeroDivisionError:
        print("ERROR: Zero division occured.")
        return nan

    result = 0
    try:
        return sqrt(partial)

    except ValueError:
        print("ERROR: Sqrt of negative number. Number: ", partial,".")
        return nan
    

if __name__ == "__main__":
    input_numbers = get_input()
    print(expresion(input_numbers, 10))
    print(expresion(input_numbers, 100))
    print(expresion(input_numbers, 1000))
