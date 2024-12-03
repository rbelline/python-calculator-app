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
    button.grid(row=0, column=1, sticky=tk.NSEW)

def create_square_button(calculator):
    button = tk.Button(calculator.buttons_frame, text="x\u00b2", bg=OFF_WHITE, fg=LABEL_COLOR,
                           font=DEFAULT_FONT_STYLE, borderwidth=0, command= calculator.square)
    button.grid(row=0, column=2, sticky=tk.NSEW)

def create_sqrt_button(calculator):
    button = tk.Button(calculator.buttons_frame, text="\u221a", bg=OFF_WHITE, fg=LABEL_COLOR,
                           font=DEFAULT_FONT_STYLE, borderwidth=0, command= calculator.sqrt)
    button.grid(row=0, column=3, sticky=tk.NSEW)

def create_equal_button(calculator):
    button = tk.Button(calculator.buttons_frame, text="=", bg=LIGHT_BLUE, fg=LABEL_COLOR,
                           font=DEFAULT_FONT_STYLE, borderwidth=0, command= calculator.evaluate)
    button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)

def bind_keys(window, calculator):
    window.bind("<Return>", lambda event: calculator.evaluate())
    window.bind("<Escape>", lambda event: calculator.clear())
    window.bind("<Delete>", lambda event: calculator.clear())
    for key in calculator.digits:
        window.bind(str(key), lambda event, digit=key: calculator.add_to_expression(digit))

    for key in calculator.operators:
        window.bind(str(key), lambda event, operator=key: calculator.append_operator(operator))

def create_special_buttons(calculator):
    create_clear_button(calculator)
    create_equal_button(calculator)
    create_square_button(calculator)
    create_sqrt_button(calculator)