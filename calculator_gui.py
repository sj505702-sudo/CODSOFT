import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("CodSoft - Calculator")
root.geometry("320x420")
root.config(bg="#222831")

expression = ""


def press(num):
    global expression
    expression += str(num)
    equation.set(expression)


def equalpress():
    global expression
    try:
        total = str(eval(expression))
        equation.set(total)
        expression = total
    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero!")
        expression = ""
        equation.set("")
    except Exception:
        messagebox.showerror("Error", "Invalid Input!")
        expression = ""
        equation.set("")


def clear():
    global expression
    expression = ""
    equation.set("")


equation = tk.StringVar()

entry = tk.Entry(
    root,
    textvariable=equation,
    font=("Arial", 20),
    bd=8,
    relief="flat",
    justify="right",
    bg="#eeeeee",
)
entry.pack(fill="x", padx=12, pady=15, ipady=10)

btn_frame = tk.Frame(root, bg="#222831")
btn_frame.pack(expand=True, fill="both", padx=10, pady=5)

buttons = [
    ("7", 0, 0),
    ("8", 0, 1),
    ("9", 0, 2),
    ("/", 0, 3),
    ("4", 1, 0),
    ("5", 1, 1),
    ("6", 1, 2),
    ("*", 1, 3),
    ("1", 2, 0),
    ("2", 2, 1),
    ("3", 2, 2),
    ("-", 2, 3),
    ("C", 3, 0),
    ("0", 3, 1),
    ("=", 3, 2),
    ("+", 3, 3),
]

for i in range(4):
    btn_frame.rowconfigure(i, weight=1)
    btn_frame.columnconfigure(i, weight=1)

for text, row, col in buttons:
    if text == "=":
        cmd = equalpress
        bg_color = "#00adb5"
    elif text == "C":
        cmd = clear
        bg_color = "#ff5722"
    elif text in ["/", "*", "-", "+"]:
        cmd = lambda t=text: press(t)
        bg_color = "#393e46"
    else:
        cmd = lambda t=text: press(t)
        bg_color = "#4e545c"

    tk.Button(
        btn_frame,
        text=text,
        font=("Arial", 16, "bold"),
        bg=bg_color,
        fg="white",
        bd=0,
        command=cmd,
    ).grid(row=row, column=col, sticky="nsew", padx=4, pady=4)

root.mainloop()
