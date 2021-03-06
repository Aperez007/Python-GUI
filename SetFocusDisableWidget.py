import tkinter as tk
from tkinter import ttk
win = tk.Tk()
win.title("Python GUI")

#win.resizable(0,0)    

# Modify adding a Label
aLabel = ttk.Label(win, text="A Label")
aLabel.grid(column=0, row=0)

#Modified Button Click Function
def clickMe():
    action.configure(text='Hello ' + name.get())

# Changing our Label
ttk.Label(win, text="Enter a name:").grid(column=0, row=0)

# Adding a Textbox Entry widget
name = tk.StringVar()
nameEntered = ttk.Entry(win, width=12, textvariable=name)
nameEntered.grid(column=0, row=1)

# Adding a Button
action = ttk.Button(win, text="Click Me!", command=clickMe)   
action.grid(column=1, row=1)
action.configure(state='disabled')    # Disable the Button Widget
nameEntered.focus()      # Place cursor into name Entry

win.mainloop()