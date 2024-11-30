calculation = ""

def add_to_calculation(symbol, text_widget):
    global calculation
    calculation += str(symbol)
    text_widget.delete(1.0, "end")
    text_widget.insert(1.0, calculation)

def evaluate_calculation(text_widget):
    global calculation
    try:
        calculation = str(eval(calculation))
        text_widget.delete(1.0, "end")
        text_widget.insert(1.0, calculation)
    except:
        clear_field(text_widget)
        text_widget.insert(1.0, "Error")

def clear_field(text_widget):
    global calculation
    calculation = ""
    text_widget.delete(1.0, "end")