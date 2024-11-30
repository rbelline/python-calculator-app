from tkinter import Button
from functions import add_to_calculation, evaluate_calculation, clear_field

def create_buttons(root, text_widget):
    btn_1 = Button(root, width=5, height=2,  text='1', font=5, bg='Gold', command=lambda: add_to_calculation(1, text_widget))
    btn_1.grid(row=2, column=1)
    btn_2 = Button(root, width=5, height=2,  text='2', font=5, bg='Gold', command=lambda: add_to_calculation(2, text_widget))
    btn_2.grid(row=2, column=2)
    btn_3 = Button(root, width=5, height=2,  text='3', font=5, bg='Gold', command=lambda: add_to_calculation(3, text_widget))
    btn_3.grid(row=2, column=3)
    btn_plus = Button(root, width=5, height=2,  text='+', font=5, bg='Gold', command=lambda: add_to_calculation("+", text_widget))
    btn_plus.grid(row=2, column=4)

    btn_4 = Button(root, width=5, height=2,  text='4', font=5, bg='Gold', command=lambda: add_to_calculation(4, text_widget))
    btn_4.grid(row=3, column=1)
    btn_5 = Button(root, width=5, height=2,  text='5', font=5, bg='Gold', command=lambda: add_to_calculation(5, text_widget))
    btn_5.grid(row=3, column=2)
    btn_6 = Button(root, width=5, height=2,  text='6', font=5, bg='Gold', command=lambda: add_to_calculation(6, text_widget))
    btn_6.grid(row=3, column=3)
    btn_minus = Button(root, width=5, height=2,  text='-', font=5, bg='Gold', command=lambda: add_to_calculation("-", text_widget))
    btn_minus.grid(row=3, column=4)

    btn_7 = Button(root, width=5, height=2,  text='7', font=5, bg='Gold', command=lambda: add_to_calculation(7, text_widget))
    btn_7.grid(row=4, column=1)
    btn_8 = Button(root, width=5, height=2,  text='8', font=5, bg='Gold', command=lambda: add_to_calculation(8, text_widget))
    btn_8.grid(row=4, column=2)
    btn_9 = Button(root, width=5, height=2,  text='9', font=5, bg='Gold', command=lambda: add_to_calculation(9, text_widget))
    btn_9.grid(row=4, column=3)
    btn_mul = Button(root, width=5, height=2,  text='*', font=5, bg='Gold', command=lambda: add_to_calculation("*", text_widget))
    btn_mul.grid(row=4, column=4)

    btn_cbleft = Button(root, width=5, height=2,  text='(', font=5, bg='Gold', command=lambda: add_to_calculation("(", text_widget))
    btn_cbleft.grid(row=5, column=1)
    btn_0 = Button(root, width=5, height=2,  text='0', font=5, bg='Gold', command=lambda: add_to_calculation(0, text_widget))
    btn_0.grid(row=5, column=2)
    btn_cbright = Button(root, width=5, height=2,  text=')', font=5, bg='Gold', command=lambda: add_to_calculation(")", text_widget))
    btn_cbright.grid(row=5, column=3)
    btn_div = Button(root, width=5, height=2,  text='/', font=5, bg='Gold', command=lambda: add_to_calculation("/", text_widget))
    btn_div.grid(row=5, column=4)

    btn_clear = Button(root, width=13, height=2,  text='C', font=5, bg='Gold', command=lambda: clear_field(text_widget))
    btn_clear.grid(row=6, column=1, columnspan=2)
    btn_equals = Button(root, width=13, height=2,  text='=', font=5, bg='Gold', command=lambda: evaluate_calculation(text_widget))
    btn_equals.grid(row=6, column=3, columnspan=2)