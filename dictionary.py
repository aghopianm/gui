import tkinter as tk
from tkinter import ttk
import json
import os

def load_definitions():
    """Load user definitions from a file and merge with default definitions."""
    user_defs = {}
    if os.path.exists("definitions.json"):
        with open("definitions.json", "r") as file:
            user_defs = json.load(file)
    
    # Merge default definitions with user definitions (user definitions override defaults if needed)
    all_defs = {**default_defs, **user_defs}
    return all_defs

def save_definitions():
    """Save user definitions (excluding the default ones) to a file."""
    # Only save definitions that are not in the default dictionary
    user_defs = {term: definition for term, definition in computer_defs.items() if term not in default_defs}
    with open("definitions.json", "w") as file:
        json.dump(user_defs, file)
    output.delete(0.0, tk.END)
    output.insert(tk.END, "Definitions saved successfully.")

def get_def():
    term = term_entry.get().lower()  # Convert input term to lowercase
    # Clears the text box from previous entries
    output.delete(0.0, tk.END)
    if term in computer_defs:
        definition = computer_defs[term]
    else:
        definition = "Sorry, that term is not in the dictionary."

    output.insert(tk.END, definition)

def add_def():
    new_term = new_term_entry.get().lower()  # Convert new term to lowercase
    new_definition = new_definition_entry.get()
    
    if new_term and new_definition:  # Check that both fields are filled
        computer_defs[new_term] = new_definition  # Add to the dictionary
        new_term_entry.delete(0, tk.END)  # Clear the entry fields
        new_definition_entry.delete(0, tk.END)
        output.delete(0.0, tk.END)
        output.insert(tk.END, f"Added definition for '{new_term}'.")

window = tk.Tk()
window.title("Best dictionary in the world")
window.configure(background='#f5f5f5')  # Soft light grey background

# Text to output to the user
instruction = tk.StringVar()
instruction.set('Enter a term you would like to know the definition of:')

# Adding a logo (if you have one)
logo = tk.PhotoImage(file="trump.png")
tk.Label(window, image=logo, bg='#f5f5f5').grid(row=0, column=0, sticky='EW', columnspan=3)

# Adding instruction for user
tk.Label(window, text=instruction.get(), 
         bg='#f5f5f5', fg='#333333', font=('Helvetica', 12, 'bold')).grid(row=1, column=0, columnspan=3, pady=10)

# Create a text entry box for term search, centered using columnspan
term_entry = tk.Entry(window, bg='white', width=40, font=('Helvetica', 10))
term_entry.grid(row=2, column=0, columnspan=3, pady=10)  # Centered entry box with more width and padding

# Add a button to get definition
ttk.Button(window, text='GET', width=10, command=get_def).grid(row=3, column=1, pady=5)

# Label for output
tk.Label(window, text='Definition:', bg='#f5f5f5', fg='#333333', font=('Helvetica', 12, 'bold')).grid(row=4, column=0, columnspan=3, pady=(20, 5), sticky='W')

# Output for the definition (large text box)
output = tk.Text(window, width=75, height=6, wrap='word', background='white', font=('Helvetica', 10))
output.grid(row=5, column=0, columnspan=3, padx=20, pady=10)

# Separator for adding new terms
tk.Label(window, text='Add your own term and definition:', bg='#f5f5f5', fg='#333333', font=('Helvetica', 12, 'bold')).grid(row=6, column=0, columnspan=3, pady=10, sticky='W')

# Entry for new term
tk.Label(window, text='Term:', bg='#f5f5f5', fg='#333333', font=('Helvetica', 10)).grid(row=7, column=0, sticky='E', padx=10)
new_term_entry = tk.Entry(window, bg='white', width=30, font=('Helvetica', 10))
new_term_entry.grid(row=7, column=1, columnspan=2, pady=5, sticky='W')

# Entry for new definition
tk.Label(window, text='Definition:', bg='#f5f5f5', fg='#333333', font=('Helvetica', 10)).grid(row=8, column=0, sticky='E', padx=10)
new_definition_entry = tk.Entry(window, bg='white', width=50, font=('Helvetica', 10))
new_definition_entry.grid(row=8, column=1, columnspan=2, pady=5, sticky='W')

# Button to add new definition
ttk.Button(window, text='SUBMIT', width=10, command=add_def).grid(row=9, column=1, pady=10, sticky='E')

# Button to save definitions
ttk.Button(window, text='SAVE', width=10, command=save_definitions).grid(row=10, column=1, pady=10, sticky='E')

# Default definitions that are always available
default_defs = {
    'http': 'HTTP (Hypertext Transfer Protocol) is the set of rules for transferring files -- such as text, images, sound, video and other multimedia files -- over the web.', 
    'kernel': "A core component of an operating system and serves as the main interface between the computer's physical hardware and the processes running on it."
}

# Load existing definitions when the program starts
computer_defs = load_definitions()

window.mainloop()
