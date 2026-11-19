import random
import tkinter as tk

root = tk.Tk()
root.title("Pro Rock-Paper-Scissors")
root.geometry("400x480")
root.config(bg="#0f172a")

user_score = 0
comp_score = 0
choices = ["Rock", "Paper", "Scissors"]


def play(user_choice):
    global user_score, comp_score
    comp_choice = random.choice(choices)

    user_lbl.config(text=f"You: {user_choice}")
    comp_lbl.config(text=f"Computer: {comp_choice}")

    if user_choice == comp_choice:
        result_lbl.config(text="IT'S A TIE!", fg="#f59e0b")
    elif (
        (user_choice == "Rock" and comp_choice == "Scissors")
        or (user_choice == "Paper" and comp_choice == "Rock")
        or (user_choice == "Scissors" and comp_choice == "Paper")
    ):
        user_score += 1
        result_lbl.config(text="YOU WIN! 🎉", fg="#10b981")
    else:
        comp_score += 1
        result_lbl.config(text="COMPUTER WINS!", fg="#ef4444")

    score_lbl.config(text=f"You: {user_score}   |   Computer: {comp_score}")


def reset_game():
    global user_score, comp_score
    user_score = 0
    comp_score = 0
    score_lbl.config(text="You: 0   |   Computer: 0")
    user_lbl.config(text="You: ---")
    comp_lbl.config(text="Computer: ---")
    result_lbl.config(text="Choose your move!", fg="#94a3b8")


# Title
tk.Label(
    root,
    text="ROCK PAPER SCISSORS",
    font=("Arial", 16, "bold"),
    bg="#0f172a",
    fg="#38bdf8",
).pack(pady=(20, 10))

# Scoreboard
score_lbl = tk.Label(
    root,
    text="You: 0   |   Computer: 0",
    font=("Arial", 12, "bold"),
    bg="#1e293b",
    fg="#f8fafc",
    pady=10,
)
score_lbl.pack(fill="x", padx=25, pady=5)

# Choices Display
card = tk.Frame(root, bg="#1e293b", pady=20)
card.pack(fill="x", padx=25, pady=15)

user_lbl = tk.Label(
    card, text="You: ---", font=("Arial", 12), bg="#1e293b", fg="#cbd5e1"
)
user_lbl.pack(pady=3)

comp_lbl = tk.Label(
    card, text="Computer: ---", font=("Arial", 12), bg="#1e293b", fg="#cbd5e1"
)
comp_lbl.pack(pady=3)

result_lbl = tk.Label(
    card,
    text="Choose your move!",
    font=("Arial", 14, "bold"),
    bg="#1e293b",
    fg="#94a3b8",
)
result_lbl.pack(pady=(12, 0))

# Buttons
btn_frame = tk.Frame(root, bg="#0f172a")
btn_frame.pack(fill="x", padx=25, pady=10)

btn_data = [
    ("ROCK", "#6366f1"),
    ("PAPER", "#3b82f6"),
    ("SCISSORS", "#0ea5e9"),
]

for idx, (choice, color) in enumerate(btn_data):
    btn_frame.columnconfigure(idx, weight=1)
    tk.Button(
        btn_frame,
        text=choice,
        font=("Arial", 10, "bold"),
        bg=color,
        fg="white",
        bd=0,
        cursor="hand2",
        command=lambda c=choice.capitalize(): play(c),
    ).grid(row=0, column=idx, sticky="ew", padx=4, ipady=10)

# Reset Button
tk.Button(
    root,
    text="RESET SCORE",
    font=("Arial", 10, "bold"),
    bg="#334155",
    fg="#cbd5e1",
    bd=0,
    cursor="hand2",
    command=reset_game,
).pack(fill="x", padx=25, ipady=8, pady=15)

root.mainloop()
