from tkinter import *
from tkinter import ttk  # new widget ui
try:
	# windows text blur
	from ctypes import windll
	windll.shcore.SetProcessDpiAwareness(1)
except ImportError:
	pass

window = Tk()


def set_up_window():
	screen_width = window.winfo_screenwidth()
	screen_height = window.winfo_screenheight()

	screen_x_half = int(screen_width / 2)
	screen_y_half = int(screen_height / 2)

	center_x = int(screen_x_half - screen_x_half)
	center_y = int(screen_y_half - screen_y_half)

	window.geometry(f'{screen_width}x{screen_width}+{center_x}+{center_y}')
	window.resizable(False, False)
	window.attributes('-topmost', 1)
	window.title("Widgets")


set_up_window()

# Frame This is much cleaner but cannot be used with pack!
# frm = ttk.Frame(window, padding=10)
# frm.grid()

# Text
Label(window, text="1) Text (old style)", font=("Helvetica", 16), fg="yellow", bg="green", width=30).pack(side=TOP, anchor=NW)
ttk.Label(window, text="1) Text (new style)", font=("Helvetica", 16), foreground="yellow", background="green", width=30).pack(side=TOP, anchor=NW)

# Picture
# NOTE: Must keep the image reference in memory, otherwise it won't be shown!
image = PhotoImage(file="python.png").subsample(10, 10)  # 10 times smaller
Label(window, image=image).pack(side=TOP, anchor=NW)

# Button
Button(window, text="Press me", command=lambda : print("Clicked!")).pack()
ttk.Button(window, text="Press me", command=lambda : print("Clicked!")).pack()


# Entry (single line input box)
input_box = Entry(window, width=20, font=("calibri", 18))
input_box.pack()
input_box.bind("<Key-Return>", lambda event: print("Enter pressed!"))

input_box_new = ttk.Entry(window, width=20, font=("calibry", 18))
input_box_new.pack()
input_box_new.bind("<Key-Return>", lambda event: print("New widget pressed!"))

# Frame separator
Frame(window, height=2, bd=1, relief=SUNKEN).pack(fill=X, padx=5, pady=5)
ttk.Frame(window, height=2, borderwidth=1, relief=SUNKEN).pack(fill=X, padx=5, pady=5)

## ttk separator
ttk.Separator(window, orient="horizontal").pack(fill=X)
ttk.Separator(window, orient="vertical").pack(fill=Y)

# List box
listbox_1 = Listbox(window)
listbox_1.pack()

listbox_1.insert(END, "1) First Entry")
for item in ["one", "two", "thre", "four"]:
	listbox_1.insert(END, "Item " + item)

# Check button
Checkbutton(window, text="Male").pack()
Checkbutton(window, text="Female").pack()

ttk.Checkbutton(window, text="Male").pack()
ttk.Checkbutton(window, text="Female").pack()

# Radio button
v = IntVar()
Radiobutton(window, text="One", variable=v, value=1).pack()
Radiobutton(window, text="Two", variable=v, value=2).pack()

ttk.Radiobutton(window, text="One -", variable=v, value=3).pack()
ttk.Radiobutton(window, text="Two - ", variable=v, value=4).pack()

# Canvas
ca = Canvas(window, width=200, height=100)
ca.pack()

ca.create_line(0, 0, 200, 100)
ca.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))

ca.create_rectangle(50, 25, 150, 75, fill="blue")

window.mainloop()
