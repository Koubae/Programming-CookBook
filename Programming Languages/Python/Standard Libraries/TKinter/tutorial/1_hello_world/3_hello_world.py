from tkinter import *


window = Tk()
window.geometry("400x400")
window.title("Hello World!")

text = Label(window, text="1) Using Pack")
text.pack()

# text2 = Label(window, text="2) Using Grid")
# text2.grid(row=0, column=2)

text3 = Label(window, text="3) Using Place")
text3.place(x=15, y=20)


try:
	# windows text blur
	from ctypes import windll
	windll.shcore.SetProcessDpiAwareness(1)
except ImportError:
	pass
finally:
	window.mainloop()
