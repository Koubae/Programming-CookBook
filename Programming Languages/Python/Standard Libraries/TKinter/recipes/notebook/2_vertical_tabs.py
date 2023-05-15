import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.geometry('800x600')
root.title('Notebook Vertical Tabs')

style = ttk.Style(root)
# style.configure("lefttab.TNotebook", tabposition='ws') # BOTTOM LEFT
# style.configure("lefttab.TNotebook", tabposition='w')  # BOTTOM
style.configure("lefttab.TNotebook", tabposition='wn', background="pink", focuscolor="green", bordercolor="yellow")  # BOTTOM

notebook = ttk.Notebook(root, style='lefttab.TNotebook')

f1 = tk.Frame(notebook, bg='red', width=800, height=600)
f2 = tk.Frame(notebook, bg='blue', width=800, height=600)
notebook.add(f1, text='Frame 1')
notebook.add(f2, text='Frame 2')
notebook.pack()

print(style.layout('lefttab.TNotebook'))

if __name__ == '__main__':
	root.mainloop()