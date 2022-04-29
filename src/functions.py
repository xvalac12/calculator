#!/usr/bin/python3

"""! @brief Package containing functions for calculator G.I.T.T."""
##
# @section description_functions Description
# This file contains mathematical functions
# for calculator G.I.T.T.
# All internal functions were build around
# needs of calculator. That is why most functions
# operate with strings. Simple functions like
# root() from calc.py use only functions they need to calculate
# right return value. Because of that it is recommended
# to use those because they are quicker.
#
# @section libraries_functions Libraries/Module
# - re
# - string
# - typing
# - time
#
# @section notes_functions Notes
#
# @file functions.py
# @brief File containing functions for calculator G.I.T.T.
# @author Jozef Michal Bukas <xbukas00@stud.fit.vutbr.cz>
# @date 28.4.2022
import time
import re
import string
from typing import Union, Generator, List


def __funct(string_for_eval):
    """!
    @brief Function which calculates basic oprations
    @param string_for_eval string with expression
    @return value value of calculated expression
    """
    value = eval(string_for_eval)

    return value


# function which finds and calculates power and root
def __find_all_expressions_power_d(string_for_change: str) -> str:
    """!
    @brief Function which finds and calculates power and root
    @param string_for_change string with expression
    @return string_for_change string with evaluated root or power

    This function finds only last occurence of symbol
    '^' and '√'. After that it calculates this expression
    and replaces substring "n^n" with calculated value.
    """
    string_list = re.findall(r" *[\^√] *", string_for_change)  # check if there are any desired symbols in string

    if not bool(string_list):
        return string_for_change

    string_for_change = "".join(
        reversed(string_for_change))  # string is reversed because I want to look for last occurrence of symbol

    try:
        # this regex must be read backwards. It is backwards because I need to look for the most inner symbol, so it
        # will be mathematically correct this regex looks for symbols ^ and √ . Then it cuts it from string with all
        # operands. It must be in try because there are two types of string which I look for. If this regex finds
        # nothing it throws exception which would ruin whole calculation

        substr = re.search(r"(?:\d+\.\d*|\d+) *[-\+]? *[\^√] *(?:\d+\.\d*|\d+) *[-\+]{1} *(?:\D|$)",
                           string_for_change).group()

        substr = "".join(reversed(substr))

        found = re.findall(r" *[-\+\*\\]{1} *[\+-]{1}",
                           substr)  # if first operand is negative number I need to strip substr from previous sign

        if bool(found):
            substr = re.sub(r"(?:\D|^)", "", substr, 1)

    except AttributeError:
        substr = ""

    if substr == "":

        try:
            substr = re.search(r"(?:\d+\.\d*|\d+) *[-\+]? *[\^√] *(?:\d+\.\d*|\d+)", string_for_change).group()
            # search is used to find first occurrence
            # this may proof inefficient, and it is but
            # while it tried to be fast it has also taken
            # shortcut which wasn't mathematically correct
        except AttributeError:

            string_for_change = "".join(reversed(string_for_change))

            return string_for_change

        substr = "".join(reversed(substr))

    if "^" in substr:

        nums = re.split(" *\^ *", substr)  # taking operands for calculation

        try:
            num = float(nums[0]) ** float(nums[1])

        except OverflowError:

            return "Arithmetic error"

        substr = "".join(reversed(substr))
        num = "".join(reversed(str(num)))

        string_for_change = string_for_change.replace(substr, str(num), 1)  # replacing substring with value

    else:

        nums = re.split(" *√ *", substr)  # splitting expression into two parts
        negative = False
        is_not_even = float(nums[0]) % 2

        try:
            exponent = (1 / float(nums[0]))

        except ZeroDivisionError:

            return "Syntax error"

        number = float(nums[1])

        if number < 0 and bool(is_not_even):
            negative = True
            number *= -1

        try:
            root = number ** exponent
        except OverflowError:

            return "Arithmetic error"

        if negative & bool(is_not_even):
            root *= -1

        substr = "".join(reversed(substr))
        root = "".join(reversed(str(root)))

        string_for_change = string_for_change.replace(substr, str(root), 1)


    string_for_change = "".join(reversed(string_for_change))

    return string_for_change


# function to change power symbol into string able to be processed by eval function
def __convert_to_evaluate_power(string_for_change: str) -> str:
    """!
    @brief Function which calls __find_all_expressions_power_d until there are no symbols left
    @param string_for_change string with expression
    @return string_for_chnage string with evaluated power and root symbols
    """
    while string_for_change != __find_all_expressions_power_d(string_for_change):
        string_for_change = __find_all_expressions_power_d(string_for_change)

    return string_for_change  


# function which calculates factorial 
def __factorial_function(number: int) -> int:
    """!
    @brief Simple recursive function which calculates factorial 
    @param number operand for factorial
    @return number multiplied by factorial of number - 1
    """
    if number == 0:
        return 1

    return number * __factorial_function(number - 1)


# function which finds all ! symbols and replaces it with number
def __find_all_expressions_factorial(string_for_change: str) -> str:
    """!
    @brief Function which finds all '!' symbols and replaces them with value
    @param string_for_change string with expression
    @return string_for_change string with calculated factorials
    """
    string_list = re.findall(r"(?:\d+|\d+\.\d*) *!", string_for_change)

    for num in string_list:

        num_replaced = num.replace("!", "")
        if int(num_replaced) > 170:
            return "Arithmetic error"

        num_replaced = __factorial_function(int(float(num_replaced)))

        string_for_change = string_for_change.replace(num, str(num_replaced))

    return string_for_change


# function which calls function for factorial evaluation
def __convert_to_evaluable_factorial(string_for_change: str) -> str:
    """!
    @brief Function which calls function for factorial evaluation
    @param string_for_change string with expression
    @return string with all factorial opertors evaluated
    """
    return __find_all_expressions_factorial(string_for_change)


# function which finds all inc symbols and replaces them with number
def __find_all_expressions_inc(string_for_change: str) -> str:
    """!
    @brief Function which finds all "inc" and "dec" symbols and replaces them with number
    @param string_for_change string with expression
    @return string_for_change string with evaluated inc or dec symbol

    This function looks for most inner occurence of
    symbols "inc/dec". Also it replaces only first occurence
    of given symbol because otherwise there would be
    inputs which would caused this function to malfunction.
    """
    string_for_change = "".join(reversed(string_for_change))  # string is reversed to look for most inner occurrence
    # also, it had tendency to change incorrect substrings
    # this is the safest way

    string_list = re.findall(r"\d+[-]?cni|\d+[-]?ced", string_for_change)

    string_for_change = "".join(reversed(string_for_change))

    for num in string_list:

        num = "".join(reversed(num))

        if "inc" in num:
            num_replaced = num.replace("inc", "")
            num_replaced = int(num_replaced) + 1

        else:
            num_replaced = num.replace("dec", "")
            num_replaced = int(num_replaced) - 1

        # replaces dec or inc with value, search depends on which operand was calculated
        string_for_change = re.sub(rf"%s\b((?:[^0-9]|\Z))" % num, r"%s\1" % str(num_replaced), string_for_change,
                                   re.IGNORECASE)

    return string_for_change


# function which calls functions for evaluation of inc and dec symbol 
def __convert_to_evaluable_inc(string_for_change: str) -> str:
    """!
    @brief Function which calls __convert_to_evaluable_inc until there are no symbols left
    @param string_for_change string with expression
    @return string_for_change string with all inc and dec symbols evaluated
    """
    while string_for_change != __find_all_expressions_inc(string_for_change):
        string_for_change = __find_all_expressions_inc(string_for_change)

    return string_for_change


def __replace_irrational_numbers(string_for_change: str) -> str:
    """!
    @brief Function which replaces constants with their aproximated value
    @param string_for_change string with expression
    @return string_for_change string with replaced irrational constants
    """
    string_for_change = string_for_change.replace("dec", "Q")

    string_for_change = string_for_change.replace("e", "2.7182818")

    string_for_change = string_for_change.replace("Q", "dec")

    string_for_change = string_for_change.replace("π", "3.14159265359")

    return string_for_change


# function which checks for invalid patterns in string before calculation
def __string_control(string_for_control: str) -> str:
    """!
    @brief Function which checks for invalid patterns in string before calculation
    @param string_for_control string with expression
    @return string contianing expression or error message 

    During this control all irrational numbers are replaced 
    with their aproximation. This must be done because nearly all
    regular expressions look for symbols like 'e' which would have
    caused nearly all expressions to be marked as syntax error.
    """
    string_list = re.findall(r"(?:\d *(?:e|π)|(?:e|π) *\d)", string_for_control)  # number before or after constants

    string_for_control = __replace_irrational_numbers(
        string_for_control)  # replacing so that symbols won't interfere with other controls

    string_list += re.findall(r"(?: +\.\d|\d\. )", string_for_control)  # space on one side of '.'

    string_list += re.findall(r"(?:(?:\D|^) *\.|\. *(?:\D|$))",
                              string_for_control)  # missing number before or after '.'

    string_list1 = re.findall(r"(?:\D|^) *- *\d+!", string_for_control)  # factorial of negative number

    string_list += re.findall(r"(?:inc|dec) ", string_for_control)  # space after inc or dec

    string_list += re.findall(r"\d *(?:inc|dec)", string_for_control)  # no operand before inc or dec

    string_list += re.findall(r"! *(?:inc|dec)", string_for_control)  # inc or dec operand after '!'

    string_list += re.findall(r"(?:inc|dec) *(?:\^|√)",
                              string_for_control)  # inc or dec operand without number before '^' or '√'

    string_list += re.findall(r"(?:! *\d| !)", string_for_control)  # no operand after '!' and space before '!'

    string_list += re.findall(r"\D *! *\D", string_for_control)  # '!' between two operands

    string_list += re.findall(r"(?:\D|^) *!", string_for_control)  # '!' at beginning without number

    string_list1 += re.findall(r"\d+\.\d+!", string_for_control)  # factorial of fraction

    string_list += re.findall(r"(?:[-\+\*\\]{1}|^) *(?:√|\^)",
                              string_for_control)  # missing or invalid first operand for '^' and '√'

    string_list += re.findall(r"[\^√]{1} *[-\+\*\\]{1} *[-\+\*\\]",
                              string_for_control)  # missing or invalid operand after '^' and '√'

    if bool(string_list):
        return "Syntax error: " + string_list[0]

    if bool(string_list1):
        return "Arithmetic error: " + string_list1[0]

    return string_for_control


def calculate_expression(str_for_calc: str) -> str:
    """!
    @brief Function which calls all necessary functions for calculation
    @param str_for_calc string with expression
    @return eval_string result of expression or error message

    Function which takes string from gui and returns
    its value. Also it can return string which indicates
    error which might have occured during calculation.
    There is chain of actions in which expression is calculated.
    This has created priority list for operators and symbols.
    List is: 1. irrational numbers
             2. operators "inc" and "dec"
             3. factorial
             4. operators '^' and '√' 
             5. multiplication and division
             6. addition and substraction
    """

    if str_for_calc == "":
        return ""

    str_for_calc = __string_control(str_for_calc)

    error = re.findall(r"(?:Syntax error:|Arithmetic error:)", str_for_calc)

    if bool(error):
        return str_for_calc

    str_for_calc = __convert_to_evaluable_inc(str_for_calc)
    str_for_calc = __convert_to_evaluable_factorial(str_for_calc)
    str_for_calc = __convert_to_evaluate_power(str_for_calc)

    try:
        eval_string = __funct(str_for_calc)  # calculation

        list_comp = re.findall(r"j", str(eval_string))

        if bool(list_comp):
            return "Arithmetic error"

    except NameError:

        return "Syntax error"

    except SyntaxError:

        return "Syntax error"

    except ZeroDivisionError:

        return "Arithmetic error: /0"

    except OverflowError:

        return "Overflow error"
  
    try:
        return float(eval_string)

    except OverflowError:

        return "Overflow error"


# ------------------------------------------------random numbers-------------------------------------------------------

def __create_generator(modulus: int, multiplier: int, increment: int, seed: int) -> Generator[int, None, None]:
    """!
    @brief Creates a lcg with given parameters.
    @param modulus The modulus the lcg will use.
    @param multiplier The multiplier the lcg will use.
    @param increment The increment the lcg will use (set to zero if you want to use a mcg).
    @param seed The initial seed the lcg will use.
    """
    while True:
        seed = (multiplier * seed + increment) % modulus
        yield seed


def __combine_generators(generators: List[Generator[int, None, None]], modulus_of_first: int) -> int:
    """!
    @brief Increments multiple lcgs and combines their results into a better one
    @param generators A list of lcgs to combine into 1
    @param modulus_of_first The modulus of the first lcg
    @return The combined result of multiple lcgs.
    """
    result = 0
    for i, generator in enumerate(generators):
        result += ((-1) ** i) * generator.__next__()
    return result % (modulus_of_first - 1)

## Linear Congruential Generator which uses time as seed
__glibc_lcg = __create_generator(2 ** 31, 1103515245, 12345, int(time.time_ns()))

## Linear Congruential Generator  which uses next item from iterator as seed
__musl_lcg = __create_generator(2 ** 64, 6364136223846793005, 1, __glibc_lcg.__next__())

# Multiplier from  https://doi.org/10.1002/spe.3030
## Linear Congruential Generator which uses power of next items from previous two generators as seed
__custom_lcg = __create_generator(2 ** 64, 0xd1342543de82ef95, 1, __glibc_lcg.__next__() ^ __musl_lcg.__next__())

## List of all LCG generators
__lcg_table = [__custom_lcg, __musl_lcg, __glibc_lcg]

## Modulus for first generator 
__first_generator_modulus = 2 ** 64


def get_random_number() -> int:
    """!
    @brief Returns a random number in the range fo [0, 2**64).
    @return A random number.

    This function should not be considered cryptographically secure.
    """
    return __combine_generators(__lcg_table, __first_generator_modulus)
