# Welcome,This is simple random password generator using gui
import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length=12):
    if length < 4:
        raise ValueError("Password length should be at least 4 characters.")

    
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    
    all_chars = lower + upper + digits + special
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(special)
    ]

    password += random.choices(all_chars, k=length - 4)

    
    random.shuffle(password)

    return ''.join(password)

def random_pass():
    try:
        length = int(entry_length.get())
        if length < 4:
            messagebox.showerror("Error", "Password length must be at least 4 characters.")
            return

        password = generate_password(length)
        entry_password.delete(0, tk.END)
        entry_password.insert(0, password)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for the password length.")

root = tk.Tk()
root.title("Random Password Generator")

label_length = tk.Label(root, text="Password Length:")
label_length.grid(row=0, column=0, padx=10, pady=10)

entry_length = tk.Entry(root)
entry_length.grid(row=0, column=1, padx=10, pady=10)
entry_length.insert(0, "12")

button_hg = tk.Button(root, text="Generate Password", command=random_pass)
button_hg.grid(row=1, column=0, columnspan=2, pady=10)

label_password = tk.Label(root, text="Generated Password:")
label_password.grid(row=2, column=0, padx=10, pady=10)

entry_password = tk.Entry(root, width=30)
entry_password.grid(row=2, column=1, padx=10, pady=10)

root.mainloop()
