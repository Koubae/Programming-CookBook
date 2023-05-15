# https://www.pythontutorial.net/tkinter/tkinter-menubutton/

import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
	def __init__(self):
		super().__init__()

		self.geometry('800x600')
		self.title('Menubutton Demo')

		# Menubutton variable
		self.selected_color = tk.StringVar()
		self.selected_color.trace("w", self.menu_item_selected)

		self.bool_my = tk.BooleanVar()
		self.bool_my.trace("w", self.on_bool_selected)

		# create the menu button
		self.create_menu_button()


	def menu_item_selected(self, *args):
		""" handle menu selected event """
		self.config(bg=self.selected_color.get())

	def on_bool_selected(self, *_):
		value = self.bool_my.get()
		if value:
			self.config(bg="yellow")
		else:
			self.config(bg="black")

	def create_menu_button(self):
		""" create a menu button """
		# menu variable
		colors = ('Red', 'Green', 'Blue')

		# create the Menubutton
		menu_button = ttk.Menubutton(
			self,
			text='Select a color')

		# create a new menu instance
		menu = tk.Menu(menu_button, tearoff=0)

		for color in colors:
			menu.add_radiobutton(
				label=color,
				value=color,
				variable=self.selected_color)

		menu.add_radiobutton(
			label="True",
			value=True,
			variable=self.bool_my)
		menu.add_radiobutton(
			label="False",
			value=False,
			variable=self.bool_my)

		# associate menu with the Menubutton
		menu_button["menu"] = menu

		menu_button.pack(expand=True)


if __name__ == "__main__":
	app = App()
	app.mainloop()
