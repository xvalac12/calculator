#!/usr/bin/python3

##
# @file profiling.py
# @author Samuel Stolarik
# @date 2022-04-24
# @brief mathematical function to be profiled
##

from functions import power, root


def avg(numbers: list) -> int:

    return sum(numbers)/len(numbers)

print(avg([4,2]))