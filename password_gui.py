import random
import string
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Pro Password Generator")
root.geometry("380x500")
root.config(bg="#0f172a")


def generate_password():
    length = length_slider.get()
    chars = string.ascii_lowercase
    if upper_var.get():
        chars += string.ascii_uppercase
    if num_var.get():
        chars += string.digits
    if sym_var.get():
        chars += "!@#$%^&*()_+-="

    if not chars:
        messagebox.showwarning("Warning", "Select at least one option!")
        return

    password = "".join(random.choice(chars) for _ in range(length))
    result_var.set(password)

    # Strength indicator
    if length < 8:
        strength_lbl.config(text="Strength: WEAK", fg="#ef4444")
    elif length < 12 or not (num_var.get() and sym_var.get()):
        strength_lbl.config(text="Strength: MEDIUM", fg="#f59e0b")
    else:
        strength_lbl.config(text="Strength: STRONG", fg="#10b981")


def copy_password():
    pwd = result_var.get()
    if pwd:
        root.clipboard_clear()
        root.clipboard_append(pwd)
        copy_btn.config(text="✔ COPIED!", bg="#10b981")
        root.after(
            1500, lambda: copy_btn.config(text="COPY PASSWORD", bg="#3b82f6")
        )


# Title
tk.Label(
    root,
    text="PASSWORD GENERATOR",
    font=("Arial", 16, "bold"),
    bg="#0f172a",
    fg="#38bdf8",
).pack(pady=(20, 10))

# Output Box
result_var = tk.StringVar()
out_entry = tk.Entry(
    root,
    textvariable=result_var,
    font=("Courier", 14, "bold"),
    bg="#1e293b",
    fg="#f8fafc",
    bd=0,
    justify="center",
    state="readonly",
    readonlybackground="#1e293b",
)
out_entry.pack(fill="x", padx=25, ipady=14, pady=8)

strength_lbl = tk.Label(
    root, text="Strength: ---", font=("Arial", 10, "bold"), bg="#0f172a", fg="#94a3b8"
)
strength_lbl.pack(pady=(0, 10))

# Card Frame
card = tk.Frame(root, bg="#1e293b", padx=20, pady=15)
card.pack(fill="x", padx=25, pady=5)

tk.Label(
    card,
    text="Password Length",
    font=("Arial", 11, "bold"),
    bg="#1e293b",
    fg="#e2e8f0",
).pack(anchor="w")

length_slider = tk.Scale(
    card,
    from_=6,
    to=24,
    orient="horizontal",
    bg="#1e293b",
    fg="#38bdf8",
    highlightthickness=0,
    troughcolor="#0f172a",
    activebackground="#38bdf8",
)
length_slider.set(12)
length_slider.pack(fill="x", pady=(2, 12))

upper_var = tk.BooleanVar(value=True)
num_var = tk.BooleanVar(value=True)
sym_var = tk.BooleanVar(value=True)

for text, var in [
    ("Uppercase Letters (A-Z)", upper_var),
    ("Numbers (0-9)", num_var),
    ("Special Symbols (@#$%)", sym_var),
]:
    tk.Checkbutton(
        card,
        text=text,
        variable=var,
        font=("Arial", 10),
        bg="#1e293b",
        fg="#cbd5e1",
        selectcolor="#0f172a",
        activebackground="#1e293b",
        activeforeground="#38bdf8",
    ).pack(anchor="w", pady=3)

# Buttons
tk.Button(
    root,
    text="GENERATE PASSWORD",
    font=("Arial", 11, "bold"),
    bg="#6366f1",
    fg="white",
    bd=0,
    cursor="hand2",
    command=generate_password,
).pack(fill="x", padx=25, ipady=10, pady=(18, 8))

copy_btn = tk.Button(
    root,
    text="COPY PASSWORD",
    font=("Arial", 11, "bold"),
    bg="#3b82f6",
    fg="white",
    bd=0,
    cursor="hand2",
    command=copy_password,
)
copy_btn.pack(fill="x", padx=25, ipady=10)

generate_password()
root.mainloop()

