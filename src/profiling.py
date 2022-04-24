#!/usr/bin/python3

##
# @file profiling.py
# @author Samuel Stolarik
# @date 2022-04-24
# @brief mathematical function to be profiled
##

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
    sum = 0
    for i in numbers:
        sum += power(i,2)
    sum-=count * power(avg(numbers), 2)
    
    return sum


my_numbers = get_input()
print(inside_function(my_numbers, len(my_numbers)))