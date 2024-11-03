from tkinter import *
window = Tk()
window.title("This is my GUI project")
window.geometry("1000x1000")

text = Label(window, text="Hello World", fg='SteelBlue', bg='LightGray')
scaleDescriber = Label(window, text="Scale to show how cool you are")
button1 = Button(window, text='Press Me!')
chkButton1 = Checkbutton(window, text='One')
chkButton2 = Checkbutton(window, text='Two')
chkButton3 = Checkbutton(window, text='Three')
text_box = Text(window, wrap='word', height=5, width=20)  # Set height and width
scale = Scale(window, from_=0, to=100, orient=HORIZONTAL)
message_text = "This is a multi-line message displayed using the Message widget. It can wrap text automatically and display longer pieces of information without needing a separate text entry."
message = Message(window, text=message_text, width=300)  # Set width to control wrapping
listbox = Listbox(window, selectmode=SINGLE, height=4)  # Height of 4 to show 4 items
items = ["Item 1", "Item 2", "Item 3", "Item 4"]
for item in items:
    listbox.insert(END, item)  # Insert each item at the end of the Listbox

spinbox = Spinbox(window, from_=0, to=100, increment=1)

left = Frame(borderwidth=5)
left.pack(padx=10, pady=10, side='right')

radio_value = StringVar(left, value="Option1")  # Default value for RadioButtons
radio1 = Radiobutton(left, text="Option 1", variable=radio_value, value="Option1")
radio2 = Radiobutton(left, text="Option 2", variable=radio_value, value="Option2")
radio3 = Radiobutton(left, text="Option 3", variable=radio_value, value="Option3")

radio1.pack(anchor=W)
radio2.pack(anchor=W)
radio3.pack(anchor=W)

chkButton1.place(height=50, width=100, x=400, y=600)
chkButton2.place(height=50, width=100, x=400, y=650)
chkButton3.place(height=50, width=100, x=400, y=700)
listbox.pack(padx=10, pady=10)
message.pack(padx=10, pady=10)  # Add padding for better layout
scaleDescriber.pack()
scale.pack(padx=10, pady=20)  # Add padding for better layout
button1.pack()
text.pack()
text_box.pack(padx=10, pady=10)
spinbox.pack()

window.mainloop()