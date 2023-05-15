USE_TTK = True
if USE_TTK:
	from tkinter import *
	from tkinter import ttk

	root = Tk()
	root.title("Hello world 6")
	root.geometry("860x600")

	frame = ttk.Frame(root, padding=10)
	frame.grid()

	ttk.Label(frame, text="Hello world").grid(column=0, row=0)
	ttk.Button(frame, text="Quit", command=root.destroy).grid(column=1, row=0)
else:
	from tkinter import *
	root = Tk()
	root.title("Hello world 6")
	root.geometry("860x600")

	frame = Frame(root)
	frame.grid()

	Label(frame, text="Hello world").grid(column=0, row=0)
	Button(frame, text="Quit", command=root.destroy).grid(column=1, row=0)

try:
	# windows text blur
	from ctypes import windll
	windll.shcore.SetProcessDpiAwareness(1)
except ImportError:
	pass
finally:
	root.mainloop()
