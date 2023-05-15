# https://www.pythontutorial.net/tkinter/tkinter-cursors/
import tkinter as tk

root = tk.Tk()
root.geometry("300x300")


def change_cursor(event):
    if event.x in range(100, 300):
        root.config(cursor="watch")
    else:
        root.config(cursor="")


root.bind("<Motion>", change_cursor)
root.mainloop()