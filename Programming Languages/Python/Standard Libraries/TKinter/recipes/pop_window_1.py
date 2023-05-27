import tkinter as tk


try:
	# windows text blur
	from ctypes import windll  # noqa

	windll.shcore.SetProcessDpiAwareness(1)
except ImportError:
	pass

from tkinter import simpledialog
# the input dialog
while True:
	newWin = tk.Tk()

	newWin.withdraw()
	try:
		answer = simpledialog.askstring(title="Test",
										prompt="What's your Name?:", parent=newWin)
	except Exception as error:
		print(error)
		raise error
	else:
		print(answer)
		newWin.destroy()