#!/usr/bin/python3

# author: Martin Valach <xvalac12>

# import everything from tkinter module

import functions
import tkinter as tk
from tkinter import *
from tkinter import ttk

# elementary settings of window
calc_gui = Tk()
calc_gui.geometry('306x329')
calc_gui.resizable(False, False)
calc_gui.title('Calculator G.I.I.T.')

expr = ""


def shift_cursor(shift):
    cursor = input_field.index(INSERT)
    input_field.icursor(cursor + shift)


def clear():
    global expr
    expr = ""
    expr_input.set(expr)


def delete():
    global expr
    expr = expr[:-1]
    expr_input.set(expr)
    # shift_cursor(-1)


def equals():
    global expr
#    eval_string = functions.evaluation_function(expr)
    clear()
#    expr = str(eval_string)
#    expr_input.set(expr)
#    shift_cursor(len(expr))


def button_press(button, shift):
    global expr
    expr = expr + str(button)
    expr_input.set(expr)
    shift_cursor(shift)


def key_press(key):
    global expr
    if key.keycode == 22:
        delete()
    elif key.keycode == 36:
        equals()
    else:
        expr = expr + str(key.char)
        expr_input.set(expr)


expr_input = StringVar()
input_field = ttk.Entry(
    calc_gui,
    font=('arial', 20, 'bold'),
    textvariable=expr_input,
)
input_field.grid(columnspan=5, ipadx=1, ipady=1)
input_field.focus()
expr_input.get()

calc_gui.bind('<Key>', key_press)

# First ROW
button_nsqrt = ttk.Button(
    calc_gui,
    text="n√",
    # height=2,
    width=4,
    command=lambda: button_press("√", 1)
)
button_nsqrt.grid(row=1, column=0)

button_sqrt = ttk.Button(
    calc_gui,
    text="√",
    # height=2,
    width=4,
    command=lambda: button_press("√", 1)
)
button_sqrt.grid(row=1, column=1)

button_pow = ttk.Button(
    calc_gui,
    text="x^2",
    # height=2,
    width=4,
    command=lambda: button_press("^2", 2)
)
button_pow.grid(row=1, column=2)

button_pown = ttk.Button(
    calc_gui,
    text="x^n",
    # height=2,
    width=4,
    command=lambda: button_press("^2", 2)
)
button_pown.grid(row=1, column=3)

button_smile = ttk.Button(
    calc_gui,
    text="smile",
    # height=2,
    width=4,
    command=lambda: button_press("lol", 3)
)
button_smile.grid(row=1, column=4)

# Second ROW
button_factorial = ttk.Button(
    calc_gui,
    text="!",
    # height=2,
    width=4,
    command=lambda: button_press("!", 1)
)
button_factorial.grid(row=2, column=0)

button_increment = ttk.Button(
    calc_gui,
    text="inc",
    # height=2,
    width=4,
    command=lambda: button_press("++", 2)
)
button_increment.grid(row=2, column=1)

button_decrement = ttk.Button(
    calc_gui,
    text="dec",
    # height=2,
    width=4,
    command=lambda: button_press("--", 2)
)
button_decrement.grid(row=2, column=2)

button_clear = ttk.Button(
    calc_gui,
    text="C",
    # height=2,
    width=4,
    command=lambda: clear()
)
button_clear.grid(row=2, column=3)

button_delete = ttk.Button(
    calc_gui,
    text="<--",
    # height=2,
    width=4,
    command=lambda: delete()
)
button_delete.grid(row=2, column=4)

# Third ROW
button_plus = ttk.Button(
    calc_gui,
    text="+",
    # height=2,
    width=4,
    command=lambda: button_press("+", 1)
)
button_plus.grid(row=3, column=0)

button_7 = ttk.Button(
    calc_gui,
    text="7",
    # height=2,
    width=4,
    command=lambda: button_press("7", 1)
)
button_7.grid(row=3, column=1)

button_8 = ttk.Button(
    calc_gui,
    text="8",
    # height=2,
    width=4,
    command=lambda: button_press("8", 1)
)
button_8.grid(row=3, column=2)

button_9 = ttk.Button(
    calc_gui,
    text="9",
    # height=2,
    width=4,
    command=lambda: button_press("9", 1)
)
button_9.grid(row=3, column=3)

button_convert = ttk.Button(
    calc_gui,
    text="€->₽",
    # height=2,
    width=4,
    command=lambda: button_press("√", 1)
)
button_convert.grid(row=3, column=4)

# Fourth ROW
button_minus = ttk.Button(
    calc_gui,
    text="-",
    # height=2,
    width=4,
    command=lambda: button_press("-", 1)
)
button_minus.grid(row=4, column=0)

button_4 = ttk.Button(
    calc_gui,
    text="4",
    # height=2,
    width=4,
    command=lambda: button_press("4", 1)
)
button_4.grid(row=4, column=1)

button_5 = ttk.Button(
    calc_gui,
    text="5",
    # height=2,
    width=4,
    command=lambda: button_press("5", 1)
)
button_5.grid(row=4, column=2)

button_6 = ttk.Button(
    calc_gui,
    text="6",
    # height=2,
    width=4,
    command=lambda: button_press("6", 1)
)
button_6.grid(row=4, column=3)

button_rng = ttk.Button(
    calc_gui,
    text="RNG",
    # height=2,
    width=4,
    command=lambda: button_press("√", 1)
)
button_rng.grid(row=4, column=4)

# Fifth ROW
button_mul = ttk.Button(
    calc_gui,
    text="*",
    # height=2,
    width=4,
    command=lambda: button_press("*", 1)
)
button_mul.grid(row=5, column=0)

button_1 = ttk.Button(
    calc_gui,
    text="1",
    # height=2,
    width=4,
    command=lambda: button_press("1", 1)
)
button_1.grid(row=5, column=1)

button_2 = ttk.Button(
    calc_gui,
    text="2",
    # height=2,
    width=4,
    command=lambda: button_press("2", 1)
)
button_2.grid(row=5, column=2)

button_3 = ttk.Button(
    calc_gui,
    text="3",
    # height=2,
    width=4,
    command=lambda: button_press("3", 1)
)
button_3.grid(row=5, column=3)

button_equals = ttk.Button(
    calc_gui,
    text="=",
    # height=5,
    width=4,
    command=lambda: equals()
)
button_equals.grid(row=5, column=4, rowspan=2)

# Sixth ROW
button_div = ttk.Button(
    calc_gui,
    text="/",
    # height=2,
    width=4,
    command=lambda: button_press("/", 1)
)
button_div.grid(row=6, column=0)

button_0 = ttk.Button(
    calc_gui,
    text="0",
    # height=2,
    width=12,
    command=lambda: button_press("0", 1)
)
button_0.grid(row=6, column=1, columnspan=2)


button_dot = ttk.Button(
    calc_gui,
    text=".",
    # height=2,
    width=4,
    command=lambda: button_press(".", 1)
)
button_dot.grid(row=6, column=3)


calc_gui.mainloop()  # run loops for events (clicks, keypress)
