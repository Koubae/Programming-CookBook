import tkinter as tk
from tkinter import ttk

root = tk.Tk()

password = tk.StringVar()
password_entry = ttk.Entry(root, textvariable=password, show="*")
password_entry.pack()

root.mainloop()