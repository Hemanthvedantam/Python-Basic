import tkinter as tk
from math import sqrt, pow, sin, cos, tan, log, factorial, radians


def button_click(value):
    try:
        if value == "=":
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        elif value == "C":
            entry.delete(0, tk.END)
        elif value == "√":
            result = sqrt(float(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        elif value == "x²":
            result = pow(float(entry.get()), 2)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        elif value == "%":
            result = float(entry.get()) / 100
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        elif value == "sin":
            result = sin(radians(float(entry.get())))
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        elif value == "cos":
            result = cos(radians(float(entry.get())))
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        elif value == "tan":
            result = tan(radians(float(entry.get())))
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        elif value == "log":
            result = log(float(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        elif value == "!":
            result = factorial(int(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        else:
            entry.insert(tk.END, value)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

root = tk.Tk()
root.title("Advanced Calculator")


entry = tk.Entry(root, width=25, font=("Arial", 20), justify="right", bd=8, relief=tk.RIDGE)
entry.grid(row=0, column=0, columnspan=5, pady=10)

buttons = [
    "7", "8", "9", "/", "C",
    "4", "5", "6", "*", "√",
    "1", "2", "3", "-", "x²",
    "0", ".", "%", "+", "=",
    "sin", "cos", "tan", "log", "!",
]


row_val = 1
col_val = 0

for button in buttons:
    tk.Button(
        root, text=button, width=6, height=2, font=("Arial", 14), bg="lightblue",
        command=lambda b=button: button_click(b)
    ).grid(row=row_val, column=col_val, padx=5, pady=5)

    col_val += 1
    if col_val > 4:
        col_val = 0
        row_val += 1


root.mainloop()
