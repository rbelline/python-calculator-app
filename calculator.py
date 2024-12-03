import tkinter as tk
from components.display import create_display_labels
from components.frames import create_display_frame, create_buttons_frame
from components.buttons import create_digit_buttons, create_operator_button, create_special_buttons, bind_keys

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0, 0)
        self.window.title("Calculator")

        # define total expression and current expression
        self.total_expression = ""
        self.current_expression = ""

        self.display_frame = create_display_frame(self.window) # creation of display frame
        self.total_label, self.label = create_display_labels(self.display_frame, self.total_expression, self.current_expression) # creation of labels inside the display frame
        
        self.digits = {
            7:(1,1), 8:(1,2), 9:(1,3),
            4:(2,1), 5:(2,2), 6:(2,3),
            1:(3,1), 2:(3,2), 3:(3,3),
            0:(4,2), '.':(4,1)
        }
        self.operators = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}
        self.buttons_frame = create_buttons_frame(self.window) # creation of button frame

        self.buttons_frame.rowconfigure(0, weight=1)
        # method to fill empty spaces in a grid
        for x in range(1,5):
            self.buttons_frame.rowconfigure(x, weight=1)
            self.buttons_frame.columnconfigure(x, weight=1)

        create_digit_buttons(self)
        create_operator_button(self)
        create_special_buttons(self)
        bind_keys(self.window, self)

    def add_to_expression(self, value):
        self.current_expression += str(value)
        self.update_label()
    
    def run(self):
        self.window.mainloop()

    def update_total_label(self):
        expression = self.total_expression
        for operator, simbolo in self.operators.items():
            expression = expression.replace(operator, f' {simbolo} ')
        self.total_label.config(text=expression)

    def update_label(self):
        self.label.config(text=self.current_expression[:11])

    def append_operator(self, operator):
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = ""
        self.update_total_label()
        self.update_label()

    def clear(self):
        self.current_expression = ""
        self.total_expression = ""
        self.update_label()
        self.update_total_label()

    def evaluate(self):
        self.total_expression += self.current_expression
        self.update_total_label()

        try:
            self.current_expression = str(eval(self.total_expression))
            self.total_expression = ""
        except Exception as e:
            self.current_expression = "Error"
        finally:
            self.update_label()

    def square(self):
        try:
            self.current_expression = str(eval(f"{self.current_expression}**2"))
        except Exception as e:
            self.current_expression = "Error"
        finally:
            self.update_label()

    def sqrt(self):
        try:
            self.current_expression = str(eval(f"{self.current_expression}**0.5"))
        except Exception as e:
            self.current_expression = "Error"
        finally:
            self.update_label()

if __name__ == "__main__":
    calc = Calculator()
    calc.run()