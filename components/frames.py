import tkinter as tk
from styles.theme import LIGHT_GRAY

def create_display_frame(window):
    frame = tk.Frame(window, height=100, bg=LIGHT_GRAY)
    frame.pack(expand=True, fill="both")
    return frame

def create_buttons_frame(window):
    frame = tk.Frame(window)
    frame.pack(expand=True, fill="both")
    return frame