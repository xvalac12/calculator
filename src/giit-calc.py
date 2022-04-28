#!/usr/bin/python3

"""! @brief Tkinter GUI and main file of calculator"""
##
# @mainpage Documentation
# @section description_main Description
# School project for subject IVS (Practical Aspects of Software Design).
# Calculator with elementary operations (+,-,*,/), factorial, exponentiation, square root, incrementation,
# decrementation and generating of random number.
# Calculator can be control by mouse and keyboard.
#
# @section notes_main Notes
# - runs on Ubuntu 20.04+
# - calculator uses python math function eval() for evaluation of expressions
# - made on python3.10
# - works on python 3.7+
# - gui made with tkinter python library


"""! @brief Tkinter GUI and main file of calculator"""
##
# @section description_giit-calc Description
# Defines GUI of calculator app and behavior of buttons.
#
# @section libraries_giit-calc Libraries/Modules
# - tkinter python library
# - webbrowser python library
# - idlelib python library
#
# @file giit-calc.py
# @brief Graphic user interface and main file of calculator
# @author Martin Valach <xvalac12@stud.fit.vutbr.cz>
# @date 28.4.2022

# import everything from tkinter module

from tkinter import *
from tkinter import ttk
import webbrowser
import re
from idlelib.tooltip import Hovertip
import functions

## Global variable for entered characters
expr = ""
## Calculator window
calc_gui = Tk()
## Width of calculator in px
screen_width = 580
# screen_width = int(calc_gui.winfo_screenwidth()/3.3)
## Width of calculator in px
screen_height = 465
# screen_height = int(calc_gui.winfo_screenheight()/2.34)
## Variable to hold string of expression in GUI
expr_input = StringVar()
## Variable to hold style of widget in GUI
style = ttk.Style(calc_gui)
## Variable to hold menu of GUI
main_menu = Menu(calc_gui)
## Variable to hold submenu File
file_menu = Menu(main_menu, tearoff=0)
## Variable to hold submenu Help
help_menu = Menu(main_menu, tearoff=0)
## Icon to show on Dock
img = Image("photo", file="icon.png")

# setting geometry and ,config of calculator window
calc_gui.geometry(f'{screen_width}x{screen_height}')
calc_gui.resizable(False, False)
calc_gui.title('Calculator G.I.I.T.')
calc_gui.config(bg="white")

# icon
calc_gui.tk.call('wm', 'iconphoto', calc_gui._w, img)

# settings of grid
calc_gui.columnconfigure(0, weight=1)
calc_gui.columnconfigure(1, weight=1)
calc_gui.columnconfigure(2, weight=1)
calc_gui.columnconfigure(3, weight=1)
calc_gui.columnconfigure(4, weight=1)

# style of label
style.configure('TLabel', font=('Helvetica', 30, 'black'), background='black')
# style of buttons
style.configure('TButton', font=('Helvetica', 17), foreground='gray', background='white',
                bordercolor='black', width=20, padding=20,)
style.map('TButton', foreground=[('pressed', 'red'), ('active', 'red')])
# style of equal button
style.configure('Equals.TButton', font=('Helvetica', 30), width=5, padding=46)
# style of number zero button
style.configure('Zero.TButton', font=('Helvetica', 17), width=40, padding=20)


# main menu settings
calc_gui.config(menu=main_menu)

#  items of main menu File and Help
main_menu.add_cascade(label="File", menu=file_menu)
main_menu.add_cascade(label="Help", menu=help_menu)

# submenus of File
file_menu.add_command(label='Exit calculator', command=calc_gui.destroy)

# submenus of Help
help_menu.add_command(label='Manual...', command=lambda: manual_window())
help_menu.add_command(label='About...', command=lambda: about_window())


def manual_window():
    """!
    @brief Open user documentation

    Manual is link to user documentation pdf.
    """
    webbrowser.open_new(r'../dokumentace.pdf')


def about_window():
    """!
    @brief Create window with info about calculator

    In about window is info about calculator (authors, version and licenses). Setting of configurations of window.
    """

    ## Variable to hold 'Help' window in GUI
    window = Toplevel()
    window.geometry(f'{int(screen_width/1.5)}x{int(screen_height/1.8)}')
    window.title("About")
    window.config(bg="white")
    ttk.Label(window,text='Pretty basic calculator', font=("Times", "16", "bold"), background="white").\
        pack(padx=10, pady=10)
    ttk.Label(window, text='Created by:\n   ', font=("Times", "12", "bold"), background="white").\
        pack(padx=10)
    ttk.Label(
        window,
        text='   Adam Bezák\n'
             '   Michal Jozef Bukas\n'
             '   Samuel Stolárik\n'
             '   Martin Valach',
        font=("Times", "12", "italic"),
        background="white").\
        pack(padx=10)
    ttk.Label(
        window,
        text='Version: 1.0\n'
             'This program comes with absolutely no warranty.\n'
             'See the GNU General Public Licence, version 3\n'
             'or later for details.',
        font=("Times", "12"),
        background="white").\
        pack(padx=10, ipady=10)


def shift_cursor(shift):
    """!
    @brief Function for shifting cursor to right
    @param shift number to shift

    Function get number of char to shift from pressed button and shift cursor to right by value shift var.
    """

    ## Position of cursor
    cursor = input_field.index(INSERT)
    input_field.icursor(cursor + shift)


def clear():
    """!
    @brief Function for clearing expression

    Clear all content shown on the display (var expr).
    """
    global expr
    expr = ""
    expr_input.set(expr)


# function for deleting last character
def delete():
    """!
    @brief Function for deleting last character

    Delete last character shown on the display (var expr).
    """

    global expr
    expr = expr[:-1]
    expr_input.set(expr)


def equals():
    """!
    @brief Function for assign evaluation from math function to expression

    Function send content from display to math function and get a result. Result is then shown on display.
    """
    global expr
    ## Result of evaluation
    eval_string = functions.calculate_expression(expr)
    clear()
    eval_string = pars_convert(eval_string)
    expr = str(eval_string)
    expr_input.set(expr)
    shift_cursor(len(expr))


def pars_convert(eval_string):
    """!
    @brief Function for parsing output from math library
    @param eval_string string to parse
    @return parsed string

    Function check string from math library (how long is it, if it has dot, if it is error)
    and convert exponential format (e+n to *10^n).
    """
    is_error = re.findall(r"(?:Syntax error|Arithmetic error)", str(eval_string))
    if bool(is_error):
        return eval_string

    exp_expr = re.findall(r"e", str(eval_string))
    is_there_dot = re.findall(r"\.", str(eval_string))

    if bool(exp_expr):
        eval_string = str(eval_string).replace("e+", "*10^")
        return eval_string

    elif bool(is_there_dot) and len(str(eval_string)) > 18:
        new_string = str(eval_string)[0:10]
        without_dot = re.split(r"\.", str(eval_string))
        exponent = len(str(without_dot[0]))

        if exponent < 10:
            decimal_places = len(str(without_dot[1])) - 1
            new_string = without_dot[0] + "." + without_dot[1][0:decimal_places]

        return float(new_string)

    elif len(str(eval_string)) > 20 and not bool(is_there_dot):
        new_string = str(eval_string)[0:10]
        exponent = len(str(eval_string))
        new_string = new_string[0] + "." + new_string[1:15] + "*10^" + str(exponent)

        return new_string

    return eval_string


def button_press(button, shift):
    """!
    @brief Function for assign value of gui button to expression

    @param button gui button to assign
    @param shift number of character to shift cursor

    Characters entered from gui buttons are concatenated to expression.
    """
    global expr
    expr = expr + str(button)
    expr_input.set(expr)
    shift_cursor(shift)


def key_press(key):
    """!
    @brief Function for assign value of key to expression

    @param key character from key to assign

    Characters entered from keyboard are concatenated to expression. Some special keys have different behavior.
    """
    global expr
    if key.keycode == 22:  # BackSpace
        delete()
    elif key.keycode == 23:  # Tab
        print()
    elif key.keycode == 36:  # Enter
        # easter egg
        url = "https://www.youtube.com/watch?v=rcVb6l4TpHw"
        if expr == "blumelein":
            webbrowser.open(url, new=0, autoraise=True)
        equals()
    else:
        expr = expr + str(key.char)
        expr_input.set(expr)


def random_number():
    """!
    @brief Function assign random number to expression

    Characters entered from keyboard are concatenated to expression. Some special characters have different behavior.
    """
    global expr
    rng = functions.get_random_number()
    expr = expr + str(rng)
    expr_input.set(expr)


def pop_mes(message, event):
    """!
    @brief Function for showing for pop-out messages about buttons

    @param message pop-up message to print
    @param event button to show message

    When mouse hover over the button, show pup-up message about button function.
    """
    Hovertip(event, message)


calc_gui.bind('<Key>', key_press)

# calculator display
## Variable to hold calculator input display
input_field = ttk.Entry(calc_gui, font=('Helvetica', 25), width=100, textvariable=expr_input, justify='right')
input_field.grid(row=1, column=0, columnspan=5, ipady=8, ipadx=15)
input_field.focus_set()
expr_input.get()


# First ROW
## Button for n-th square root
button_nsqrt = ttk.Button(calc_gui, text="n√", command=lambda: button_press("√", 0))
button_nsqrt.grid(row=2, column=0)
button_nsqrt.bind(pop_mes(" Nth root of x \n n√x ", button_nsqrt))

## Button for square root
button_sqrt = ttk.Button(calc_gui, text="2√", command=lambda: button_press("2√", 2))
button_sqrt.grid(row=2, column=1)
button_sqrt.bind(pop_mes(" Square root of x \n 2√x ", button_sqrt))

## Button for exponentiation
button_pow = ttk.Button(calc_gui, text="x^2", command=lambda: button_press("^2", 2))
button_pow.grid(row=2, column=2)
button_pow.bind(pop_mes(" Exponentiation \n x^2 ", button_pow))

## Button for n-th exponentiation
button_pown = ttk.Button(calc_gui, text="x^n", command=lambda: button_press("^", 1))
button_pown.grid(row=2, column=3)
button_pown.bind(pop_mes(" Exponentiation \n x^n ", button_pown))

## Button for pi (π)
button_pi = ttk.Button(calc_gui, text="π", command=lambda: button_press("π", 1))
button_pi.grid(row=2, column=4)
button_pi.bind(pop_mes(" Ludolph\'s number ", button_pi))

# Second ROW
## Button for factorial
button_factorial = ttk.Button(calc_gui, text="!", command=lambda: button_press("!", 1))
button_factorial.grid(row=3, column=0)
button_factorial.bind(pop_mes(" Factorial of x \n x! ", button_factorial))

## Button for increment
button_increment = ttk.Button(calc_gui, text="INC", command=lambda: button_press("inc", 3))
button_increment.grid(row=3, column=1)
button_increment.bind(pop_mes(" Incrementation by 1 \n incx ", button_increment))

## Button for decrement
button_decrement = ttk.Button(calc_gui, text="DEC", command=lambda: button_press("dec", 3))
button_decrement.grid(row=3, column=2)
button_decrement.bind(pop_mes(" Decrementation by 1 \n decx ", button_decrement))

## Button for clear expression
button_clear = ttk.Button(calc_gui, text="C", command=lambda: clear())
button_clear.grid(row=3, column=3)
button_clear.bind(pop_mes(" Clear all characters ", button_clear))

## Button for delete one char
button_delete = ttk.Button(calc_gui, text="<--", command=lambda: delete())
button_delete.grid(row=3, column=4)
button_delete.bind(pop_mes(" Clear last character ", button_delete))

# Third ROW
## Button for equation
button_plus = ttk.Button(calc_gui, text="+", command=lambda: button_press("+", 1))
button_plus.grid(row=4, column=0)
button_plus.bind(pop_mes(" Addition \n x+y ", button_plus))

## Button number 7
button_7 = ttk.Button(calc_gui, text="7", command=lambda: button_press("7", 1))
button_7.grid(row=4, column=1)
button_7.bind(pop_mes(" Number 7 ", button_7))

## Button number 8
button_8 = ttk.Button(calc_gui, text="8", command=lambda: button_press("8", 1))
button_8.grid(row=4, column=2)
button_8.bind(pop_mes(" Number 8 ", button_8))

## Button number 9
button_9 = ttk.Button(calc_gui, text="9", command=lambda: button_press("9", 1))
button_9.grid(row=4, column=3)
button_9.bind(pop_mes(" Number 9 ", button_9))

## Button e (Euler`n number)
button_e = ttk.Button(calc_gui, text="e", command=lambda: button_press("e", 1))
button_e.grid(row=4, column=4)
button_e.bind(pop_mes(" Euler\'s number ", button_e))

# Fourth ROW
## Button for subtraction
button_minus = ttk.Button(calc_gui, text="-", command=lambda: button_press("-", 1))
button_minus.grid(row=5, column=0)
button_minus.bind(pop_mes(" Subtraction \n x-y ", button_minus))

## Button number 4
button_4 = ttk.Button(calc_gui, text="4", command=lambda: button_press("4", 1))
button_4.grid(row=5, column=1)
button_4.bind(pop_mes(" Number 4 ", button_4))

## Button number 5
button_5 = ttk.Button(calc_gui, text="5", command=lambda: button_press("5", 1))
button_5.grid(row=5, column=2)
button_5.bind(pop_mes(" Number 5 ", button_5))

## Button number 6
button_6 = ttk.Button(calc_gui, text="6", command=lambda: button_press("6", 1))
button_6.grid(row=5, column=3)
button_6.bind(pop_mes(" Number 6 ", button_6))

## Button for generating random number
button_rng = ttk.Button(calc_gui, text="RNG", command=lambda: random_number())
button_rng.grid(row=5, column=4)
button_rng.bind(pop_mes(" Generate random number ", button_rng))

# Fifth ROW
## Button for multiplying
button_mul = ttk.Button(calc_gui, text="*", command=lambda: button_press("*", 1))
button_mul.grid(row=6, column=0)
button_mul.bind(pop_mes(" Multiplication \n x*y ", button_mul))

## Button number 1
button_1 = ttk.Button(calc_gui, text="1", command=lambda: button_press("1", 1))
button_1.grid(row=6, column=1)
button_1.bind(pop_mes(" Number 1 ", button_1))

## Button number 2
button_2 = ttk.Button(calc_gui, text="2", command=lambda: button_press("2", 1))
button_2.grid(row=6, column=2)
button_2.bind(pop_mes(" Number 2 ", button_2))

## Button number 3
button_3 = ttk.Button(calc_gui, text="3", command=lambda: button_press("3", 1))
button_3.grid(row=6, column=3)
button_3.bind(pop_mes(" Number 3 ", button_3))

## Button for equation of expression
button_equals = ttk.Button(calc_gui, text="=", style='Equals.TButton', command=lambda: equals())
button_equals.grid(row=6, column=4, rowspan=2)
button_equals.bind(pop_mes(" Calculate expression ", button_equals))

# Sixth ROW
## Button for division
button_div = ttk.Button(calc_gui, text="/", command=lambda: button_press("/", 1))
button_div.grid(row=7, column=0)
button_div.bind(pop_mes(" Division \n x/y ", button_div))

## Button number 0
button_0 = ttk.Button(calc_gui, text="0", style='Zero.TButton', command=lambda: button_press("0", 1))
button_0.grid(row=7, column=1, columnspan=2)
button_0.bind(pop_mes(" Number 0 ", button_0))

## Button decimal separator
button_dot = ttk.Button(calc_gui, text=".", command=lambda: button_press(".", 1))
button_dot.grid(row=7, column=3)
button_dot.bind(pop_mes(" Decimal separator ", button_dot))

calc_gui.mainloop()  # run loops for events (clicks, keypress)
