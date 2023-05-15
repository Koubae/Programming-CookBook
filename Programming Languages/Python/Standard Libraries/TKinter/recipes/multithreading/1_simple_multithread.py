# https://www.pythontutorial.net/tkinter/tkinter-thread/
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror
from threading import Thread
import requests


class AsyncDownload(Thread):
	def __init__(self, url):
		super().__init__()

		self.html = None
		self.url = url

	def run(self):
		response = requests.get(self.url)
		self.html = response.text


class App(tk.Tk):
	def __init__(self):
		super().__init__()

		self.title('Webpage Download')
		self.geometry('800x600')
		self.resizable(False, False)

		self.create_header_frame()
		self.create_body_frame()
		self.create_footer_frame()

	def create_header_frame(self):

		self.header = ttk.Frame(self)
		# configure the grid
		self.header.columnconfigure(0, weight=1)
		self.header.columnconfigure(1, weight=10)
		self.header.columnconfigure(2, weight=1)
		# label
		self.label = ttk.Label(self.header, text='URL')
		self.label.grid(column=0, row=0, sticky=tk.W)

		# entry
		self.url_var = tk.StringVar()
		self.url_entry = ttk.Entry(self.header,
								   textvariable=self.url_var,
								   width=80)

		self.url_entry.grid(column=1, row=0, sticky=tk.EW)

		# download button
		self.download_button = ttk.Button(self.header, text='Download')
		self.download_button['command'] = self.handle_download
		self.download_button.grid(column=2, row=0, sticky=tk.E)

		# attach the header frame
		self.header.grid(column=0, row=0, sticky=tk.NSEW, padx=10, pady=10)

	def handle_download(self):
		url = self.url_var.get()
		if url:
			self.download_button['state'] = tk.DISABLED
			self.html.delete(1.0, "end")

			download_thread = AsyncDownload(url)
			download_thread.start()

			self.monitor(download_thread)
		else:
			showerror(title='Error',
					  message='Please enter the URL of the webpage.')

	def monitor(self, thread):
		if thread.is_alive():
			# check the thread every 100ms
			self.after(100, lambda: self.monitor(thread))
		else:
			self.html.insert(1.0, thread.html)
			self.download_button['state'] = tk.NORMAL

	def create_body_frame(self):
		self.body = ttk.Frame(self)
		# text and scrollbar
		self.html = tk.Text(self.body, height=20)
		self.html.grid(column=0, row=1)

		scrollbar = ttk.Scrollbar(self.body,
								  orient='vertical',
								  command=self.html.yview)

		scrollbar.grid(column=1, row=1, sticky=tk.NS)
		self.html['yscrollcommand'] = scrollbar.set

		# attach the body frame
		self.body.grid(column=0, row=1, sticky=tk.NSEW, padx=10, pady=10)

	def create_footer_frame(self):
		self.footer = ttk.Frame(self)
		# configure the grid
		self.footer.columnconfigure(0, weight=1)
		# exit button
		self.exit_button = ttk.Button(self.footer,
									  text='Exit',
									  command=self.destroy)

		self.exit_button.grid(column=0, row=0, sticky=tk.E)

		# attach the footer frame
		self.footer.grid(column=0, row=2, sticky=tk.NSEW, padx=10, pady=10)


if __name__ == "__main__":
	app = App()
	app.mainloop()
