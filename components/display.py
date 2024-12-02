import tkinter as tk
from styles.theme import SMALL_FONT_STYLE, LARGE_FONT_STYLE, LIGHT_GRAY, LABEL_COLOR

def create_display_labels(display_frame, total_expression, current_expression):
    total_label = tk.Label(display_frame, text=total_expression, anchor=tk.E, 
                           bg=LIGHT_GRAY, fg=LABEL_COLOR, padx=24, font=SMALL_FONT_STYLE)
    total_label.pack(expand=True, fill="both")

    label = tk.Label(display_frame, text=current_expression, anchor=tk.E, 
                           bg=LIGHT_GRAY, fg=LABEL_COLOR, padx=24, font=LARGE_FONT_STYLE)
    label.pack(expand=True, fill="both")
    return total_label, label