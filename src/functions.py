#!/usr/bin/python3
from logging import raiseExceptions
import re
from typing import Union


# function which calculates basic operations
def __funct(string_for_eval):

  
    value = eval(string_for_eval)
   
    
    return value


def __find_all_expressions_power_d(string_for_change: str) -> str:

    string_list = re.findall(r" *[\^√] *",string_for_change)  # check if there are any desired symbols in string

    if bool(string_list) == False:

        return string_for_change

    string_for_change = "".join(reversed(string_for_change))  # string is reversed because I want to look for last occurence of symbol

    try:
        # this regex must be read backwards. It is backwards because I need to look for the most inner symbol so it will be mathematicly correct
        # this regex looks for symbols ^ and √ . Then it cuts it from string with all operands.
        # It must be in try because there are two tipes of tring which I look for. If this regex finds nothing it throws exception
        # which would ruin whole calculation

        substr = re.search(r"(?:\d+\.\d*|\d+) *[-\+]? *[\^√] *(?:\d+\.\d*|\d+) *[-\+]{1} *(?:\D|$)", string_for_change).group()

        substr = "".join(reversed(substr))

        found = re.findall(r" *[-\+\*\\]{1} *[\+-]{1}",substr) # if first operand is negative number I need to strip substr from previous sign

        if bool(found):

            substr = re.sub(r"(?:\D|^)","",substr,1)  

    except AttributeError:
        substr = ""

    if substr == "":
    
        substr = re.search(r"(?:\d+\.\d*|\d+) *[-\+]? *[\^√] *(?:\d+\.\d*|\d+)", string_for_change).group()
                                                                                                        # search is used to find first occurence
                                                                                                        # this may proof uneffecient and it is but
                                                                                                        # while it tried to be fast it has also taken
                                                                                                        # shortcut which wasn't mathemathicly correct
        substr = "".join(reversed(substr))

    if "^" in substr:

        nums = re.split(" *\^ *",substr)    # taking oprands for calculation
        
        num = float(nums[0])**float(nums[1])
        
        substr = "".join(reversed(substr))
        num = "".join(reversed(str(num)))
        
        string_for_change = string_for_change.replace(substr, str(num),1)    # replacing substring with value

    else:

        nums = re.split(" *√ *",substr)     # spliting expression into two parts
        negative = False
        is_not_even = float(nums[0]) % 2
       
        exponent = (1 / float(nums[0]))
        number = float(nums[1])

        if number < 0:

            negative = True
            number *= -1
      
        root = number ** exponent
        
        if negative & bool(is_not_even):

            root *= -1

        substr = "".join(reversed(substr))
        root = "".join(reversed(str(root)))
        
        string_for_change = string_for_change.replace(substr, str(root),1)
        #print(string_for_change)
   

    string_for_change = "".join(reversed(string_for_change))
    
    return string_for_change


# function which finds all num^ substrings and changes 
def __find_all_expressions_u(string_for_change: str) -> str:

    string_list_num = re.findall("[-]?(?:\d*\.\d+ *\^ *|\d+ *\^ *)",string_for_change)

    for num in string_list_num:

        num_replaced = num.replace("^","")
        string_for_change = string_for_change.replace(num,num_replaced + "**2")

    

    return string_for_change


# function to change power symbol into string able to be processed by eval function
def __convert_to_evaluate_power(string_for_change: str) -> str:

    
    while string_for_change != __find_all_expressions_power_d(string_for_change):
    
        string_for_change = __find_all_expressions_power_d(string_for_change)    

    return string_for_change   # 1024


    # 2√2^2+5^2-4√81  


# function which calculates factorial 
def __factorial_function(number: int) -> int:

    if number == 0:
        return 1

    return number * __factorial_function(number - 1)


# function which finds all ! symbols and replaces it with number
def __find_all_expressions_factorial(string_for_change: str) -> str:

    string_list = re.findall(r"(?:\d+|\d+\.\d*) *!", string_for_change)

    for num in string_list:

        num_replaced = num.replace("!", "")
        num_replaced = __factorial_function(int(float(num_replaced)))     
        
        string_for_change = string_for_change.replace(num,str(num_replaced))

    return string_for_change

# function whitch calls function for factorial evaluation
def __convert_to_evaluable_factorial(string_for_change: str) -> str:

    return __find_all_expressions_factorial(string_for_change)


# function which finds all inc symbols and replaces them with number
def __find_all_expressions_inc(string_for_change: str) -> str:

    string_for_change = "".join(reversed(string_for_change)) # string is reversed to look for most inner occurence
                                                             # also it had tendency to change incorrect substrings 
                                                             # this is the safest way

    string_list = re.findall(r"\d+[-]?cni|\d+[-]?ced",string_for_change)  

    string_for_change = "".join(reversed(string_for_change))  

    for num in string_list:

        num = "".join(reversed(num))
        
        if "inc" in num:
            num_replaced = num.replace("inc","")
            num_replaced = int(num_replaced) + 1

        else:
            num_replaced = num.replace("dec","")
            num_replaced = int(num_replaced) - 1

        # replaces dec or inc with value, search depends on which operand was calculated
        string_for_change = re.sub(rf"%s\b((?:[^0-9]|\Z))" % num , r"%s\1" % str(num_replaced), string_for_change,re.IGNORECASE)


    return string_for_change


# function which calls functions for evaluation of inc and dec symbol 
def __convert_to_evalauble_inc(string_for_change: str) -> str:

    while string_for_change != __find_all_expressions_inc(string_for_change):
        
        string_for_change = __find_all_expressions_inc(string_for_change)

    return string_for_change


# basic test how to use throws in python
def __string_control(string_for_control: str) -> str:

    string_list1 = re.findall(r" \. ",string_for_control)

    if bool(string_list1) == True:

        raise SyntaxError("Space is not allowed between number dot number\n")

    string_list2 = re.findall(r"(?:\D|^) *- *[\d]!",string_for_control)
    
    if bool(string_list2) == True:

        return "a"
        

    return string_for_control

    

# def calculate_expression(str_for_calc: str) -> Union[int, float]:

def calculate_expression(str_for_calc: str) -> float :

    #print(str_for_calc)    
    if str_for_calc == "":
        return ""

    
    str_for_calc = __string_control(str_for_calc)

    error = re.findall(r"a",str_for_calc)
    if bool(error):
 
        raise SyntaxError("Unable to calculate factorial from negative number\n")
        
    str_for_calc = __convert_to_evalauble_inc(str_for_calc)
    str_for_calc = __convert_to_evaluable_factorial(str_for_calc)
    str_for_calc = __convert_to_evaluate_power(str_for_calc)
    
    
    asdf = __funct(str_for_calc)

    #print(asdf)
    return float(asdf)
















def __testing_function(string_for_change: str) -> int:

    string = re.findall(r"inca7",string_for_change)

    string_for_change = "".join(reversed(string_for_change))
    print(string_for_change)

    try:
        substr = re.search(r"(?:\d+\.\d*|\d+) *[-\+]? *[\^√] *(?:\d+\.\d*|\d+) *[-\+]{1} *\D", string_for_change).group()
    except AttributeError:
        substr = re.search(r"(?:\d+\.\d*|\d+) *[\^√] *(?:\d+\.\d*|\d+)[-]{2}", string_for_change)

    substr = "".join(reversed(substr))

    substr = re.sub(r"\D","",substr,1)

    # substr = re.finditer()

    print(substr)

    return string_for_change


# find_all_expressions_power_d("3√-27")
