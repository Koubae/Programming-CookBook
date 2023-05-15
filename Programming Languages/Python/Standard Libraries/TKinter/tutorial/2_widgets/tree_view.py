import tkinter as tk
from tkinter import ttk

root = tk.Tk()

b1 = ttk.Button(root, text='b1')
b1.grid(row=0, column=0, sticky="w")

e1 = ttk.Entry(root)
e1.grid(row=0, column=1, sticky="ew")

t = ttk.Treeview(root)
t.grid(row=1, column=0, columnspan=2, sticky="nsew") # columnspan=2 goes here.

scroll = ttk.Scrollbar(root)
scroll.grid(row=1, column=2, sticky="nse") # set this to column=2 so it sits in the correct spot.

scroll.configure(command=t.yview)
t.configure(yscrollcommand=scroll.set)

# root.columnconfigure(0, weight=1) Removing this line fixes the sizing issue with the entry field.
root.columnconfigure(1, weight=1)
root.rowconfigure(1, weight=1)

root.mainloop()