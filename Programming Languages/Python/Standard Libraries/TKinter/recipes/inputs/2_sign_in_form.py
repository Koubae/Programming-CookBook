# https://www.pythontutorial.net/tkinter/tkinter-entry/
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


root = tk.Tk()
root.geometry("800x600")
root.resizable(False, False)
root.title("Sign In")


form = ttk.Frame(root)
form.pack(padx=10, pady=10, fill='x', expand=True)

email = tk.StringVar()
ttk.Label(form, text="Email Address:").pack(fill='x', expand=True)
email_entry = ttk.Entry(form, textvariable=email)
email_entry.pack(fill='x', expand=True)
email_entry.focus()

password = tk.StringVar()
ttk.Label(form, text="Password:").pack(fill="x", expand=True)
password_entry = ttk.Entry(form, textvariable=password, show="*")
password_entry.pack(fill='x', expand=True)


def on_submit():
	data = {
		"email": email.get(),
		"password": password.get()
	}
	showinfo("Login info", f"Form submitted data: {data}")

submit = ttk.Button(form, text="Login", command=on_submit)
submit.pack(fill='x', expand=True, pady=10)

if __name__ == '__main__':
	root.mainloop()