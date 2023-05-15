import tkinter as tk


class App(tk.Frame):
	def __init__(self, master = None):
		super().__init__(master)
		self.pack()


app = App()
app.master.title("Hello World App")
app.master.maxsize(1000, 400)
app.mainloop()
