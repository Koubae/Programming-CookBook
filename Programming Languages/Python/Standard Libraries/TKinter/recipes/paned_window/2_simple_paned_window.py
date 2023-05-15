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

paned_window_vertical = ttk.PanedWindow(root, orient=tk.VERTICAL)
paned_window_vertical.pack(fill=tk.BOTH, expand=True)


# paned window
paned_window_horizontal_top = ttk.PanedWindow(root, orient=tk.HORIZONTAL)
# place the panedwindow on the root window
paned_window_horizontal_top.pack(fill=tk.BOTH, expand=True)
# Left listbox
left_list = tk.Listbox(root, height=6,
					   listvariable=tk.Variable(value=('Java', 'C#', 'C', 'C++', 'Python', 'Go', 'JavaScript', 'PHP', 'Swift')),
					   selectmode=tk.EXTENDED)
left_list.pack( side=tk.LEFT)
# link a scrollbar to a list
# SCROLL BAR NOT WORKING ...
# scrollbar = ttk.Scrollbar(root,orient=tk.VERTICAL,command=left_list.yview)
# left_list['yscrollcommand'] = scrollbar.set
#
# scrollbar.pack(side=tk.RIGHT, expand=True, fill=tk.Y)

paned_window_horizontal_top.add(left_list)



# Right listbox
right_list = tk.Listbox(root,  height=6,
					   listvariable=tk.Variable(value=tuple([i for i in range(100)])),
					   selectmode=tk.EXTENDED)
right_list.pack(side=tk.LEFT)
paned_window_horizontal_top.add(right_list)




paned_window_horizontal_bottom = ttk.PanedWindow(root, orient=tk.HORIZONTAL)
# place the panedwindow on the root window
paned_window_horizontal_bottom.pack(fill=tk.BOTH, expand=True)


left_bottom_list = tk.Listbox(root, height=6,
					   listvariable=tk.Variable(value=('Java', 'C#', 'C', 'C++', 'Python', 'Go', 'JavaScript', 'PHP', 'Swift')),
					   selectmode=tk.EXTENDED)
left_bottom_list.pack( side=tk.LEFT)
paned_window_horizontal_bottom.add(left_bottom_list)


right_bottom_list = tk.Listbox(root,  height=6,
					   listvariable=tk.Variable(value=tuple([i for i in range(100)])),
					   selectmode=tk.EXTENDED)
right_bottom_list.pack(side=tk.LEFT)
paned_window_horizontal_bottom.add(right_bottom_list)

paned_window_vertical.add(paned_window_horizontal_top)
paned_window_vertical.add(paned_window_horizontal_bottom)


root.mainloop()
