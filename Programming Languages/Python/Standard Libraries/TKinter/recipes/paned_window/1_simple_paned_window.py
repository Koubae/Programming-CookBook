# https://www.pythontutorial.net/tkinter/tkinter-panedwindow/
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('PanedWindow Demo')
root.geometry('800x600')

# change style to classic (Windows only)
# to show the sash and handle
style = ttk.Style()
style.theme_use('classic')

# paned window
paned_window_horizontal = ttk.PanedWindow(orient=tk.HORIZONTAL)

# Left listbox
left_list = tk.Listbox(root)
left_list.pack(side=tk.LEFT)
paned_window_horizontal.add(left_list)

# Right listbox
right_list = tk.Listbox(root)
right_list.pack(side=tk.LEFT)
paned_window_horizontal.add(right_list)

# place the panedwindow on the root window
paned_window_horizontal.pack(fill=tk.BOTH, expand=True)

root.mainloop()