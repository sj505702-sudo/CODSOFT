import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Pro Contact Book")
root.geometry("420x580")
root.config(bg="#0f172a")

contacts = {}


def refresh_list(filter_text=""):
    listbox.delete(0, tk.END)
    for name, info in contacts.items():
        if (
            filter_text.lower() in name.lower()
            or filter_text in info["phone"]
        ):
            listbox.insert(tk.END, f"  {name}  |  {info['phone']}")


def clear_fields():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    addr_entry.delete(0, tk.END)


def add_contact():
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    email = email_entry.get().strip()
    addr = addr_entry.get().strip()

    if not name or not phone:
        messagebox.showwarning("Warning", "Name aur Phone zaroori hain!")
        return

    contacts[name] = {"phone": phone, "email": email, "addr": addr}
    refresh_list()
    clear_fields()


def update_contact():
    name = name_entry.get().strip()
    if name in contacts:
        contacts[name] = {
            "phone": phone_entry.get().strip(),
            "email": email_entry.get().strip(),
            "addr": addr_entry.get().strip(),
        }
        refresh_list()
        clear_fields()
        messagebox.showinfo("Updated", "Contact update ho gaya!")
    else:
        messagebox.showwarning(
            "Warning", "List se contact select karo ya sahi Name likho!"
        )


def delete_contact():
    try:
        selected = listbox.get(listbox.curselection())
        name = selected.split("|")[0].strip()
        del contacts[name]
        refresh_list()
        clear_fields()
    except IndexError:
        messagebox.showwarning("Warning", "Delete karne ke liye contact select karo!")


def on_select(event):
    try:
        selected = listbox.get(listbox.curselection())
        name = selected.split("|")[0].strip()
        info = contacts[name]
        clear_fields()
        name_entry.insert(0, name)
        phone_entry.insert(0, info["phone"])
        email_entry.insert(0, info["email"])
        addr_entry.insert(0, info["addr"])
    except Exception:
        pass


# Title
tk.Label(
    root,
    text="CONTACT BOOK",
    font=("Arial", 16, "bold"),
    bg="#0f172a",
    fg="#38bdf8",
).pack(pady=(15, 8))

# Input Card
form = tk.Frame(root, bg="#1e293b", padx=15, pady=12)
form.pack(fill="x", padx=20)

fields = ["Name*", "Phone*", "Email", "Address"]
entries = {}

for i, label in enumerate(fields):
    tk.Label(
        form, text=label, font=("Arial", 9, "bold"), bg="#1e293b", fg="#cbd5e1"
    ).grid(row=i, column=0, sticky="w", pady=4)
    ent = tk.Entry(
        form,
        font=("Arial", 10),
        bg="#0f172a",
        fg="#f8fafc",
        insertbackground="white",
        bd=0,
    )
    ent.grid(row=i, column=1, sticky="ew", padx=(10, 0), pady=4, ipady=4)
    entries[label] = ent

form.columnconfigure(1, weight=1)
name_entry, phone_entry, email_entry, addr_entry = (
    entries["Name*"],
    entries["Phone*"],
    entries["Email"],
    entries["Address"],
)

# Buttons
btn_frame = tk.Frame(root, bg="#0f172a")
btn_frame.pack(fill="x", padx=20, pady=10)

for idx, (text, color, cmd) in enumerate(
    [
        ("ADD", "#10b981", add_contact),
        ("UPDATE", "#3b82f6", update_contact),
        ("DELETE", "#ef4444", delete_contact),
        ("CLEAR", "#475569", clear_fields),
    ]
):
    btn_frame.columnconfigure(idx, weight=1)
    tk.Button(
        btn_frame,
        text=text,
        font=("Arial", 9, "bold"),
        bg=color,
        fg="white",
        bd=0,
        cursor="hand2",
        command=cmd,
    ).grid(row=0, column=idx, sticky="ew", padx=3, ipady=6)

# Search Box
search_var = tk.StringVar()
search_var.trace(
    "w", lambda *args: refresh_list(search_var.get().strip())
)
tk.Entry(
    root,
    textvariable=search_var,
    font=("Arial", 10),
    bg="#1e293b",
    fg="#38bdf8",
    insertbackground="white",
    bd=0,
).pack(fill="x", padx=20, ipady=6, pady=(0, 8))
search_var.set("")

# Listbox
listbox = tk.Listbox(
    root,
    font=("Arial", 11),
    bg="#1e293b",
    fg="#f8fafc",
    selectbackground="#334155",
    selectforeground="#38bdf8",
    bd=0,
    highlightthickness=0,
)
listbox.pack(fill="both", expand=True, padx=20, pady=(0, 15))
listbox.bind("<<ListboxSelect>>", on_select)

root.mainloop()
      
