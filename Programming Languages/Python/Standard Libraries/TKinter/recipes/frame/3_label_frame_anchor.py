# https://www.pythontutorial.net/tkinter/tkinter-labelframe/
import tkinter as tk
from tkinter import ttk

# root window
root = tk.Tk()
root.title('LabelFrame Label Anchor')

# label frame
label_frame = ttk.LabelFrame(root, text='Label Anchor')
label_frame.grid(column=0, row=0, padx=20, pady=20, sticky=tk.NSEW)

anchor_var = tk.StringVar()
anchors = {
    'nw': {'row': 0, 'column': 1},
    'n': {'row': 0, 'column': 2},
    'ne': {'row': 0, 'column': 3},
    'en': {'row': 1, 'column': 4},
    'e': {'row': 2, 'column': 4},
    'es': {'row': 3, 'column': 4},
    'se': {'row': 4, 'column': 3},
    's': {'row': 4, 'column': 2},
    'sw': {'row': 4, 'column': 1},
    'ws': {'row': 3, 'column': 0},
    'w': {'row': 2, 'column': 0},
    'wn': {'row': 1, 'column': 0}
}


def change_label_anchor():
    label_frame['labelanchor'] = anchor_var.get()


# create radio buttons and place them on the label frame
for key, value in anchors.items():
    # create a radio button
    radio = ttk.Radiobutton(
        label_frame,
        text=key.upper(),
        value=key,
        command=change_label_anchor,
        variable=anchor_var
    ).grid(**value, padx=10, pady=10, sticky=tk.NSEW)

# set the radio button selected
anchor_var.set(label_frame['labelanchor'])

# show the root window
root.mainloop()