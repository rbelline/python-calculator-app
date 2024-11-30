import tkinter as tk
from number_buttons import create_buttons
from functions import *


root = tk.Tk()
root.title("Calculator")
root.geometry('330x350')

text_result = tk.Text(root, height=2, width=16, font=("Arial", 24))
text_result.grid(columnspan=5)

create_buttons(root, text_result)


root.mainloop()
