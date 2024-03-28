import tkinter as tk
import string
import random

def generate_password():
    # Getting password length
    password_length = int(length_entry.get())

    # Clear previous password
    password_var.set("")

    # Create character set for password
    character_set = ""
    if digit_var.get():
        character_set += string.digits
    if letter_var.get():
        character_set += string.ascii_letters
    if special_var.get():
        character_set += string.punctuation

    if not character_set:
        password_var.set("Please select at least one character set")
        return

    # Generate password
    password = ''.join(random.choices(character_set, k=password_length))
    password_var.set(password)

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Label and entry for password length
length_label = tk.Label(root, text="Password Length:")
length_label.grid(row=0, column=0)
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1)

# Checkboxes for character sets
digit_var = tk.BooleanVar()
digit_check = tk.Checkbutton(root, text="Digits", variable=digit_var)
digit_check.grid(row=1, column=0, sticky="W")

letter_var = tk.BooleanVar()
letter_check = tk.Checkbutton(root, text="Letters", variable=letter_var)
letter_check.grid(row=2, column=0, sticky="W")

special_var = tk.BooleanVar()
special_check = tk.Checkbutton(root, text="Special Characters", variable=special_var)
special_check.grid(row=3, column=0, sticky="W")

# Button to generate password
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=4, column=0, columnspan=2)

# Display the generated password
password_var = tk.StringVar()
password_label = tk.Label(root, textvariable=password_var)
password_label.grid(row=5, column=0, columnspan=2)

# Start the GUI event loop
root.mainloop()
