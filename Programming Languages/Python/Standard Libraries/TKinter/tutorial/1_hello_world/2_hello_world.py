import tkinter as tk


root = tk.Tk()

message = tk.Label(root, text="Hello world!")
message.pack()

try:
	# windows text blur
	from ctypes import windll
	windll.shcore.SetProcessDpiAwareness(1)
except ImportError:
	pass
finally:
	root.mainloop()
