import tkinter as tk
from tkinter.messagebox import showerror
from tkinter import *

# Set up the window
window = tk.Tk()
window.title("Temperature Converter")
window.geometry('420x650')
window.option_add('*Font', '25')
window.option_add('*Font', 'Tahoma')
window.configure(bg='#f8f8f8')
window.resizable(0, 0)
window.iconbitmap('temperature-converter.ico')

###################################
#### Fahrenheit to Celsius ####
###################################

def fahrenheit_to_celsius():
    fahrenheit = fahrenheit_to_celsius_entry_temperature.get()
    if fahrenheit == '':
        showerror(title='Empty Field Error', message="Field is empty. Please input number.")
    else:
        try:
            celsius = (5 / 9) * (float(fahrenheit) - 32)
            fahrenheit_to_celsius_label_result["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"
        except:
            showerror(title='Input Error', message="Invalid input. Please input only number.")

fahrenheit_to_celsius_label_heading = tk.Label(text="Fahrenheit to Celsius:", bg='#f8f8f8', fg='Black')

fahrenheit_to_celsius_frame_entry = tk.Frame(master=window)
fahrenheit_to_celsius_entry_temperature = tk.Entry(master=fahrenheit_to_celsius_frame_entry, width=10)
fahrenheit_to_celsius_label_temperature = tk.Label(master=fahrenheit_to_celsius_frame_entry, text="\N{DEGREE FAHRENHEIT}")

def fahrenheit_to_celsius_clear():
    fahrenheit_to_celsius_entry_temperature.delete(0, tk.END)
    fahrenheit_to_celsius_label_result.config(text="\N{DEGREE CELSIUS}")

fahrenheit_to_celsius_button_clear = tk.Button(window, text="Clear", command=fahrenheit_to_celsius_clear, bg='#c82333', fg='White')

fahrenheit_to_celsius_label_heading.grid(row=0, column=0, columnspan=3, sticky="w")
fahrenheit_to_celsius_entry_temperature.grid(row=1, column=0, sticky="ew")
fahrenheit_to_celsius_label_temperature.grid(row=1, column=1, sticky="ew")
fahrenheit_to_celsius_button_clear.grid(row=1, column=2, sticky="w")


fahrenheit_to_celsius_button_convert = tk.Button(master=window, text="Convert", command=fahrenheit_to_celsius, bg='#218838', fg='White')
fahrenheit_to_celsius_label_result = tk.Label(master=window, text="\N{DEGREE CELSIUS}")

fahrenheit_to_celsius_label_heading.grid(row=0, padx=10, pady=10)
fahrenheit_to_celsius_frame_entry.grid(row=1, column=0, padx=12, sticky="ew")
fahrenheit_to_celsius_button_convert.grid(row=1, column=1, padx=0, sticky="ew")
fahrenheit_to_celsius_button_clear.grid(row=1, column=2, padx=(5,0), sticky="ew")
fahrenheit_to_celsius_label_result.grid(row=1, column=3, padx=0, sticky="w")



###################################
#### Celsius to Fahrenheit ####
###################################

def celsius_to_fahrenheit():
    celsius = celsius_to_fahrenheit_entry_temperature.get()
    if celsius == '':
        showerror(title='Empty Field Error', message="Field is empty. Please input number.")
    else:
        try:
            fahrenheit = (float(celsius) * (9/5)) + 32
            celsius_to_fahrenheit_label_result["text"] = f"{round(fahrenheit, 2)} \N{DEGREE FAHRENHEIT}"
        except:
            showerror(title='Input Error', message="Invalid input. Please input only number.")

celsius_to_fahrenheit_label_heading = tk.Label(text="Celsius to Fahrenheit:", bg='#f8f8f8', fg='Black')

celsius_to_fahrenheit_frame_entry = tk.Frame(master=window)
celsius_to_fahrenheit_entry_temperature = tk.Entry(master=celsius_to_fahrenheit_frame_entry, width=10)
celsius_to_fahrenheit_label_temperature = tk.Label(master=celsius_to_fahrenheit_frame_entry, text="\N{DEGREE CELSIUS}")

def celsius_to_fahrenheit_clear():
    celsius_to_fahrenheit_entry_temperature.delete(0, tk.END)
    celsius_to_fahrenheit_label_result.config(text="\N{DEGREE FAHRENHEIT}")

celsius_to_fahrenheit_button_clear = tk.Button(window, text="Clear", command=celsius_to_fahrenheit_clear, bg='#c82333', fg='White')

celsius_to_fahrenheit_label_heading.grid(row=2, column=0, columnspan=3, sticky="w")
celsius_to_fahrenheit_entry_temperature.grid(row=3, column=0, sticky="ew")
celsius_to_fahrenheit_label_temperature.grid(row=3, column=1, sticky="ew")
celsius_to_fahrenheit_button_clear.grid(row=3, column=2, sticky="w")

celsius_to_fahrenheit_button_convert = tk.Button(master=window, text="Convert", command=celsius_to_fahrenheit, bg='#218838', fg='White')
celsius_to_fahrenheit_label_result = tk.Label(master=window, text="\N{DEGREE FAHRENHEIT}")

celsius_to_fahrenheit_label_heading.grid(row=2, padx=10, pady=10)
celsius_to_fahrenheit_frame_entry.grid(row=3, column=0, padx=12, sticky="ew")
celsius_to_fahrenheit_button_convert.grid(row=3, column=1, padx=0, sticky="ew")
celsius_to_fahrenheit_button_clear.grid(row=3, column=2, padx=(5,0), sticky="ew")
celsius_to_fahrenheit_label_result.grid(row=3, column=3, padx=0, sticky="w")



# ###################################
# #### Fahrenheit to Kelvin ####
# ##################################

def fahrenheit_to_kelvin():
    fahrenheit = fahrenheit_to_kelvin_entry_temperature.get()
    if fahrenheit == '':
        showerror(title='Empty Field Error', message="Field is empty. Please input number.")
    else:
        try:
            kelvin = (float(fahrenheit) + 459.67) * 5/9
            fahrenheit_to_kelvin_label_result["text"] = f"{round(kelvin, 2)} \N{DEGREE SIGN}K"
        except:
            showerror(title='Input Error', message="Invalid input. Please input only number.")

fahrenheit_to_kelvin_label_heading = tk.Label(text="Fahrenheit to Kelvin:", bg='#f8f8f8', fg='Black')

fahrenheit_to_kelvin_frame_entry = tk.Frame(master=window)
fahrenheit_to_kelvin_entry_temperature = tk.Entry(master=fahrenheit_to_kelvin_frame_entry, width=10)
fahrenheit_to_kelvin_label_temperature = tk.Label(master=fahrenheit_to_kelvin_frame_entry, text="\N{DEGREE FAHRENHEIT}")

def fahrenheit_to_kelvin_clear():
    fahrenheit_to_kelvin_entry_temperature.delete(0, tk.END)
    fahrenheit_to_kelvin_label_result.config(text="\N{DEGREE SIGN}K")

fahrenheit_to_kelvin_button_clear = tk.Button(window, text="Clear", command=fahrenheit_to_kelvin_clear, bg='#c82333', fg='White')

fahrenheit_to_kelvin_label_heading.grid(row=4, column=0, columnspan=3, sticky="w")
fahrenheit_to_kelvin_entry_temperature.grid(row=5, column=0, sticky="ew")
fahrenheit_to_kelvin_label_temperature.grid(row=5, column=1, sticky="ew")
fahrenheit_to_kelvin_button_clear.grid(row=5, column=2, sticky="w")

fahrenheit_to_kelvin_button_convert = tk.Button(master=window, text="Convert", command=fahrenheit_to_kelvin, bg='#218838', fg='White')
fahrenheit_to_kelvin_label_result = tk.Label(master=window, text="\N{DEGREE SIGN}K")

fahrenheit_to_kelvin_label_heading.grid(row=4, padx=10, pady=10)
fahrenheit_to_kelvin_frame_entry.grid(row=5, column=0, padx=12, sticky="ew")
fahrenheit_to_kelvin_button_convert.grid(row=5, column=1, padx=0, sticky="ew")
fahrenheit_to_kelvin_button_clear.grid(row=5, column=2, padx=(5,0), sticky="ew")
fahrenheit_to_kelvin_label_result.grid(row=5, column=3, padx=0, sticky="w")


# ###################################
# #### Kelvin to Fahrenheit ####
# ##################################

def kelvin_to_fahrenheit():
    kelvin = kelvin_to_fahrenheit_entry_temperature.get()
    if kelvin == '':
        showerror(title='Empty Field Error', message="Field is empty. Please input number.")
    else:
        try:
            fahrenheit = 1.8 * (float(kelvin) - 273) + 32
            kelvin_to_fahrenheit_label_result["text"] = f"{round(fahrenheit, 2)} \N{DEGREE FAHRENHEIT}"
        except:
            showerror(title='Input Error', message="Invalid input. Please input only number.")

kelvin_to_fahrenheit_label_heading = tk.Label(text="Kelvin to Fahrenheit:", bg='#f8f8f8', fg='Black')

kelvin_to_fahrenheit_frame_entry = tk.Frame(master=window)
kelvin_to_fahrenheit_entry_temperature = tk.Entry(master=kelvin_to_fahrenheit_frame_entry, width=10)
kelvin_to_fahrenheit_label_temperature = tk.Label(master=kelvin_to_fahrenheit_frame_entry, text="\N{DEGREE SIGN}K")

def kelvin_to_fahrenheit_clear():
    kelvin_to_fahrenheit_entry_temperature.delete(0, tk.END)
    kelvin_to_fahrenheit_label_result.config(text="\N{DEGREE FAHRENHEIT}")

kelvin_to_fahrenheit_button_clear = tk.Button(window, text="Clear", command=kelvin_to_fahrenheit_clear, bg='#c82333', fg='White')

kelvin_to_fahrenheit_label_heading.grid(row=6, column=0, columnspan=3, sticky="w")
kelvin_to_fahrenheit_entry_temperature.grid(row=7, column=0, sticky="ew")
kelvin_to_fahrenheit_label_temperature.grid(row=7, column=1, sticky="ew")
kelvin_to_fahrenheit_button_clear.grid(row=7, column=2, sticky="w")

kelvin_to_fahrenheit_button_convert = tk.Button(master=window, text="Convert", command=kelvin_to_fahrenheit, bg='#218838', fg='White')
kelvin_to_fahrenheit_label_result = tk.Label(master=window, text="\N{DEGREE FAHRENHEIT}")

kelvin_to_fahrenheit_label_heading.grid(row=6, padx=10, pady=10)
kelvin_to_fahrenheit_frame_entry.grid(row=7, column=0, padx=12, sticky="ew")
kelvin_to_fahrenheit_button_convert.grid(row=7, column=1, padx=0, sticky="ew")
kelvin_to_fahrenheit_button_clear.grid(row=7, column=2, padx=(5,0), sticky="ew")
kelvin_to_fahrenheit_label_result.grid(row=7, column=3, padx=0, sticky="w")


###################################
#### Celsius to Kelvin ####
##################################

def celsius_to_kelvin():
    celsius = celsius_to_kelvin_entry_temperature.get()
    if celsius == '':
        showerror(title='Empty Field Error', message="Field is empty. Please input number.")
    else:
        try:
            kelvin = float(celsius) + 273.15
            celsius_to_kelvin_label_result["text"] = f"{round(kelvin, 2)} \N{DEGREE SIGN}K"
        except:
            showerror(title='Input Error', message="Invalid input. Please input only number.")

celsius_to_kelvin_label_heading = tk.Label(text="Celsius to Kelvin:", bg='#f8f8f8', fg='Black')

celsius_to_kelvin_frame_entry = tk.Frame(master=window)
celsius_to_kelvin_entry_temperature = tk.Entry(master=celsius_to_kelvin_frame_entry, width=10)
celsius_to_kelvin_label_temperature = tk.Label(master=celsius_to_kelvin_frame_entry, text="\N{DEGREE CELSIUS}")

def celsius_to_kelvin_clear():
    celsius_to_kelvin_entry_temperature.delete(0, tk.END)
    celsius_to_kelvin_label_result.config(text="\N{DEGREE SIGN}K")

celsius_to_kelvin_button_clear = tk.Button(window, text="Clear", command=celsius_to_kelvin_clear, bg='#c82333', fg='White')

celsius_to_kelvin_label_heading.grid(row=8, column=0, columnspan=3, sticky="w")
celsius_to_kelvin_entry_temperature.grid(row=9, column=0, sticky="ew")
celsius_to_kelvin_label_temperature.grid(row=9, column=1, sticky="ew")
celsius_to_kelvin_button_clear.grid(row=9, column=2, sticky="w")

celsius_to_kelvin_button_convert = tk.Button(master=window, text="Convert", command=celsius_to_kelvin, bg='#218838', fg='White')
celsius_to_kelvin_label_result = tk.Label(master=window, text="\N{DEGREE SIGN}K")

celsius_to_kelvin_label_heading.grid(row=8, padx=10, pady=10)
celsius_to_kelvin_frame_entry.grid(row=9, column=0, padx=12, sticky="ew")
celsius_to_kelvin_button_convert.grid(row=9, column=1, padx=0, sticky="ew")
celsius_to_kelvin_button_clear.grid(row=9, column=2, padx=(5,0), sticky="ew")
celsius_to_kelvin_label_result.grid(row=9, column=3, padx=0, sticky="w")


###################################
#### Kelvin to Celsius ####
##################################

def kelvin_to_celsius():
    kelvin = kelvin_to_celsius_entry_temperature.get()
    if kelvin == '':
        showerror(title='Empty Field Error', message="Field is empty. Please input number.")
    else:
        try:
            celsius = float(kelvin) - 273.15
            kelvin_to_celsius_label_result["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"
        except:
            showerror(title='Input Error', message="Invalid input. Please input only number.")

kelvin_to_celsius_label_heading = tk.Label(text="Kelvin to Celsius:", bg='#f8f8f8', fg='Black')

kelvin_to_celsius_frame_entry = tk.Frame(master=window)
kelvin_to_celsius_entry_temperature = tk.Entry(master=kelvin_to_celsius_frame_entry, width=10)
kelvin_to_celsius_label_temperature = tk.Label(master=kelvin_to_celsius_frame_entry, text="\N{DEGREE SIGN}K")

def kelvin_to_celsius_clear():
    kelvin_to_celsius_entry_temperature.delete(0, tk.END)
    kelvin_to_celsius_label_result.config(text="\N{DEGREE CELSIUS}")

kelvin_to_celsius_button_clear = tk.Button(window, text="Clear", command=kelvin_to_celsius_clear, bg='#c82333', fg='White')

kelvin_to_celsius_label_heading.grid(row=10, column=0, columnspan=3, sticky="w")
kelvin_to_celsius_entry_temperature.grid(row=11, column=0, sticky="ew")
kelvin_to_celsius_label_temperature.grid(row=11, column=1, sticky="ew")
kelvin_to_celsius_button_clear.grid(row=11, column=2, sticky="w")

kelvin_to_celsius_button_convert = tk.Button(master=window, text="Convert", command=kelvin_to_celsius, bg='#218838', fg='White')
kelvin_to_celsius_label_result = tk.Label(master=window, text="\N{DEGREE CELSIUS}")

kelvin_to_celsius_label_heading.grid(row=10, padx=10, pady=10)
kelvin_to_celsius_frame_entry.grid(row=11, column=0, padx=12, sticky="ew")
kelvin_to_celsius_button_convert.grid(row=11, column=1, padx=0, sticky="ew")
kelvin_to_celsius_button_clear.grid(row=11, column=2, padx=(5,0), sticky="ew")
kelvin_to_celsius_label_result.grid(row=11, column=3, padx=0, sticky="w")

def close_app():
   window.destroy()
button_close = tk.Button(window, text="Close App", command=close_app, bg='#c82333', fg='White')
button_close.grid(row=12, column=0, columnspan=10,  padx=10, pady=40, sticky="nsew")

window.mainloop()