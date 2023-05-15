# https://www.pythontutorial.net/tkinter/tkinter-treeview/
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# create root window
root = tk.Tk()
root.title('Treeview Demo - Hierarchical Data')
root.geometry('400x200')

# configure the grid layout
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)


# create a treeview
tree = ttk.Treeview(root)
tree.heading('#0', text='Departments', anchor=tk.W)


# adding data
tree.insert('', tk.END, text='Administration', iid=0, open=False)
tree.insert('', tk.END, text='Logistics', iid=1, open=False)
tree.insert('', tk.END, text='Sales', iid=2, open=False)
tree.insert('', tk.END, text='Finance', iid=3, open=False)
tree.insert('', tk.END, text='IT', iid=4, open=False)

# adding children of first node
tree.insert('', tk.END, text='John Doe', iid=5, open=False)
tree.insert('', tk.END, text='Jane Doe', iid=6, open=False)
tree.move(5, 0, 0)
tree.move(6, 0, 1)

tree.insert('', tk.END, text='John Doe 2', iid=7, open=False)
tree.insert('', tk.END, text='Jane Doe 2', iid=8, open=False)
tree.move(7, 1, 0)
tree.move(8, 1, 1)

# place the Treeview widget on the root window
tree.grid(row=0, column=0, sticky=tk.NSEW)

# run the app
root.mainloop()