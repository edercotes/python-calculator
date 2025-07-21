import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

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
        try:
            value = float(current) / 100
            display_var.set(str(value))
        except Exception:
            messagebox.showerror("Error", "Invalid Percentage Expression")
            display_var.set("")
    else:
        display_var.set(current + text)

root = tk.Tk()
root.title("Mac Style Calculator")
root.resizable(False, False)
root.configure(bg="#222")

# Use clam theme for rounded buttons
style = ttk.Style(root)
style.theme_use('clam')

# Base button style
style.configure("TButton",
    font=("Helvetica Neue", 20),
    padding=10,
    borderwidth=0,
    focusthickness=3,
    focuscolor='none',
    background="#333",
    foreground="#fff"
)

# Operator style
style.configure("Operator.TButton", background="#ff9500", foreground="#fff")
# Equals style
style.configure("Equals.TButton", background="#34c759", foreground="#fff")
# Clear style
style.configure("Clear.TButton", background="#ff3b30", foreground="#fff")
# Percent style
style.configure("Percent.TButton", background="#a6a6a6", foreground="#222")

display_var = tk.StringVar()
display = tk.Entry(root, textvariable=display_var, font=("Helvetica Neue", 28), bd=0, relief=tk.FLAT, justify="right", width=15, bg="#222", fg="#fff", insertbackground="#fff")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky="we")

buttons = [
    ['C', '%', '', '/'],
    ['7', '8', '9', '*'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '+'],
    ['0', '.', '=', '']
]

style_map = {
    '/': "Operator.TButton",
    '*': "Operator.TButton",
    '-': "Operator.TButton",
    '+': "Operator.TButton",
    '=': "Equals.TButton",
    'C': "Clear.TButton",
    '%': "Percent.TButton"
}

for r, row in enumerate(buttons, 1):
    for c, char in enumerate(row):
        if char == '':
            continue
        btn_style = style_map.get(char, "TButton")
        btn = ttk.Button(root, text=char, style=btn_style)
        btn.grid(row=r, column=c, padx=6, pady=6, sticky="nsew")
        btn.bind("<Button-1>", click)
        btn.configure(cursor="hand2", takefocus=0, width=4)

for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
