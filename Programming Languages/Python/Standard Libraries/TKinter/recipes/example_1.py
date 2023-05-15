# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 12:10:04 2019

@author: sangupta
@fixes and improvements: Federico Bau  | 15th Mon May 2023

Blog Post --> https://medium.com/lifeandtech/executable-gui-with-python-fc79562a5558
"""
try:  # python 2.7
    import Tkinter as tk
    import tkMessageBox as tkm
    import ScrolledText as tkst
    from tkFileDialog import askopenfilename
except ImportError:
    import tkinter as tk
    import tkinter.messagebox as tkm
    import tkinter.scrolledtext as tkst
    from tkinter.filedialog import askopenfilename


import time
import os

try:
    # Files needed to print the pdf document
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.lib.units import inch
except ImportError as error:
    print(f"Missing Dependency 'reportlab' required for document functionalities, error {error}")


# file needed to print the document
try:
    import win32api
except ImportError as error:
    print(f"Error importing win32api, error : {error}")


class ResizingCanvas(tk.Canvas):
    def __init__(self, parent, **kwargs):
        tk.Canvas.__init__(self, parent, **kwargs)
        self.bind("<Configure>", self.on_resize)
        self.height = self.winfo_reqheight()
        self.width = self.winfo_reqwidth()

    def on_resize(self, event):
        # determine the ratio of old width/height to new width/height
        scale_width = float(event.width) / self.width
        scale_height = float(event.height) / self.height
        self.width = event.width
        self.height = event.height
        # resize the canvas
        self.config(width=self.width, height=self.height)
        # rescale all the objects tagged with the "all" tag
        self.scale("all", 0, 0, scale_width, scale_height)


class MenuFile(tk.Menu):
    def __init__(self, app: 'MainApplication', menu: 'MenuMain', cnf=None, **kw):
        super().__init__(app.master, cnf or {}, **kw)
        self.app: MainApplication = app
        self.master: tk.Tk = self.app.master
        self.menu: 'MenuMain' = menu

        self.add_command(label="Open", command=self.open_file)
        self.add_command(label="Save", command=self.save_report_pdf)
        self.add_separator()
        self.add_command(label="Print", command=self.print_file)
        self.add_separator()
        self.add_command(label="Exit", command=self.master.destroy)

    def open_file(self):
        self.master.fileName = askopenfilename(title="Select file")
        if self.master.fileName:
            os.startfile(self.master.fileName)

    def save_report_pdf(self):
        text_report = self.app.edit_space.get("1.0", 'end-1c')
        tkm.showinfo('Message Info', 'Saving file with current time')
        local_time = time.strftime("%m_%d_%Y_%H_%M_%S")
        pdf_file_name = "Report " + str(self.app.entry_operator) + " " + str(self.app.entry_vessel) + " " + \
                        str(local_time) + ".pdf"

        doc = SimpleDocTemplate(pdf_file_name)

        styles = getSampleStyleSheet()
        h3 = styles["h3"]
        normal = styles["Normal"]

        text = text_report
        story = [Paragraph("Report", h3)]
        if text:
            story.append(Paragraph(text, normal))

        story.append(Spacer(1, 0.1 * inch))
        doc.build(story)

    def print_file(self):
        text_report = self.app.edit_space.get("1.0", 'end-1c')
        tkm.showinfo('Message Info', 'Printing and Saving the Report')
        local_time = time.strftime("%m_%d_%Y_%H_%M_%S")
        pdf_file_name = "Report " + str(local_time) + ".pdf"

        doc = SimpleDocTemplate(pdf_file_name)

        styles = getSampleStyleSheet()
        h3 = styles["h3"]
        normal = styles["Normal"]

        text = text_report
        story = [Paragraph("Report", h3)]
        if text:
            story.append(Paragraph(text, normal))

        story.append(Spacer(1, 0.1 * inch))

        doc.build(story)
        win32api.ShellExecute(0, "print", pdf_file_name, None, ".", 0)


class MenuHelp(tk.Menu):
    def __init__(self, app: 'MainApplication', menu: 'MenuMain', cnf=None, **kw):
        super().__init__(app.master, cnf or {}, **kw)
        self.app: MainApplication = app
        self.master: tk.Tk = self.app.master
        self.menu: 'MenuMain' = menu

        self.add_command(label="Help", command=self.open_help)
        self.add_command(label="Print Diag", command=self.open_wiring_diag)

    @staticmethod
    def open_help():
        help_add = os.path.join("assets", "help.txt")
        if help_add:
            os.startfile(help_add)
        else:
            tkm.showinfo('Message Info', "Sorry the help isn't available")

    @staticmethod
    def open_wiring_diag():
        file_name = "python.png"
        diag_add = os.path.join("assets", file_name)
        try:
            os.startfile(diag_add)
        except FileNotFoundError as error:
            tkm.showwarning('Error', f"Error while opening file {file_name}, error {error}")

class MenuMain(tk.Menu):
    def __init__(self, app: 'MainApplication' = None, cnf=None, **kw):
        super().__init__(app.master, cnf or {}, **kw)
        self.app: MainApplication = app
        self.master: tk.Tk = self.app.master
        self.master.config(menu=self)

        self.menu_file: MenuFile = MenuFile(self.app, self)
        self.add_cascade(label="File", menu=self.menu_file)

        self.menu_help: MenuHelp = MenuHelp(self.app, self)
        self.add_cascade(label="Help", menu=self.menu_help)


class MainApplication:

    def __init__(self):
        self.master: tk.Tk = tk.Tk()
        self.master.title("Example for Tkinter")

        self.canvas = tk.Canvas(self.master, width=450, height=500)
        # to make a frame
        self.frame = tk.Frame(self.master, bg='white')

        # to place a menu item in the window
        self.menu = MenuMain(self)

        ############################################################################################
        # Frame general information
        # this frame is placed in the original frame
        self.frame_gen_inf = tk.Frame(self.frame, bd='10', padx=3, pady=3)

        self.label_gen_inf = tk.Label(self.frame_gen_inf, text='General Information', bd='3', fg='blue', font='Helvetica 9 bold')
        self.label_gen_inf.place(relx=0.009, rely=0.009, relheight=0.25)

        self.label_operator = tk.Label(self.frame_gen_inf, text='Name', bd='3')
        self.entry_vessel = tk.Entry(self.frame_gen_inf, bd='3', justify="center")
        self.label_operator.place(relx=0.08, rely=0.45, relheight=0.25)
        self.entry_vessel.place(relx=0.66, rely=0.45, relwidth=0.25, relheight=0.3)

        self.label_vessel = tk.Label(self.frame_gen_inf, text='ID no.', bd='3')
        self.entry_operator = tk.Entry(self.frame_gen_inf, bd='3', justify="center")
        self.label_vessel.place(relx=0.55, rely=0.45, relheight=0.25)
        self.entry_operator.place(relx=0.22, rely=0.45, relwidth=0.2, relheight=0.3)

        ############################################################################################
        # frame test Selection
        self.frame_test = tk.Frame(self.frame, bd='10', padx=3, pady=3)
        self.label_test = tk.Label(self.frame_test, text='Test Selection', bd='3', fg='blue', font='Helvetica 9 bold')

        # variables for the checkboxes
        self.check_but_1 = tk.IntVar()
        self.check_but_2 = tk.IntVar()
        self.check_but_3 = tk.IntVar()
        self.check_but_4 = tk.IntVar()
        self.check_but_5 = tk.IntVar()

        # checkboxes, the results can be read usig the check_but var,get funct
        self.check_button_1 = tk.Checkbutton(self.frame_test, text="1", variable=self.check_but_1, onvalue=1, offvalue=0)
        self.check_button_2 = tk.Checkbutton(self.frame_test, text="2", variable=self.check_but_2, onvalue=1, offvalue=0)
        self.check_button_3 = tk.Checkbutton(self.frame_test, text="3", variable=self.check_but_3, onvalue=1, offvalue=0)
        self.check_button_4 = tk.Checkbutton(self.frame_test, text="4", variable=self.check_but_4, onvalue=1, offvalue=0)
        self.check_button_5 = tk.Checkbutton(self.frame_test, text="5", variable=self.check_but_5, onvalue=1, offvalue=0)

        # placing all the checkboxes
        self.label_test.place(relx=0.009, rely=0.009, relheight=0.25)
        self.check_button_1.place(relx=0.009, rely=0.45,relheight=0.25, relwidth=0.15)
        self.check_button_2.place(relx=0.20, rely=0.45, relheight=0.25, relwidth=0.15)
        self.check_button_3.place(relx=0.40, rely=0.45, relheight=0.25, relwidth=0.15)
        self.check_button_4.place(relx=0.60, rely=0.45, relheight=0.25, relwidth=0.15)
        self.check_button_5.place(relx=0.80, rely=0.45, relheight=0.25, relwidth=0.15)

        ##########################################################################################
        # frame for the Results
        self.frame_results = tk.Frame(self.frame, bd='10')
        self.canvas_result = ResizingCanvas(self.frame_results)
        self.canvas_result.place(relx=0, rely=0, relheight=1, relwidth=1)
        self.label_results = tk.Label(self.frame_results, text='Result', bd='1', fg='blue', font='Helvetica 9 bold')

        # Labels for different options
        self.label_1 = tk.Label(self.frame_results, text='1')
        self.label_2 = tk.Label(self.frame_results, text='2')
        self.label_3 = tk.Label(self.frame_results, text='3')
        self.label_4 = tk.Label(self.frame_results, text='4')
        self.label_5 = tk.Label(self.frame_results, text='5')

        # placing all the labels
        self.label_results.place(relx=0.025, rely=0.009, relheight=0.25)
        self.label_1.place(relx=0.009, rely=0.30, relheight=0.25, relwidth=0.15)
        self.label_2.place(relx=0.20, rely=0.30, relheight=0.25, relwidth=0.15)
        self.label_3.place(relx=0.40, rely=0.30, relheight=0.25, relwidth=0.15)
        self.label_4.place(relx=0.60, rely=0.30, relheight=0.25, relwidth=0.15)
        self.label_5.place(relx=0.80, rely=0.30, relheight=0.25, relwidth=0.15)

        # creating the circles to display the result
        rad_x = 5.5
        rad_y = 22
        self.result_1 = self.canvas_result.create_oval(22 - rad_x, 190 - rad_y, 22 + rad_x, 190 + rad_y, fill="green", outline="#DDD", width=2)
        self.result_2 = self.canvas_result.create_oval(95 - rad_x, 190 - rad_y, 95 + rad_x, 190 + rad_y, fill="green", outline="#DDD", width=2)
        self.result_3 = self.canvas_result.create_oval(172 - rad_x,  190 - rad_y, 172 + rad_x, 190 + rad_y, fill="red", outline="#DDD", width=2)
        self.result_4 = self.canvas_result.create_oval(248 - rad_x, 190 - rad_y, 248 + rad_x, 190 + rad_y, fill="green", outline="#DDD", width=2)
        self.result_5 = self.canvas_result.create_oval(325 - rad_x, 190 - rad_y, 325 + rad_x, 190 + rad_y, fill="gray", outline="#DDD", width=2)

        # Text for the result LED's
        self.label_result_1 = self.canvas_result.create_text((45, 190), text="")
        self.label_result_2 = self.canvas_result.create_text((118, 190), text="OK")
        self.label_result_3 = self.canvas_result.create_text((195, 190), text="OK")
        self.label_result_4 = self.canvas_result.create_text((271, 190), text="OK")
        self.label_result_5 = self.canvas_result.create_text((348, 190), text="OK")

        ###########################################################################################
        # frame for the Status
        self.frame_status = tk.Frame(self.frame, bd='10', padx=3, pady=3)
        self.label_status = tk.Label(self.frame_status, text='Status', bd='3', fg='blue', font='Helvetica 9 bold')

        self.edit_space = tkst.ScrolledText(master=self.frame_status, wrap='word', bg='white')
        self.edit_space.place(relx=0, rely=0.13, relheight=0.9, relwidth=1)

        self.label_status.place(relx=0.009, rely=0, relheight=0.11)

        ############################################################################################
        # placing the buttons below
        self.frame_button = tk.Frame(self.frame, bd='3', padx=3, pady=3)
        self.button_start = tk.Button(self.frame_button, text='Begin', command=self.start_clicked)
        self.button_cancel = tk.Button(self.frame_button, text='Cancel', command=self.master.destroy)

        self.button_start.place(relx=0.6, rely=0.22, relheight=0.8, relwidth=0.18)
        self.button_cancel.place(relx=0.8, rely=0.22, relheight=0.8,relwidth=0.18)

        ###############################################################################################
        # all the frames are placed in their respective positions

        self.frame_gen_inf.place(relx=0.005, rely=0.005, relwidth=0.99, relheight=0.18)
        self.frame_test.place(relx=0.005, rely=0.190, relwidth=0.99, relheight=0.18)
        self.frame_results.place(relx=0.005, rely=0.375, relwidth=0.99, relheight=0.18)
        self.frame_status.place(relx=0.005, rely=0.560, relwidth=0.99, relheight=0.35)
        self.frame_button.place(relx=0.005, rely=0.915, relwidth=0.99, relheight=0.08)

        self.frame.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.96)
        self.canvas.pack()
        ##############################################################################################

    def __call__(self) -> None:
        self.master.mainloop()

    def save_report_txt(self):
        text_report = self.edit_space.get("1.0", 'end-1c')
        tkm.showinfo('Message Info', 'Saving file with current time')
        local_time = time.strftime("%m_%d_%Y_%H_%M_%S")
        with open("Report " + str(local_time) + ".txt", "a") as outf:
            outf.write(text_report)

    def start_clicked(self):
        print("Start is clicked")
        print('the Operator is: ', self.entry_operator.get())
        print("the vessel Number is: ", self.entry_vessel.get())
        if self.check_but_1.get() == 1:
            print("Testing for ESM 1")
        if self.check_but_2.get() == 1:
            print("Testing for ESM 2")


def main():
    MainApplication()()


if __name__ == '__main__':
    main()
