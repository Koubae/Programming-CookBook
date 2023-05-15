# https://www.pythontutorial.net/tkinter/ttk-style-map/
import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry('300x100')

        button = ttk.Button(self, text='Save')
        button.pack(expand=True)

        style = ttk.Style(self)
        style.configure('TButton', font=('Helvetica', 16))
        style.map('TButton',
                foreground=[('pressed', 'blue'),
                            ('active', 'red')])

        print(style.layout('TButton'))


if __name__ == "__main__":
    app = App()
    app.mainloop()