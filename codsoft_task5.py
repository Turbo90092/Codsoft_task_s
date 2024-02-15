import tkinter as tk
from tkinter import messagebox

class ContactManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Management System")

        self.address_book = []

        self.create_widgets()

    def create_widgets(self):
        # Label and Entry widgets for adding a contact
        tk.Label(self.root, text="Name:").grid(row=0, column=0, sticky="w")
        self.name_entry = tk.Entry(self.root)
        self.name_entry.grid(row=0, column=1)

        tk.Label(self.root, text="Phone Number:").grid(row=1, column=0, sticky="w")
        self.phone_entry = tk.Entry(self.root)
        self.phone_entry.grid(row=1, column=1)

        tk.Label(self.root, text="Email:").grid(row=2, column=0, sticky="w")
        self.email_entry = tk.Entry(self.root)
        self.email_entry.grid(row=2, column=1)

        tk.Label(self.root, text="Address:").grid(row=3, column=0, sticky="w")
        self.address_entry = tk.Entry(self.root)
        self.address_entry.grid(row=3, column=1)

        # Buttons for adding, viewing, searching, updating, and deleting contacts
        tk.Button(self.root, text="Add Contact", command=self.add_contact).grid(row=4, column=0, columnspan=2, pady=5)
        tk.Button(self.root, text="View Contacts", command=self.view_contacts).grid(row=5, column=0, columnspan=2, pady=5)
        tk.Button(self.root, text="Search Contact", command=self.search_contact).grid(row=6, column=0, columnspan=2, pady=5)
        tk.Button(self.root, text="Update Contact", command=self.update_contact).grid(row=7, column=0, columnspan=2, pady=5)
        tk.Button(self.root, text="Delete Contact", command=self.delete_contact).grid(row=8, column=0, columnspan=2, pady=5)

    def add_contact(self):
        name = self.name_entry.get()
        phone_number = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()
        contact = (name, phone_number, email, address)
        self.address_book.append(contact)
        messagebox.showinfo("Success", "Contact added successfully!")

    def view_contacts(self):
        if not self.address_book:
            messagebox.showinfo("Info", "No contacts found.")
            return
        contact_list = "Contact List:\n"
        for index, contact in enumerate(self.address_book, start=1):
            contact_list += f"{index}. Name: {contact[0]}, Phone: {contact[1]}\n"
        messagebox.showinfo("Contact List", contact_list)

    def search_contact(self):
        keyword = messagebox.askstring("Search Contact", "Enter name or phone number to search:")
        found_contacts = []
        for contact in self.address_book:
            if keyword.lower() in contact[0].lower() or keyword in contact[1]:
                found_contacts.append(contact)
        if found_contacts:
            contact_list = "Found contacts:\n"
            for index, contact in enumerate(found_contacts, start=1):
                contact_list += f"{index}. Name: {contact[0]}, Phone: {contact[1]}\n"
            messagebox.showinfo("Found Contacts", contact_list)
        else:
            messagebox.showinfo("Info", "No contacts found.")

    def update_contact(self):
        self.view_contacts()
        index = messagebox.askinteger("Update Contact", "Enter index of contact to update:") - 1
        if 0 <= index < len(self.address_book):
            name, phone_number, email, address = self.address_book[index]
            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(tk.END, name)
            self.phone_entry.delete(0, tk.END)
            self.phone_entry.insert(tk.END, phone_number)
            self.email_entry.delete(0, tk.END)
            self.email_entry.insert(tk.END, email)
            self.address_entry.delete(0, tk.END)
            self.address_entry.insert(tk.END, address)
        else:
            messagebox.showinfo("Info", "Invalid index.")

    def delete_contact(self):
        self.view_contacts()
        index = messagebox.askinteger("Delete Contact", "Enter index of contact to delete:") - 1
        if 0 <= index < len(self.address_book):
            del self.address_book[index]
            messagebox.showinfo("Success", "Contact deleted successfully!")
        else:
            messagebox.showinfo("Info", "Invalid index.")

def main():
    root = tk.Tk()
    app = ContactManagementApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
