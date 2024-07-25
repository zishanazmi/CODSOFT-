import tkinter as tk
from tkinter import messagebox

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}, Address: {self.address}"

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address):
        new_contact = Contact(name, phone, email, address)
        self.contacts.append(new_contact)

    def get_contacts(self):
        return self.contacts

    def search_contact(self, query):
        return [contact for contact in self.contacts if query.lower() in contact.name.lower() or query in contact.phone]

    def update_contact(self, original_name, name, phone, email, address):
        for contact in self.contacts:
            if contact.name.lower() == original_name.lower():
                contact.name = name
                contact.phone = phone
                contact.email = email
                contact.address = address
                return True
        return False

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                return True
        return False

class ContactApp(tk.Tk):
    def __init__(self, manager):
        super().__init__()
        self.manager = manager
        self.title("Contact Management System")
        self.geometry("400x400")
        self.create_widgets()

    def create_widgets(self):
        # Entry fields
        self.label_name = tk.Label(self, text="Name")
        self.label_name.pack()
        self.entry_name = tk.Entry(self)
        self.entry_name.pack()

        self.label_phone = tk.Label(self, text="Phone")
        self.label_phone.pack()
        self.entry_phone = tk.Entry(self)
        self.entry_phone.pack()

        self.label_email = tk.Label(self, text="Email")
        self.label_email.pack()
        self.entry_email = tk.Entry(self)
        self.entry_email.pack()

        self.label_address = tk.Label(self, text="Address")
        self.label_address.pack()
        self.entry_address = tk.Entry(self)
        self.entry_address.pack()

        # Buttons
        self.button_add = tk.Button(self, text="Add Contact", command=self.add_contact)
        self.button_add.pack()

        self.button_view = tk.Button(self, text="View Contacts", command=self.view_contacts)
        self.button_view.pack()

        self.button_search = tk.Button(self, text="Search Contact", command=self.search_contact)
        self.button_search.pack()

        self.button_update = tk.Button(self, text="Update Contact", command=self.update_contact)
        self.button_update.pack()

        self.button_delete = tk.Button(self, text="Delete Contact", command=self.delete_contact)
        self.button_delete.pack()

    def add_contact(self):
        name = self.entry_name.get()
        phone = self.entry_phone.get()
        email = self.entry_email.get()
        address = self.entry_address.get()
        if name and phone:
            self.manager.add_contact(name, phone, email, address)
            messagebox.showinfo("Success", "Contact added successfully!")
            self.clear_entries()
        else:
            messagebox.showwarning("Input Error", "Name and Phone are required fields!")

    def view_contacts(self):
        contacts = self.manager.get_contacts()
        contacts_str = "\n".join(str(contact) for contact in contacts)
        messagebox.showinfo("Contact List", contacts_str if contacts else "No contacts found.")

    def search_contact(self):
        query = self.entry_name.get()
        results = self.manager.search_contact(query)
        results_str = "\n".join(str(contact) for contact in results)
        messagebox.showinfo("Search Results", results_str if results else "No matching contacts found.")

    def update_contact(self):
        original_name = self.entry_name.get()
        name = self.entry_name.get()
        phone = self.entry_phone.get()
        email = self.entry_email.get()
        address = self.entry_address.get()
        if original_name and name and phone:
            if self.manager.update_contact(original_name, name, phone, email, address):
                messagebox.showinfo("Success", "Contact updated successfully!")
                self.clear_entries()
            else:
                messagebox.showwarning("Update Error", "Contact not found.")
        else:
            messagebox.showwarning("Input Error", "Please provide all necessary details.")

    def delete_contact(self):
        name = self.entry_name.get()
        if name:
            if self.manager.delete_contact(name):
                messagebox.showinfo("Success", "Contact deleted successfully!")
                self.clear_entries()
            else:
                messagebox.showwarning("Delete Error", "Contact not found.")
        else:
            messagebox.showwarning("Input Error", "Please provide a contact name.")

    def clear_entries(self):
        self.entry_name.delete(0, tk.END)
        self.entry_phone.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.entry_address.delete(0, tk.END)

if __name__ == "__main__":
    manager = ContactManager()
    app = ContactApp(manager)
    app.mainloop()
