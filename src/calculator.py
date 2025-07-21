import tkinter as tk
from tkinter import messagebox

def click(event):
    current = display_var.get()
    text = event.widget["text"]

    if text == "C":
        display_var.set("")
    elif text == "=":
        try:
            result = eval(current)
            display_var.set(result)
        except Exception:
            messagebox.showerror("Error", "Invalid Expression")
            display_var.set("")
    elif text == "%":
        # Find last operator (+, -, *, /)
        for op in ['+', '-', '*', '/']:
            if op in current:
                parts = current.rsplit(op, 1)
                try:
                    base = float(parts[0])
                    percent = float(parts[1])
                    if op == '+':
                        value = base + (base * percent / 100)
                    elif op == '-':
                        value = base - (base * percent / 100)
                    elif op == '*':
                        value = base * (percent / 100)
                    elif op == '/':
                        if percent == 0:
                            raise ZeroDivisionError
                        value = base / (percent / 100)
                    display_var.set(str(value))
                except Exception:
                    messagebox.showerror("Error", "Invalid Percentage Expression")
                    display_var.set("")
                return
        # If no operator, just divide by 100
        try:
            value = float(current) / 100
            display_var.set(str(value))
        except Exception:
            messagebox.showerror("Error", "Invalid Percentage Expression")
            display_var.set("")
    else:
        display_var.set(current + text)

root = tk.Tk()
root.title("Python Calculator")
root.resizable(False, False)

display_var = tk.StringVar()
display = tk.Entry(root, textvariable=display_var, font=("Arial", 20), bd=10, relief=tk.RIDGE, justify="right", width=18)
display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

buttons = [
    ['C', '', '', '/'],
    ['7', '8', '9', '*'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '+'],
    ['0', '.', '%', '=']
]

for r, row in enumerate(buttons, 1):
    for c, char in enumerate(row):
        if char == '':
            continue
        btn = tk.Button(root, text=char, font=("Arial", 18), width=4, height=2)
        btn.grid(row=r, column=c, padx=3, pady=3)
        btn.bind("<Button-1>", click)

root.mainloop()