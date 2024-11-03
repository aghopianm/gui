from tkinter import *

import tkinter as tk
from tkinter import ttk

class RegistrationForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Register Personal Details")
        
        # Create main frame
        main_frame = ttk.Frame(root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Name section
        ttk.Label(main_frame, text="Name:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.name_entry = ttk.Entry(main_frame, width=40)
        self.name_entry.grid(row=0, column=1, sticky=tk.W, pady=5)
        
        # Profession section
        ttk.Label(main_frame, text="Profession:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.profession_combo = ttk.Combobox(main_frame, width=37)
        self.profession_combo['values'] = ('Software Engineer', 'Doctor', 'Teacher', 'Lawyer', 'Other')
        self.profession_combo.grid(row=1, column=1, sticky=tk.W, pady=5)
        
        # Position section
        ttk.Label(main_frame, text="Position:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.position_combo = ttk.Combobox(main_frame, width=37)
        self.position_combo['values'] = ('Junior', 'Senior', 'Manager', 'Director', 'Other')
        self.position_combo.grid(row=2, column=1, sticky=tk.W, pady=5)
        
        # Employment Status Frame (Radio Buttons)
        status_frame = ttk.LabelFrame(main_frame, text="Employment Status", padding="10")
        status_frame.grid(row=0, column=2, rowspan=3, padx=(20,0), sticky=(tk.N, tk.S, tk.E, tk.W))
        
        self.status_var = tk.StringVar()
        statuses = ['Currently Employed', 'Self Employed', 'Unemployed', 'Other']
        for i, status in enumerate(statuses):
            ttk.Radiobutton(status_frame, text=status, variable=self.status_var, 
                          value=status).grid(row=i, column=0, sticky=tk.W, pady=2)
        
        # Additional Info Frame (Checkboxes)
        info_frame = ttk.LabelFrame(main_frame, text="Additional Information", padding="10")
        info_frame.grid(row=3, column=2, padx=(20,0), sticky=(tk.N, tk.S, tk.E, tk.W))
        
        self.student_var = tk.BooleanVar()
        self.homeowner_var = tk.BooleanVar()
        self.transport_var = tk.BooleanVar()
        
        ttk.Checkbutton(info_frame, text="Student (Part/Full time)", 
                       variable=self.student_var).grid(row=0, column=0, sticky=tk.W, pady=2)
        ttk.Checkbutton(info_frame, text="Home Owner", 
                       variable=self.homeowner_var).grid(row=1, column=0, sticky=tk.W, pady=2)
        ttk.Checkbutton(info_frame, text="Transport Owner", 
                       variable=self.transport_var).grid(row=2, column=0, sticky=tk.W, pady=2)
        
        # Biography section
        ttk.Label(main_frame, text="Biography:").grid(row=3, column=0, sticky=tk.NW, pady=5)
        self.biography_text = tk.Text(main_frame, width=50, height=6)
        self.biography_text.grid(row=3, column=1, sticky=(tk.W, tk.E), pady=5)
        
        # Buttons frame
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=4, column=0, columnspan=3, pady=20)
        
        ttk.Button(button_frame, text="Clear", command=self.clear_form).grid(row=0, column=0, padx=5)
        ttk.Button(button_frame, text="Cancel", command=root.destroy).grid(row=0, column=1, padx=5)
        ttk.Button(button_frame, text="Submit", command=self.submit_form).grid(row=0, column=2, padx=5)

    def clear_form(self):
        self.name_entry.delete(0, tk.END)
        self.profession_combo.set('')
        self.position_combo.set('')
        self.status_var.set('')
        self.student_var.set(False)
        self.homeowner_var.set(False)
        self.transport_var.set(False)
        self.biography_text.delete('1.0', tk.END)

    def submit_form(self):
        # Here you would typically validate and process the form data
        print("Form submitted!")
        # Add your submission logic here

def main():
    root = tk.Tk()
    app = RegistrationForm(root)
    root.mainloop()

if __name__ == "__main__":
    main()