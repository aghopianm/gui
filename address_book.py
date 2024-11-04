import tkinter as tk
from tkinter import ttk
import json
import os
import matplotlib.pyplot as plt
from collections import Counter

# File path for storing contacts
contacts_file = "contacts.json"

def load_contacts():
    """Load contacts from a JSON file."""
    if os.path.exists(contacts_file):
        with open(contacts_file, "r") as file:
            return json.load(file)
    return []  # Return an empty list if the file does not exist

def save_contacts():
    """Save contacts to a JSON file."""
    with open(contacts_file, "w") as file:
        json.dump(contacts, file)

def show_contact_details(event):
    """Display the details of the selected contact."""
    selected_index = contact_listbox.curselection()
    if selected_index:
        index = selected_index[0]
        contact = contacts[index]
        name_label_value.config(text=contact["name"])
        phone_label_value.config(text=contact["phone"])
        email_label_value.config(text=contact["email"])
        city_label_value.config(text=contact["city"])

def add_contact():
    """Add a new contact to the address book."""
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    city = city_entry.get()  # Get the city information

    if name and phone and email and city:  # Ensure all fields are filled
        new_contact = {"name": name, "phone": phone, "email": email, "city": city}
        contacts.append(new_contact)  # Add to the contact list
        contact_listbox.insert(tk.END, name)  # Add the name to the listbox

        # Clear the entry fields
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        city_entry.delete(0, tk.END)

        save_contacts()  # Save contacts after adding a new one

def generate_statistics():
    """Generate and display statistics about the contacts."""
    # Count the number of contacts per city
    cities = [contact.get("city", "Unknown") for contact in contacts]
    city_counts = Counter(cities)

    # Create a bar chart
    plt.figure(figsize=(10, 5))
    plt.bar(city_counts.keys(), city_counts.values(), color='skyblue')
    plt.title("Number of Contacts by City")
    plt.xlabel("City")
    plt.ylabel("Number of Contacts")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Create the main window
window = tk.Tk()
window.title("Digital Address Book")
window.configure(background='#f5f5f5')

# Load existing contacts when the program starts
contacts = load_contacts()

# Contact List Section
contact_listbox = tk.Listbox(window, width=30, height=10, font=('Helvetica', 10))
contact_listbox.grid(row=0, column=0, padx=20, pady=20, rowspan=4)
for contact in contacts:
    contact_listbox.insert(tk.END, contact["name"])

# Bind the listbox to display contact details
contact_listbox.bind("<<ListboxSelect>>", show_contact_details)

# Contact Details Section
details_frame = tk.Frame(window, bg='#f5f5f5')
details_frame.grid(row=0, column=1, padx=20, pady=20, sticky='N')

tk.Label(details_frame, text="Contact Details", bg='#f5f5f5', fg='#333333', font=('Helvetica', 12, 'bold')).pack(anchor='w')

tk.Label(details_frame, text="Name:", bg='#f5f5f5', fg='#333333', font=('Helvetica', 10)).pack(anchor='w')
name_label_value = tk.Label(details_frame, text="", bg='#f5f5f5', fg='#555555', font=('Helvetica', 10))
name_label_value.pack(anchor='w')

tk.Label(details_frame, text="Phone:", bg='#f5f5f5', fg='#333333', font=('Helvetica', 10)).pack(anchor='w')
phone_label_value = tk.Label(details_frame, text="", bg='#f5f5f5', fg='#555555', font=('Helvetica', 10))
phone_label_value.pack(anchor='w')

tk.Label(details_frame, text="Email:", bg='#f5f5f5', fg='#333333', font=('Helvetica', 10)).pack(anchor='w')
email_label_value = tk.Label(details_frame, text="", bg='#f5f5f5', fg='#555555', font=('Helvetica', 10))
email_label_value.pack(anchor='w')

tk.Label(details_frame, text="City:", bg='#f5f5f5', fg='#333333', font=('Helvetica', 10)).pack(anchor='w')
city_label_value = tk.Label(details_frame, text="", bg='#f5f5f5', fg='#555555', font=('Helvetica', 10))
city_label_value.pack(anchor='w')

# Add Contact Form
form_frame = tk.Frame(window, bg='#f5f5f5')
form_frame.grid(row=4, column=0, columnspan=2, pady=20)

tk.Label(form_frame, text="Add New Contact", bg='#f5f5f5', fg='#333333', font=('Helvetica', 12, 'bold')).grid(row=0, column=0, columnspan=2, pady=10)

tk.Label(form_frame, text="Name:", bg='#f5f5f5', fg='#333333', font=('Helvetica', 10)).grid(row=1, column=0, sticky='E')
name_entry = tk.Entry(form_frame, width=30)
name_entry.grid(row=1, column=1, pady=5)

tk.Label(form_frame, text="Phone:", bg='#f5f5f5', fg='#333333', font=('Helvetica', 10)).grid(row=2, column=0, sticky='E')
phone_entry = tk.Entry(form_frame, width=30)
phone_entry.grid(row=2, column=1, pady=5)

tk.Label(form_frame, text="Email:", bg='#f5f5f5', fg='#333333', font=('Helvetica', 10)).grid(row=3, column=0, sticky='E')
email_entry = tk.Entry(form_frame, width=30)
email_entry.grid(row=3, column=1, pady=5)

tk.Label(form_frame, text="City:", bg='#f5f5f5', fg='#333333', font=('Helvetica', 10)).grid(row=4, column=0, sticky='E')
city_entry = tk.Entry(form_frame, width=30)
city_entry.grid(row=4, column=1, pady=5)

# Add Contact Button
add_button = ttk.Button(form_frame, text="Add Contact", command=add_contact)
add_button.grid(row=5, column=1, pady=10, sticky='E')

# Generate Statistics Button
stats_button = ttk.Button(window, text="Generate Statistics", command=generate_statistics)
stats_button.grid(row=5, column=0, columnspan=2, pady=10)

# Save contacts when the application closes
def on_closing():
    save_contacts()
    window.destroy()

window.protocol("WM_DELETE_WINDOW", on_closing)  # Handle window closing

window.mainloop()
