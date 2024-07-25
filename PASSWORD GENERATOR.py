import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate password
def generate_password():
    try:
        length = int(length_entry.get())
        if length < 1:
            messagebox.showerror("Invalid Input", "Password length must be at least 1.")
            return

        # Define character sets
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        digits = string.digits
        symbols = string.punctuation

        # Combine all character sets
        all_characters = lower + upper + digits + symbols

        # Generate the password
        password = ''.join(random.choice(all_characters) for _ in range(length))
        password_entry.config(state=tk.NORMAL)
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
        password_entry.config(state=tk.DISABLED)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid integer for the password length.")

# Function to copy password to clipboard
def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_entry.get())
    messagebox.showinfo("Success", "Password copied to clipboard!")

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Set window size
root.geometry("400x200")

# Create UI elements
length_label = tk.Label(root, text="Enter Password Length:", font=('Arial', 12))
length_label.pack(pady=10)

length_entry = tk.Entry(root, width=20, font=('Arial', 12))
length_entry.pack(pady=5)

generate_button = tk.Button(root, text="Generate Password", command=generate_password, font=('Arial', 12))
generate_button.pack(pady=10)

password_entry = tk.Entry(root, width=40, font=('Arial', 12), state=tk.DISABLED)
password_entry.pack(pady=5)

copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, font=('Arial', 12))
copy_button.pack(pady=10)

# Run the main event loop
root.mainloop()
