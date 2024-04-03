import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import re

class ContactManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Manager")
        
        # Create a treeview to display contacts
        self.tree = ttk.Treeview(self.root, columns=("Name", "Phone", "Email"))
        self.tree.heading("#0", text="ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Phone", text="Phone")
        self.tree.heading("Email", text="Email")
        self.tree.pack()
        
        # Add entry fields for adding new contacts
        self.name_entry = ttk.Entry(self.root)
        self.name_entry.pack()
        self.phone_entry = ttk.Entry(self.root)
        self.phone_entry.pack()
        self.email_entry = ttk.Entry(self.root)
        self.email_entry.pack()
        
        # Add a button to add a new contact
        self.add_button = ttk.Button(self.root, text="Add Contact", command=self.add_contact)
        self.add_button.pack()
        
    def add_contact(self):
        # Get input values
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        
        # Validate phone number
        if not re.match(r'^\d{10}$', phone):
            messagebox.showerror("Error", "Invalid phone number")
            return
        
        # Validate email address
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            messagebox.showerror("Error", "Invalid email address")
            return
        
        # Add contact to treeview
        self.tree.insert("", "end", text="1", values=(name, phone, email))
        
# Create the main Tkinter window
root = tk.Tk()

# Create the ContactManagerApp instance
app = ContactManagerApp(root)

# Run the Tkinter event loop
root.mainloop()
