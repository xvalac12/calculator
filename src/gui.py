#!/usr/bin/python3
# author: Martin Valach <xvalac12>

import functions
# import everything from tkinter module
import tkinter as tk
from tkinter import *
from tkinter import ttk

# elementary settings of window
calc_gui = Tk()
screen_width = int(calc_gui.winfo_screenwidth()/10)
screen_height = int(calc_gui.winfo_screenheight()/2.95)
calc_gui.geometry(f'{screen_width}x{screen_height}')
calc_gui.resizable(False, False)
calc_gui.title('Calculator G.I.I.T.')
img = Image("photo", file="icon/icon.png")
calc_gui.tk.call('wm', 'iconphoto', calc_gui._w, img)

# menu settings
menubar = Menu(calc_gui)
calc_gui.config(menu=menubar)

file_menu = Menu(
    menubar,
    tearoff=0
)

# add menu items to the File menu
file_menu.add_command(label='New')
file_menu.add_command(label='Open...')
file_menu.add_command(label='Close')
file_menu.add_separator()

# add Exit menu item
file_menu.add_command(
    label='Exit',
    command=calc_gui.destroy
)

# add the File menu to the menubar
menubar.add_cascade(
    label="File",
    menu=file_menu
)
# create the Help menu
help_menu = Menu(
    menubar,
    tearoff=0
)

help_menu.add_command(label='Welcome')
help_menu.add_command(label='About...')

# add the Help menu to the menubar
menubar.add_cascade(
    label="Help",
    menu=help_menu
)

# settings of grid
calc_gui.columnconfigure(0, weight=1)
calc_gui.columnconfigure(1, weight=1)
calc_gui.columnconfigure(2, weight=1)
calc_gui.columnconfigure(3, weight=1)
calc_gui.columnconfigure(4, weight=1)

# settings of style
style = ttk.Style(calc_gui)
style.configure('TLabel', font=('Helvetica', 30, 'black'), background='black')
style.configure('TButton',
                font=('Helvetica', 19),
                foreground='gray',
                background='white',
                bordercolor='black',
                width=5,
                padding=10
                )
style.configure('Equals.TButton',
                font=('Helvetica', 30),
                width=2,
                padding=28,
                )
style.configure('Zero.TButton',
                font=('Helvetica', 19),
                width=10,
                padding=10,
                )
style.map('TButton', foreground=[('pressed', 'red'), ('active', 'red')])
# style.theme_use('default')

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
    eval_string = functions.calculate_expression(expr)
    clear()
    expr = str(eval_string)
    expr_input.set(expr)
    shift_cursor(len(expr))


def button_press(button, shift):
    global expr
    expr = expr + str(button)
    expr_input.set(expr)
    shift_cursor(shift)


def key_press(key):
    global expr
    if key.keycode == 22:
        delete()
    elif key.keycode == 36 or key.keycode == 20:
        equals()
    else:
        expr = expr + str(key.char)
        expr_input.set(expr)


expr_input = StringVar()

input_field = ttk.Entry(calc_gui, font=('Helvetica', 30), width=25, textvariable=expr_input)
input_field.grid(row=1, column=0, columnspan=5, ipady=8, ipadx=15)
input_field.focus()
expr_input.get()

calc_gui.bind('<Key>', key_press)

# First ROW
button_nsqrt = ttk.Button(calc_gui, text="n√", command=lambda: button_press("√", 0))
button_nsqrt.grid(row=2, column=0)

button_sqrt = ttk.Button(calc_gui, text="2√", command=lambda: button_press("2√", 2))
button_sqrt.grid(row=2, column=1)

button_pow = ttk.Button(calc_gui, text="x^2", command=lambda: button_press("^2", 2))
button_pow.grid(row=2, column=2)

button_pown = ttk.Button(calc_gui, text="x^n", command=lambda: button_press("^", 1))
button_pown.grid(row=2, column=3)

button_smile = ttk.Button(calc_gui, text="SFT", command=lambda: shift_cursor(1))
button_smile.grid(row=2, column=4)

# Second ROW
button_factorial = ttk.Button(calc_gui, text="!", command=lambda: button_press("!", 1))
button_factorial.grid(row=3, column=0)

button_increment = ttk.Button(calc_gui, text="INC", command=lambda: button_press("inc", 3))
button_increment.grid(row=3, column=1)

button_decrement = ttk.Button(calc_gui, text="DEC", command=lambda: button_press("dec", 3))
button_decrement.grid(row=3, column=2)

button_clear = ttk.Button(calc_gui, text="C", command=lambda: clear())
button_clear.grid(row=3, column=3)

button_delete = ttk.Button(calc_gui, text="<--", command=lambda: delete())
button_delete.grid(row=3, column=4)

# Third ROW
button_plus = ttk.Button(calc_gui, text="+", command=lambda: button_press("+", 1))
button_plus.grid(row=4, column=0)

button_7 = ttk.Button(calc_gui, text="7", command=lambda: button_press("7", 1))
button_7.grid(row=4, column=1)

button_8 = ttk.Button(calc_gui, text="8", command=lambda: button_press("8", 1))
button_8.grid(row=4, column=2)

button_9 = ttk.Button(calc_gui, text="9", command=lambda: button_press("9", 1))
button_9.grid(row=4, column=3)

button_convert = ttk.Button(calc_gui, text="€->₽", command=lambda: button_press("√", 1))
button_convert.grid(row=4, column=4)

# Fourth ROW
button_minus = ttk.Button(calc_gui, text="-", command=lambda: button_press("-", 1))
button_minus.grid(row=5, column=0)

button_4 = ttk.Button(calc_gui, text="4", command=lambda: button_press("4", 1))
button_4.grid(row=5, column=1)

button_5 = ttk.Button(calc_gui, text="5", command=lambda: button_press("5", 1))
button_5.grid(row=5, column=2)

button_6 = ttk.Button(calc_gui, text="6", command=lambda: button_press("6", 1))
button_6.grid(row=5, column=3)

button_rng = ttk.Button(calc_gui, text="RNG", command=lambda: button_press("√", 1))
button_rng.grid(row=5, column=4)

# Fifth ROW
button_mul = ttk.Button(calc_gui, text="*", command=lambda: button_press("*", 1))
button_mul.grid(row=6, column=0)

button_1 = ttk.Button(calc_gui, text="1", command=lambda: button_press("1", 1))
button_1.grid(row=6, column=1)

button_2 = ttk.Button(calc_gui, text="2", command=lambda: button_press("2", 1))
button_2.grid(row=6, column=2)

button_3 = ttk.Button(calc_gui, text="3", command=lambda: button_press("3", 1))
button_3.grid(row=6, column=3)

button_equals = ttk.Button(calc_gui, text="=", style='Equals.TButton', command=lambda: equals())
button_equals.grid(row=6, column=4, rowspan=2)

# Sixth ROW
button_div = ttk.Button(calc_gui, text="/", command=lambda: button_press("/", 1))
button_div.grid(row=7, column=0)

button_0 = ttk.Button(calc_gui, text="0", style='Zero.TButton', command=lambda: button_press("0", 1))
button_0.grid(row=7, column=1, columnspan=2)

button_dot = ttk.Button(calc_gui, text=".", command=lambda: button_press(".", 1))
button_dot.grid(row=7, column=3)

calc_gui.mainloop()  # run loops for events (clicks, keypress)
