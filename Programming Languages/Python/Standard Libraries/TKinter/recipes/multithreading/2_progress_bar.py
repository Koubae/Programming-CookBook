# https://www.pythontutorial.net/tkinter/tkinter-thread-progressbar/

import requests
import tkinter as tk
from threading import Thread
from PIL import Image, ImageTk
from tkinter import ttk
# from proxies import proxyDict


class PictureDownload(Thread):
    def __init__(self, url):
        super().__init__()

        self.picture_file = None
        self.url = url

    def run(self):
        """ download a picture and save it to a file """
        # download the picture
        # response = requests.get(self.url, proxies=proxyDict)
        response = requests.get(self.url)
        picture_name = self.url.split('/')[-1]
        picture_file = f'./assets/{picture_name}.jpg'

        # save the picture to a file
        with open(picture_file, 'wb') as f:
            f.write(response.content)

        self.picture_file = picture_file


class App(tk.Tk):
    def __init__(self, canvas_width, canvas_height):
        super().__init__()
        self.resizable(0, 0)
        self.title('Image Viewer')

        # Progress frame
        self.progress_frame = ttk.Frame(self)

        # configrue the grid to place the progress bar is at the center
        self.progress_frame.columnconfigure(0, weight=1)
        self.progress_frame.rowconfigure(0, weight=1)

        # progressbar
        self.pb = ttk.Progressbar(
            self.progress_frame, orient=tk.HORIZONTAL, mode='indeterminate')
        self.pb.grid(row=0, column=0, sticky=tk.EW, padx=10, pady=10)

        # place the progress frame
        self.progress_frame.grid(row=0, column=0, sticky=tk.NSEW)

        # Picture frame
        self.picture_frame = ttk.Frame(self)

        # canvas width &amp; height
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height

        # canvas
        self.canvas = tk.Canvas(
            self.picture_frame,
            width=self.canvas_width,
            height=self.canvas_height)
        self.canvas.grid(row=0, column=0)

        self.picture_frame.grid(row=0, column=0)

        # Button
        btn = ttk.Button(self, text='Next Picture')
        btn['command'] = self.handle_download
        btn.grid(row=1, column=0)

    def start_downloading(self):
        self.progress_frame.tkraise()
        self.pb.start(20)

    def stop_downloading(self):
        self.picture_frame.tkraise()
        self.pb.stop()

    def set_picture(self, file_path):
        """ Set the picture to the canvas """
        pil_img = Image.open(file_path)

        # resize the picture
        resized_img = pil_img.resize(
            (self.canvas_width, self.canvas_height),
            Image.ANTIALIAS)

        self.img = ImageTk.PhotoImage(resized_img)

        # set background image
        self.bg = self.canvas.create_image(
            0,
            0,
            anchor=tk.NW,
            image=self.img)

    def handle_download(self):
        """ Download a random photo from unsplash """
        self.start_downloading()

        url = 'https://source.unsplash.com/random/640x480'
        download_thread = PictureDownload(url)
        download_thread.start()

        self.monitor(download_thread)

    def monitor(self, download_thread):
        """ Monitor the download thread """
        if download_thread.is_alive():
            self.after(100, lambda: self.monitor(download_thread))
        else:
            self.stop_downloading()
            self.set_picture(download_thread.picture_file)


if __name__ == '__main__':
    app = App(640, 480)
    app.mainloop()
