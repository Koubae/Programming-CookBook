# https://www.pythontutorial.net/tkinter/tkinter-button/
import os
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# root window
root = tk.Tk()
root.geometry('1400x600')
root.resizable(False, False)
root.title('Image Button Demo')


# download button
def download_clicked():
	showinfo(
		title='Information',
		message='Download button clicked!'
	)


image_path = os.path.join("../assets", "download.png")
download_icon = tk.PhotoImage(file=image_path)
download_button = ttk.Button(
	root,
	text="Download",
	compound=tk.LEFT,
	image=download_icon,
	command=download_clicked
)

download_button.pack(
	ipadx=5,
	ipady=5,
	expand=True
)

root.mainloop()
