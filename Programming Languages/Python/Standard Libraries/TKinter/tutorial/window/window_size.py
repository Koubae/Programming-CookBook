import tkinter as tk


root = tk.Tk()
root.title('Tkinter Window - Center')


# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# define window dimension
window_width = screen_width
window_height = screen_height

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)


# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# or to set full window use
# root.state('zoomed')  # maximize the window
root.resizable(False, False)
# root.attributes('-alpha',0.5)
root.attributes('-topmost', 1)

# transparent
# root.attributes("-alpha", 00)

# default icon
root.iconbitmap('./python.ico')

root.mainloop()
