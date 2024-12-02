import tkinter as tk
from styles.theme import DEFAULT_FONT_STYLE, DIGIT_FONT_STYLE, LIGHT_BLUE, WHITE, OFF_WHITE, LABEL_COLOR

def create_digit_buttons(calculator):
    for digit, grid_value in calculator.digits.items():
        button = tk.Button(calculator.buttons_frame, text=str(digit), bg=WHITE, fg=LABEL_COLOR,
                           font=DIGIT_FONT_STYLE, borderwidth=0, command=lambda x=digit: calculator.add_to_expression(x))
        button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

def create_operator_button(calculator):
    i = 0
    for operator, symbol in calculator.operators.items():
        button = tk.Button(calculator.buttons_frame, text=symbol, bg=OFF_WHITE, fg=LABEL_COLOR,
                           font=DEFAULT_FONT_STYLE, borderwidth=0, command=lambda x=operator: calculator.append_operator(x))
        button.grid(row=i, column=4, sticky=tk.NSEW)
        i += 1

def create_clear_button(calculator):
    button = tk.Button(calculator.buttons_frame, text="C", bg=OFF_WHITE, fg=LABEL_COLOR,
                           font=DEFAULT_FONT_STYLE, borderwidth=0, command= calculator.clear)
    button.grid(row=0, column=1, columnspan=3, sticky=tk.NSEW)

def create_equal_button(calculator):
    button = tk.Button(calculator.buttons_frame, text="=", bg=LIGHT_BLUE, fg=LABEL_COLOR,
                           font=DEFAULT_FONT_STYLE, borderwidth=0, command= calculator.evaluate)
    button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)

def create_special_buttons(calculator):
    create_clear_button(calculator)
    create_equal_button(calculator)