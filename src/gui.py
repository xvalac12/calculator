#!/usr/bin/python3
# author: Martin Valach <xvalac12>

from idlelib.tooltip import Hovertip
# import everything from tkinter module
from tkinter import *
from tkinter import ttk

import functions

# elementary settings of window
calc_gui = Tk()
screen_width = int(calc_gui.winfo_screenwidth()/9)
screen_height = int(calc_gui.winfo_screenheight()/3.05)
calc_gui.geometry(f'{screen_width}x{screen_height}')
calc_gui.resizable(False, False)
calc_gui.title('Calculator G.I.I.T.')
calc_gui.config(bg="white")
img = Image("photo", file="icon/icon.png")
calc_gui.tk.call('wm', 'iconphoto', calc_gui._w, img)


# settings of grid
calc_gui.columnconfigure(0, weight=1)
calc_gui.columnconfigure(1, weight=1)
calc_gui.columnconfigure(2, weight=1)
calc_gui.columnconfigure(3, weight=1)
calc_gui.columnconfigure(4, weight=1)

# settings of style
style = ttk.Style(calc_gui)
style.configure('TLabel',
                font=('Helvetica', 30, 'black'),
                background='black'
                )
style.configure('TButton',
                font=('Helvetica', 19),
                foreground='gray',
                background='white',
                bordercolor='black',
                width=20,
                padding=10
                )
style.configure('Equals.TButton',
                font=('Helvetica', 30),
                width=10,
                padding=28,
                )
style.configure('Zero.TButton',
                font=('Helvetica', 19),
                width=40,
                padding=10,
                )
style.map('TButton', foreground=[('pressed', 'red'), ('active', 'red')])
# style.theme_use('default')

expr = ""

# main menu settings
main_menu = Menu(calc_gui)
calc_gui.config(menu=main_menu)
file_menu = Menu(main_menu, tearoff=0)
help_menu = Menu(main_menu, tearoff=0)

#  items of main menu File and Help
main_menu.add_cascade(label="File", menu=file_menu)
main_menu.add_cascade(label="Help", menu=help_menu)

# submenus of File
file_menu.add_command(label='Maybe something')
file_menu.add_command(label='Exit calculator', command=calc_gui.destroy)

# submenus of Help
help_menu.add_command(label='Manual...', command=lambda: manual_window())
help_menu.add_command(label='About...', command=lambda: about_window())


def manual_window():
    window = Toplevel()
    window.geometry(f'{screen_height}x{int(screen_width/2)}')
    window.title("Manual")
    window.config(bg="white")
    ttk.Label(
        window,
        text='See user documentation',
        font=("Times", "12"),
        background="white"
    ).pack(pady=10)
    window.mainloop()


def about_window():
    window = Toplevel()
    window.geometry(f'{screen_height}x{int(screen_width/1.8)}')
    window.title("About")
    window.config(bg="white")
    ttk.Label(
        window,
        text='Pretty basic calculator',
        font=("Times", "16", "bold"),
        background="white"
    ).pack(padx=10, pady=10)
    ttk.Label(
        window,
        text='Created by:\n   ',
        font=("Times", "12", "bold"),
        background="white"
    ).pack(padx=10)
    ttk.Label(
        window,
        text='   Adam Bezák\n'
             '   Michal Jozef Bukas\n'
             '   Samuel Stolárik\n'
             '   Martin Valach',
        font=("Times", "12", "italic"),
        background="white"
    ).pack(padx=10)
    ttk.Label(
        window,
        text='Version: 1.0\n'
             'This program comes with absolutely no warranty.\n'
             'See the GNU General Public Licence, version 3\n'
             'or later for details.',
        font=("Times", "12"),
        background="white"
    ).pack(padx=10, ipady=10)
    window.mainloop()


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
    elif key.keycode == 36:
        equals()
    else:
        expr = expr + str(key.char)
        expr_input.set(expr)


def pop_mes(message, event):
    myTip = Hovertip(event, message)


expr_input = StringVar()

input_field = ttk.Entry(calc_gui, font=('Helvetica', 20), width=100, textvariable=expr_input)
input_field.grid(row=1, column=0, columnspan=5, ipady=8, ipadx=15)
input_field.focus()
expr_input.get()

calc_gui.bind('<Key>', key_press)


# First ROW
button_nsqrt = ttk.Button(calc_gui, text="n√", command=lambda: button_press("√", 0))
button_nsqrt.grid(row=2, column=0)
button_nsqrt.bind(pop_mes(" Nth root of x - n√x ", button_nsqrt))

button_sqrt = ttk.Button(calc_gui, text="2√", command=lambda: button_press("2√", 2))
button_sqrt.grid(row=2, column=1)
button_sqrt.bind(pop_mes(" Square root of x - 2√x ", button_sqrt))

button_pow = ttk.Button(calc_gui, text="x^2", command=lambda: button_press("^2", 2))
button_pow.grid(row=2, column=2)
button_pow.bind(pop_mes(" Exponentiation - x^2 ", button_pow))

button_pown = ttk.Button(calc_gui, text="x^n", command=lambda: button_press("^", 1))
button_pown.grid(row=2, column=3)
button_pown.bind(pop_mes(" Exponentiation - x^n ", button_pown))

button_smile = ttk.Button(calc_gui, text="SFT", command=lambda: shift_cursor(1))
button_smile.grid(row=2, column=4)
button_smile.bind(pop_mes(" No idea RN ", button_smile))

# Second ROW
button_factorial = ttk.Button(calc_gui, text="!", command=lambda: button_press("!", 1))
button_factorial.grid(row=3, column=0)
button_factorial.bind(pop_mes(" Factorial of x - x! ", button_factorial))

button_increment = ttk.Button(calc_gui, text="INC", command=lambda: button_press("inc", 3))
button_increment.grid(row=3, column=1)
button_increment.bind(pop_mes(" Incrementation by 1 - inc1 ", button_increment))

button_decrement = ttk.Button(calc_gui, text="DEC", command=lambda: button_press("dec", 3))
button_decrement.grid(row=3, column=2)
button_decrement.bind(pop_mes(" Decrementation by 1 - dec1 ", button_decrement))

button_clear = ttk.Button(calc_gui, text="C", command=lambda: clear())
button_clear.grid(row=3, column=3)
button_clear.bind(pop_mes(" Clear all characters ", button_clear))

button_delete = ttk.Button(calc_gui, text="<--", command=lambda: delete())
button_delete.grid(row=3, column=4)
button_delete.bind(pop_mes(" Clear last character ", button_delete))

# Third ROW
button_plus = ttk.Button(calc_gui, text="+", command=lambda: button_press("+", 1))
button_plus.grid(row=4, column=0)
button_plus.bind(pop_mes(" Addition - x+x ", button_plus))

button_7 = ttk.Button(calc_gui, text="7", command=lambda: button_press("7", 1))
button_7.grid(row=4, column=1)
button_7.bind(pop_mes(" Number 7 ", button_7))

button_8 = ttk.Button(calc_gui, text="8", command=lambda: button_press("8", 1))
button_8.grid(row=4, column=2)
button_8.bind(pop_mes(" Number 8 ", button_8))

button_9 = ttk.Button(calc_gui, text="9", command=lambda: button_press("9", 1))
button_9.grid(row=4, column=3)
button_9.bind(pop_mes(" Number 9 ", button_9))

button_convert = ttk.Button(calc_gui, text="€->₽", command=lambda: button_press("√", 1))
button_convert.grid(row=4, column=4)
button_convert.bind(pop_mes(" Conversion from eur(€) to ruble(₽) ", button_convert))

# Fourth ROW
button_minus = ttk.Button(calc_gui, text="-", command=lambda: button_press("-", 1))
button_minus.grid(row=5, column=0)
button_minus.bind(pop_mes(" Subtraction - x-x ", button_minus))

button_4 = ttk.Button(calc_gui, text="4", command=lambda: button_press("4", 1))
button_4.grid(row=5, column=1)
button_4.bind(pop_mes(" Number 4 ", button_4))

button_5 = ttk.Button(calc_gui, text="5", command=lambda: button_press("5", 1))
button_5.grid(row=5, column=2)
button_5.bind(pop_mes(" Number 5 ", button_5))

button_6 = ttk.Button(calc_gui, text="6", command=lambda: button_press("6", 1))
button_6.grid(row=5, column=3)
button_6.bind(pop_mes(" Number 6 ", button_6))

button_rng = ttk.Button(calc_gui, text="RNG", command=lambda: button_press("√", 1))
button_rng.grid(row=5, column=4)
button_rng.bind(pop_mes(" Generate random number ", button_rng))

# Fifth ROW
button_mul = ttk.Button(calc_gui, text="*", command=lambda: button_press("*", 1))
button_mul.grid(row=6, column=0)
button_mul.bind(pop_mes(" Multiplication - x*x ", button_mul))

button_1 = ttk.Button(calc_gui, text="1", command=lambda: button_press("1", 1))
button_1.grid(row=6, column=1)
button_1.bind(pop_mes(" Number 1 ", button_1))

button_2 = ttk.Button(calc_gui, text="2", command=lambda: button_press("2", 1))
button_2.grid(row=6, column=2)
button_2.bind(pop_mes(" Number 2 ", button_2))

button_3 = ttk.Button(calc_gui, text="3", command=lambda: button_press("3", 1))
button_3.grid(row=6, column=3)
button_3.bind(pop_mes(" Number 3 ", button_3))

button_equals = ttk.Button(calc_gui, text="=", style='Equals.TButton', command=lambda: equals())
button_equals.grid(row=6, column=4, rowspan=2)
button_equals.bind(pop_mes(" Calculate expression ", button_equals))

# Sixth ROW
button_div = ttk.Button(calc_gui, text="/", command=lambda: button_press("/", 1))
button_div.grid(row=7, column=0)
button_div.bind(pop_mes(" Division - x/x ", button_div))

button_0 = ttk.Button(calc_gui, text="0", style='Zero.TButton', command=lambda: button_press("0", 1))
button_0.grid(row=7, column=1, columnspan=2)
button_0.bind(pop_mes(" Number 0 ", button_0))

button_dot = ttk.Button(calc_gui, text=".", command=lambda: button_press(".", 1))
button_dot.grid(row=7, column=3)
button_dot.bind(pop_mes(" Decimal separator ", button_dot))

calc_gui.mainloop()  # run loops for events (clicks, keypress)
