#!/usr/bin/python3

# author: Martin Valach <xvalac12>

# import everything from tkinter module
import tkinter as tk
from tkinter import *

# elementary settings of window
calc = Tk()
calc.geometry('306x329')
calc.resizable(False, False)
calc.title('Calculator G.I.I.T.')

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
    # evaluation_string = evaluation_function(expr)
    clear()
    # expr_input.set(evaluation_string)


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
input_field = Entry(
    calc,
    font=('arial', 20, 'bold'),
    textvariable=expr_input,
)
input_field.grid(columnspan=5, ipadx=1, ipady=1)
input_field.focus()
expr_input.get()

calc.bind('<Key>', key_press)

# First ROW
button_nsqrt = tk.Button(
    calc,
    text="n√",
    height=2,
    width=4,
    command=lambda: button_press("√", 1)
)
button_nsqrt.grid(row=1, column=0)

button_sqrt = tk.Button(
    calc,
    text="√",
    height=2,
    width=4,
    command=lambda: button_press("√", 1)
)
button_sqrt.grid(row=1, column=1)

button_pow = tk.Button(
    calc,
    text="x^2",
    height=2,
    width=4,
    command=lambda: button_press("^2", 2)
)
button_pow.grid(row=1, column=2)

button_pown = tk.Button(
    calc,
    text="x^n",
    height=2,
    width=4,
    command=lambda: button_press("^2", 2)
)
button_pown.grid(row=1, column=3)

button_smile = tk.Button(
    calc,
    text="smile",
    height=2,
    width=4,
    command=lambda: button_press("lol", 3)
)
button_smile.grid(row=1, column=4)

# Second ROW
button_factorial = tk.Button(
    calc,
    text="!",
    height=2,
    width=4,
    command=lambda: button_press("!", 1)
)
button_factorial.grid(row=2, column=0)

button_increment = tk.Button(
    calc,
    text="inc",
    height=2,
    width=4,
    command=lambda: button_press("++", 2)
)
button_increment.grid(row=2, column=1)

button_decrement = tk.Button(
    calc,
    text="dec",
    height=2,
    width=4,
    command=lambda: button_press("--", 2)
)
button_decrement.grid(row=2, column=2)

button_clear = tk.Button(
    calc,
    text="C",
    height=2,
    width=4,
    command=lambda: clear()
)
button_clear.grid(row=2, column=3)

button_delete = tk.Button(
    calc,
    text="<--",
    height=2,
    width=4,
    command=lambda: delete()
)
button_delete.grid(row=2, column=4)

# Third ROW
button_plus = tk.Button(
    calc,
    text="+",
    height=2,
    width=4,
    command=lambda: button_press("+", 1)
)
button_plus.grid(row=3, column=0)

button_7 = tk.Button(
    calc,
    text="7",
    height=2,
    width=4,
    command=lambda: button_press("7", 1)
)
button_7.grid(row=3, column=1)

button_8 = tk.Button(
    calc,
    text="8",
    height=2,
    width=4,
    command=lambda: button_press("8", 1)
)
button_8.grid(row=3, column=2)

button_9 = tk.Button(
    calc,
    text="9",
    height=2,
    width=4,
    command=lambda: button_press("9", 1)
)
button_9.grid(row=3, column=3)

button_convert = tk.Button(
    calc,
    text="€->₽",
    height=2,
    width=4,
    command=lambda: button_press("√", 1)
)
button_convert.grid(row=3, column=4)

# Fourth ROW
button_minus = tk.Button(
    calc,
    text="-",
    height=2,
    width=4,
    command=lambda: button_press("-", 1)
)
button_minus.grid(row=4, column=0)

button_4 = tk.Button(
    calc,
    text="4",
    height=2,
    width=4,
    command=lambda: button_press("4", 1)
)
button_4.grid(row=4, column=1)

button_5 = tk.Button(
    calc,
    text="5",
    height=2,
    width=4,
    command=lambda: button_press("5", 1)
)
button_5.grid(row=4, column=2)

button_6 = tk.Button(
    calc,
    text="6",
    height=2,
    width=4,
    command=lambda: button_press("6", 1)
)
button_6.grid(row=4, column=3)

button_rng = tk.Button(
    calc,
    text="RNG",
    height=2,
    width=4,
    command=lambda: button_press("√", 1)
)
button_rng.grid(row=4, column=4)

# Fifth ROW
button_mul = tk.Button(
    calc,
    text="*",
    height=2,
    width=4,
    command=lambda: button_press("*", 1)
)
button_mul.grid(row=5, column=0)

button_1 = tk.Button(
    calc,
    text="1",
    height=2,
    width=4,
    command=lambda: button_press("1", 1)
)
button_1.grid(row=5, column=1)

button_2 = tk.Button(
    calc,
    text="2",
    height=2,
    width=4,
    command=lambda: button_press("2", 1)
)
button_2.grid(row=5, column=2)

button_3 = tk.Button(
    calc,
    text="3",
    height=2,
    width=4,
    command=lambda: button_press("3", 1)
)
button_3.grid(row=5, column=3)

button_equals = tk.Button(
    calc,
    text="=",
    height=5,
    width=4,
    command=lambda: equals()
)
button_equals.grid(row=5, column=4, rowspan=2)

# Sixth ROW
button_div = tk.Button(
    calc,
    text="/",
    height=2,
    width=4,
    command=lambda: button_press("/", 1)
)
button_div.grid(row=6, column=0)

button_0 = tk.Button(
    calc,
    text="0",
    height=2,
    width=12,
    command=lambda: button_press("0", 1)
)
button_0.grid(row=6, column=1, columnspan=2)


button_dot = tk.Button(
    calc,
    text=".",
    height=2,
    width=4,
    command=lambda: button_press(".", 1)
)
button_dot.grid(row=6, column=3)


calc.mainloop()  # run loops for events (clicks, keypress)
