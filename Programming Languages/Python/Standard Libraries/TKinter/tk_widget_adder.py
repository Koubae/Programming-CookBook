from tk_imports import *


class Window:

    def __init__(self, root, config):
        self.root = root
        self.title = config.get('title') and config.pop('title') or "Title Not Set"
        self.geometry = config.get('geometry') and config.pop('geometry')
        self.fullscreen = config.pop('fullscreen') if 'fullscreen' in config else None
        self.config = config
        self.surface = self._init_window()

    def _init_window(self):
        window = tk.Frame(master=self.root, cnf=self.config)
        if self.fullscreen:
            self.root.attributes(self.fullscreen, True)
        elif self.geometry:
            self.root.geometry(self.geometry)
        window.pack(fill=tk.BOTH, expand=True)
        # window.pack()
        return window

    def run(self):
        self.root.mainloop()

    def create_frame(self, _frame, master):
        frame = tk.Frame(master=master, cnf=_frame)
        frame.pack(fill=tk.BOTH, expand=True)
        return frame

    def append_btn(self, btn):
        # btn = tk.Button(btn.get('parent'), text=btn.get('text'), command=btn.get('action'))
        btn = tk.Button(btn.pop('parent'), command=btn.pop('action'), cnf=btn)
        btn.pack()
        return btn

    def append_label(self, label):
        side = label.pop('side')
        fill = label.pop('fill')
        font = label.pop('font')
        _label = tk.Label(label.pop('parent'), cnf=label)
        _label.pack(side=side, fill=fill)
        _label.config(font=font)
        return _label

def main(title):
    config = {
        "title": title,
        "name": "window",
        "bg": "black",
        # "width": 1200,
        # "height": 940,
        "geometry": '350x450+700+200',
        # "geometry": '1200x940',
        # 'fullscreen': '-fullscreen'
        'fullscreen': False
    }

    # ws.geometry('350x450+700+200')
    # a = tk.Canvas.create_window()
    window = Window(tk.Tk(), config)
    # quit = Button(root, text="QUIT", command=root.destroy)
    font = {"family": "Helvetica", "size": 1, "weight": "bold", "slant": "roman", "underline": 1, "overstrike": 1}
    main_header_cnf = {
        'parent': window.surface,
        'side': tk.TOP,
        'fill': tk.BOTH,
        'font': (
            "Courier",
            22,
            "bold",
            "italic",
        ),
        # 'font': font,
        'text': 'My First Python Desktop App'.upper(),
        'bg': "#f2f2ed",
        'fg': '#6ee0db',
        # "width": 1200,
        "height": 2,
    }
    main_header = window.append_label(main_header_cnf)


    main_surface_cnf = {
        "name": "main_surface", # TODO: Study --> newPathname
        "bg": "#ffffff",
        "width": 1200,
        "height": 940,
    }
    main_surface = window.create_frame(main_surface_cnf, window.surface)
    quit_button_cnf = {
        "name": "quit_button",
        "text": "Quit",
        "parent": main_surface,
        "action": window.root.destroy
    }
    quit_button = window.append_btn(quit_button_cnf)


    return window



if __name__ == '__main__':
    title = "My First Tkinter App"
    window = main(title)
    window.run()