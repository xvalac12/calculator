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
    print(numbers)
    if len(numbers) == 0:
        return int(0)
    
    return sum(numbers)/len(numbers)

