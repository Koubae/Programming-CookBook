# https://www.pythontutorial.net/tkinter/tkinter-cursors/
from tkinter import ttk
import tkinter as tk

root = tk.Tk()
root.geometry("800x600")
root.resizable(False, False)
root.title("Cursor Selector")

window = ttk.Frame(root)

ttk.Label(window, text="Cursor:").pack(fill=tk.X, padx=5, pady=5)

cursor_current = tk.StringVar()
cursors_entity = ttk.Combobox(window, textvariable=cursor_current, cursor='arrow')
cursors = [
	'arrow',
	'man',
	'based_arrow_down',
	'middlebutton',
	'based_arrow_up',
	'mouse',
	'boat',
	'pencil',
	'bogosity',
	'pirate',
	'bottom_left_corner',
	'plus',
	'bottom_right_corner',
	'question_arrow',
	'bottom_side',
	'right_ptr',
	'bottom_tee',
	'right_side',
	'box_spiral',
	'right_tee',
	'center_ptr',
	'rightbutton',
	'circle',
	'rtl_logo',
	'clock',
	'sailboat',
	'coffee_mug',
	'sb_down_arrow',
	'cross',
	'sb_h_double_arrow',
	'cross_reverse',
	'sb_left_arrow',
	'crosshair',
	'sb_right_arrow',
	'diamond_cross',
	'sb_up_arrow',
	'dot',
	'sb_v_double_arrow',
	'dotbox',
	'shuttle',
	'double_arrow',
	'sizing',
	'draft_large',
	'spider',
	'draft_small',
	'spraycan',
	'draped_box',
	'star',
	'exchange',
	'target',
	'fleur',
	'tcross',
	'gobbler',
	'top_left_arrow',
	'gumby',
	'top_left_corner',
	'hand1',
	'top_right_corner',
	'hand2',
	'top_side',
	'heart',
	'top_tee',
	'icon',
	'trek',
	'iron_cross',
	'ul_angle',
	'left_ptr',
	'umbrella',
	'left_side',
	'ur_angle',
	'left_tee',
	'watch',
	'leftbutton',
	'xterm',
	'll_angle',
	'X_cursor',
	'lr_angle',
]
cursors_entity['values'] = cursors
cursors_entity['state'] = 'readonly'
cursors_entity.pack(fill=tk.X, padx=5, pady=5)


def on_cursor_change(_):
	window.config(cursor=cursor_current.get())


cursors_entity.bind('<<ComboboxSelected>>', on_cursor_change)

window.pack(expand=True, fill=tk.BOTH)


if __name__ == '__main__':
	root.mainloop()
