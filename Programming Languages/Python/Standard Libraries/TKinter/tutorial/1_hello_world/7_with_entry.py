import tkinter as tk
import time

class App(tk.Frame):
	def __init__(self, master):
		super().__init__(master)
		self.pack()

		self.entrythingy = tk.Entry()
		self.entrythingy.pack()

		# Create the application variable.
		self.contents = tk.StringVar()
		# Set it to some value.
		self.contents.set("this is a variable")
		# Tell the entry widget to watch this variable.
		self.entrythingy["textvariable"] = self.contents

		# Define a callback for when the user hits return.
		# It prints the current value of the variable.
		self.entrythingy.bind('<Key-Return>',
							  self.print_contents)

		self.button = tk.Button(text="Press Me")
		self.button.pack()

		# self.button.bind("<Enter>", self.turn_red)
		self.button.bind("<Enter>", lambda event: event.widget.config(activeforeground="red", activebackground="blue"))
	def print_contents(self, event):
		print(f"{event} \n: Hi. The current entry content is:",
			  self.contents.get())
		self.contents.set("")

		fore = self.button["foreground"]
		back = self.button["background"]
		print(fore)
		print(back)

		self.button.config(foreground="green", background="yellow")

		def callback():
			self.button.config(foreground=fore, background=back)
		self.button.after(150, callback)



	def turn_red(self, event):
		event.widget["activeforeground"] = "red"
		event.widget["activebackground"] = "blue"


root = tk.Tk()
myapp = App(root)
myapp.mainloop()
