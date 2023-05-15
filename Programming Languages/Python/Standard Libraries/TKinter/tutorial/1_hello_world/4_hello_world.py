import tkinter as tk

class App(tk.Frame):
	def __init__(self, master = None):
		super().__init__(master)
		self.pack()
		self.create_widgets()

	def create_widgets(self):
		self.button = tk.Button(self)
		self.button["text"] = "Hello world\n(click me!)"
		self.button["command"] = self.say_hi
		self.button.pack(side="top")

		self.quit = tk.Button(self, text="Quit", fg="red", command=self.master.destroy)
		self.quit.pack(side="bottom")

	def say_hi(self):
		print("Hello world")

app = App(master=tk.Tk())
app.mainloop()
