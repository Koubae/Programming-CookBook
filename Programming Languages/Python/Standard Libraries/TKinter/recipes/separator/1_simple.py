# https://www.pythontutorial.net/tkinter/tkinter-separator/

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('300x200')
root.resizable(False, False)
root.title('Separator Widget Demo')

ttk.Label(root, text="First Label").pack()

separator = ttk.Separator(root, orient='horizontal')
separator.pack(fill='x')
ttk.Label(root, text="Second Label").pack()

root.mainloop()