# Imports From Tkinter
import tkinter as tk
from tkinter import ttk

# Setting Window
window = tk.Tk()
window.title("Currency Converter")
window.geometry("300x200")

# Setting Frames
main_menu_frame = tk.Frame(window, width=300, height=200)
main_menu_frame.grid(row=0, column=0)
currency_converter_frame = tk.Frame(window, width=300, height=200)
currency_converter_frame.grid(row=1, column=0)
currency_converter_frame.grid_forget()
language_selector_frame = tk.Frame(window, width=300, height=200)
language_selector_frame.grid_forget()
references_frame = tk.Frame(window, width=300, height=200)
references_frame.grid_forget()


# Setting Button Functions
def to_currency_converter():
    main_menu_frame.grid_forget()
    currency_converter_frame.grid(row=0, column=0)
    back_button = tk.Button(currency_converter_frame, text='Back', command=lambda: back(currency_converter_frame))
    back_button.grid(row=0, column=0)
    reset_button = tk.Button(currency_converter_frame, text='Reset')
    reset_button.grid(row=0, column=2)

def to_language_selector():
    main_menu_frame.grid_forget()
    language_selector_frame.grid(row=0, column=0)
    back_button = tk.Button(language_selector_frame, text='Back', command=lambda: back(language_selector_frame))
    back_button.grid(row=0, column=0)


def to_references():
    main_menu_frame.grid_forget()
    references_frame.grid(row=0, column=0)
    back_button = tk.Button(references_frame, text='Back', command=lambda: back(references_frame))
    back_button.grid(row=0, column=0)


def quit_button():
    quit()


def back(frame_name):
    frame_name.grid_forget()
    main_menu_frame.grid(row=0, column=0)


# def old_currency():


# def old_currency_amount():


# def reset():


old_currency = ["NZD", "USD"]
old_currency = ttk.Combobox(currency_converter_frame, value=old_currency, width=20)
old_currency.grid(row=2, column=2, padx=1 , pady=1)

old_currency_amount = [1, 2]
old_currency_amount = ttk.Combobox(currency_converter_frame, value=old_currency_amount, width=20)
old_currency_amount.grid(row=2, column=4, pady=1)

new_currency = ["NZD", "USD"]
new_currency = ttk.Combobox(currency_converter_frame, value=new_currency, width=20)
new_currency.grid(row=2, column=6, pady=1)

new_currency_amount = tk.Label(currency_converter_frame, text="The new currency amount")
new_currency_amount.grid(row=3, column=4, pady=15)

# Quit Button
quit_button = tk.Button(main_menu_frame, text='Quit', command=quit_button)
quit_button.grid(row=7, column=3)

# Currency Button
currency_button = tk.Button(main_menu_frame, text="Currency Converter", command=to_currency_converter)
currency_button.grid(row=3, column=2)

# Language Button
language_button = tk.Button(main_menu_frame, text="Language Selector", command=to_language_selector)
language_button.grid(row=3, column=5)

# Reference Button
reference_button = tk.Button(main_menu_frame, text="References", command=to_references)
reference_button.grid(row=7, column=6)


window.mainloop()
