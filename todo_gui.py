import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("CodSoft - To-Do List")
root.geometry("400x480")
root.config(bg="#f4f4f9")

tasks = []


def add_task():
    task = entry.get().strip()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")


def update_task():
    try:
        index = listbox.curselection()[0]
        new_task = entry.get().strip()
        if new_task:
            listbox.delete(index)
            listbox.insert(index, new_task)
            entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Enter updated text in the box!")
    except IndexError:
        messagebox.showwarning("Warning", "Select a task to update!")


def mark_done():
    try:
        index = listbox.curselection()[0]
        task = listbox.get(index)
        if not task.startswith("✔ "):
            listbox.delete(index)
            listbox.insert(index, "✔ " + task)
            listbox.itemconfig(index, fg="green")
    except IndexError:
        messagebox.showwarning("Warning", "Select a task to mark done!")


def delete_task():
    try:
        index = listbox.curselection()[0]
        listbox.delete(index)
    except IndexError:
        messagebox.showwarning("Warning", "Select a task to delete!")


tk.Label(
    root, text="My To-Do List", font=("Arial", 16, "bold"), bg="#f4f4f9"
).pack(pady=10)

entry = tk.Entry(root, font=("Arial", 12), width=30)
entry.pack(pady=5)

btn_frame = tk.Frame(root, bg="#f4f4f9")
btn_frame.pack(pady=10)

tk.Button(
    btn_frame,
    text="Add",
    width=8,
    bg="#4caf50",
    fg="white",
    command=add_task,
).grid(row=0, column=0, padx=4)
tk.Button(
    btn_frame,
    text="Update",
    width=8,
    bg="#2196f3",
    fg="white",
    command=update_task,
).grid(row=0, column=1, padx=4)
tk.Button(
    btn_frame,
    text="Done",
    width=8,
    bg="#ff9800",
    fg="white",
    command=mark_done,
).grid(row=0, column=2, padx=4)
tk.Button(
    btn_frame,
    text="Delete",
    width=8,
    bg="#f44336",
    fg="white",
    command=delete_task,
).grid(row=0, column=3, padx=4)

listbox = tk.Listbox(root, font=("Arial", 12), width=36, height=14)
listbox.pack(pady=10)

root.mainloop()
