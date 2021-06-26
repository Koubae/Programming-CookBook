# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 12:10:04 2019

@author: sangupta

Blog Post --> https://medium.com/lifeandtech/executable-gui-with-python-fc79562a5558
File --> https://drive.google.com/file/d/153pW74-0sXQcdai4AuyXI8Oas8gRfMOA/view
"""
try:
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
# import pdfkit

# Files needed to print the pdf document
# from reportlab.pdfgen import canvas
# from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
# from reportlab.lib.styles import getSampleStyleSheet
# from reportlab.lib.units import inch
import cgi
import tempfile

# file needed to print the document
# import win32api


class ResizingCanvas(tk.Canvas):
    def __init__(self, parent, **kwargs):
        tk.Canvas.__init__(self, parent, **kwargs)
        self.bind("<Configure>", self.on_resize)
        self.height = self.winfo_reqheight()
        self.width = self.winfo_reqwidth()

    def on_resize(self, event):
        # determine the ratio of old width/height to new width/height
        wscale = float(event.width) / self.width
        hscale = float(event.height) / self.height
        self.width = event.width
        self.height = event.height
        # resize the canvas
        self.config(width=self.width, height=self.height)
        # rescale all the objects tagged with the "all" tag
        self.scale("all", 0, 0, wscale, hscale)


class MainApplication:

    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(master, width=450, height=500)
        # to make a frame
        self.frame = tk.Frame(master, bg='white')

        # to place a menu item in the window
        self.menu = tk.Menu(master)
        master.config(menu=self.menu)

        # all the commands for the submenu File
        self.subMenu_file = tk.Menu(self.menu)
        self.menu.add_cascade(label="File", menu=self.subMenu_file)
        self.subMenu_file.add_command(label="Open",
                                      command=self.open_file)
        self.subMenu_file.add_command(label="Save",
                                      command=self.save_report_pdf)
        self.subMenu_file.add_separator()
        self.subMenu_file.add_command(label="Print", command=self.print_file)
        self.subMenu_file.add_separator()
        self.subMenu_file.add_command(label="Exit", command=master.destroy)

        # all the commands for the submenu Help
        self.subMenu_help = tk.Menu(self.menu)
        self.menu.add_cascade(label="Help", menu=self.subMenu_help)
        self.subMenu_help.add_command(label="Help", command=self.open_help)
        self.subMenu_help.add_command(label="Print Diag",
                                      command=self.open_wiring_diag)

        ############################################################################################
        # Frame general information
        # this frame is placed in the original frame
        self.frame_gen_inf = tk.Frame(self.frame, bd='10', padx=3, pady=3)
        self.label_gen_inf = tk.Label(self.frame_gen_inf,
                                      text='General Information',
                                      bd='3', fg='blue', font='Helvetica 9 bold')
        self.label_operator = tk.Label(self.frame_gen_inf, text='Name',
                                       bd='3')
        self.label_vessel = tk.Label(self.frame_gen_inf, text='ID no.', bd='3')
        self.entry_operator = tk.Entry(self.frame_gen_inf, bd='3',
                                       justify="center")
        self.entry_vessel = tk.Entry(self.frame_gen_inf, bd='3',
                                     justify="center")

        # place used to place the widgets in the frame
        self.label_gen_inf.place(relx=0.009, rely=0.009, relheight=0.25)
        self.label_operator.place(relx=0.08, rely=0.45, relheight=0.25)
        self.entry_operator.place(relx=0.22, rely=0.45, relwidth=0.2,
                                  relheight=0.3)
        self.label_vessel.place(relx=0.55, rely=0.45, relheight=0.25)
        self.entry_vessel.place(relx=0.66, rely=0.45, relwidth=0.25,
                                relheight=0.3)

        ############################################################################################
        # frame test Selection
        self.frame_test = tk.Frame(self.frame, bd='10', padx=3, pady=3)
        self.label_test = tk.Label(self.frame_test, text='Test Selection',
                                   bd='3', fg='blue', font='Helvetica 9 bold')

        # variables for the checkboxes
        self.check_but_1 = tk.IntVar()
        self.check_but_2 = tk.IntVar()
        self.check_but_3 = tk.IntVar()
        self.check_but_4 = tk.IntVar()
        self.check_but_5 = tk.IntVar()

        # checkboxes, the results can be read usig the check_but var,get funct
        self.check_button_1 = tk.Checkbutton(self.frame_test,
                                             text="1", variable=self.check_but_1, onvalue=1, offvalue=0)
        self.check_button_2 = tk.Checkbutton(self.frame_test,
                                             text="2", variable=self.check_but_2, onvalue=1, offvalue=0)
        self.check_button_3 = tk.Checkbutton(self.frame_test,
                                             text="3", variable=self.check_but_3, onvalue=1, offvalue=0)
        self.check_button_4 = tk.Checkbutton(self.frame_test,
                                             text="4", variable=self.check_but_4, onvalue=1, offvalue=0)
        self.check_button_5 = tk.Checkbutton(self.frame_test,
                                             text="5", variable=self.check_but_5, onvalue=1, offvalue=0)

        # placing all the checkboxes
        self.label_test.place(relx=0.009, rely=0.009, relheight=0.25)
        self.check_button_1.place(relx=0.009, rely=0.45,
                                  relheight=0.25, relwidth=0.15)
        self.check_button_2.place(relx=0.20, rely=0.45,
                                  relheight=0.25, relwidth=0.15)
        self.check_button_3.place(relx=0.40, rely=0.45,
                                  relheight=0.25, relwidth=0.15)
        self.check_button_4.place(relx=0.60, rely=0.45,
                                  relheight=0.25, relwidth=0.15)
        self.check_button_5.place(relx=0.80, rely=0.45,
                                  relheight=0.25, relwidth=0.15)

        ##########################################################################################
        # frame for the Results
        self.frame_results = tk.Frame(self.frame, bd='10')
        self.canvas_result = ResizingCanvas(self.frame_results)
        self.canvas_result.place(relx=0, rely=0, relheight=1, relwidth=1)
        self.label_results = tk.Label(self.frame_results, text='Result',
                                      bd='1', fg='blue', font='Helvetica 9 bold')

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
        self.result_1 = self.canvas_result.create_oval(22 - rad_x,
                                                       190 - rad_y, 22 + rad_x, 190 + rad_y, fill="green",
                                                       outline="#DDD", width=2)
        self.result_2 = self.canvas_result.create_oval(95 - rad_x,
                                                       190 - rad_y, 95 + rad_x, 190 + rad_y, fill="green",
                                                       outline="#DDD", width=2)
        self.result_3 = self.canvas_result.create_oval(172 - rad_x,
                                                       190 - rad_y, 172 + rad_x, 190 + rad_y, fill="red",
                                                       outline="#DDD", width=2)
        self.result_4 = self.canvas_result.create_oval(248 - rad_x,
                                                       190 - rad_y, 248 + rad_x, 190 + rad_y, fill="green",
                                                       outline="#DDD", width=2)
        self.result_5 = self.canvas_result.create_oval(325 - rad_x,
                                                       190 - rad_y, 325 + rad_x, 190 + rad_y, fill="gray",
                                                       outline="#DDD", width=2)

        # Text for the result LED's
        self.label_result_1 = self.canvas_result.create_text((45, 190),
                                                             text="")
        self.label_result_2 = self.canvas_result.create_text((118, 190),
                                                             text="OK")
        self.label_result_3 = self.canvas_result.create_text((195, 190),
                                                             text="OK")
        self.label_result_4 = self.canvas_result.create_text((271, 190),
                                                             text="OK")
        self.label_result_5 = self.canvas_result.create_text((348, 190),
                                                             text="OK")

        ###########################################################################################
        # frame for the Status
        self.frame_status = tk.Frame(self.frame, bd='10', padx=3, pady=3)
        self.label_status = tk.Label(self.frame_status, text='Status', bd='3',
                                     fg='blue', font='Helvetica 9 bold')

        self.edit_space = tkst.ScrolledText(master=self.frame_status,
                                            wrap='word', bg='white')
        self.edit_space.place(relx=0, rely=0.13, relheight=0.9, relwidth=1)

        self.label_status.place(relx=0.009, rely=0, relheight=0.11)

        ############################################################################################
        # placing the buttons below
        self.frame_button = tk.Frame(self.frame, bd='3', padx=3, pady=3)
        self.button_start = tk.Button(self.frame_button, text='Begin',
                                      command=self.start_clicked)
        self.button_cancel = tk.Button(self.frame_button, text='Cancel',
                                       command=master.destroy)

        self.button_start.place(relx=0.6, rely=0.22, relheight=0.8,
                                relwidth=0.18)
        self.button_cancel.place(relx=0.8, rely=0.22, relheight=0.8,
                                 relwidth=0.18)

        ###############################################################################################
        # all the frames are placed in their respective positions

        self.frame_gen_inf.place(relx=0.005, rely=0.005, relwidth=0.99,
                                 relheight=0.18)
        self.frame_test.place(relx=0.005, rely=0.190, relwidth=0.99,
                              relheight=0.18)
        self.frame_results.place(relx=0.005, rely=0.375, relwidth=0.99,
                                 relheight=0.18)
        self.frame_status.place(relx=0.005, rely=0.560, relwidth=0.99,
                                relheight=0.35)
        self.frame_button.place(relx=0.005, rely=0.915, relwidth=0.99,
                                relheight=0.08)

        self.frame.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.96)
        self.canvas.pack()
        ##############################################################################################


    # To save the report as a txt file change the function in the menu command above
    def save_report_txt(self):
        text_report = self.edit_space.get("1.0", 'end-1c')
        tkm.showinfo('Message Info', 'Saving file with current time')
        local_time = time.strftime("%m_%d_%Y_%H_%M_%S")
        with open("Report " + str(local_time) + ".txt", "a") as outf:
            outf.write(text_report)

    # To save the report in pdf format, saves whatever is in the status box
    def save_report_pdf(self):
        text_report = self.edit_space.get("1.0", 'end-1c')
        tkm.showinfo('Message Info', 'Saving file with current time')
        local_time = time.strftime("%m_%d_%Y_%H_%M_%S")
        pdf_file_name = "Report " + str(self.entry_operator) + " " + str(self.entry_vessel) + " " +\
                        str(local_time) + ".pdf"

        doc = SimpleDocTemplate(pdf_file_name)

        styles = getSampleStyleSheet()
        h3 = styles["h3"]
        normal = styles["Normal"]

        text = text_report
        # print(text)

        story = [Paragraph("Report", h3)]
        if text:
            story.append(Paragraph(text, normal))

        story.append(Spacer(1, 0.1 * inch))

        doc.build(story)

    # To print the report in pdf format, prints whatever is in the status box
    def print_file(self):
        text_report = self.edit_space.get("1.0", 'end-1c')
        tkm.showinfo('Message Info', 'Printing and Saving the Report')
        local_time = time.strftime("%m_%d_%Y_%H_%M_%S")
        pdf_file_name = "Report " + str(local_time) + ".pdf"

        doc = SimpleDocTemplate(pdf_file_name)

        styles = getSampleStyleSheet()
        h3 = styles["h3"]
        normal = styles["Normal"]

        text = text_report
        # print(text)

        story = [Paragraph("Report", h3)]
        if text:
            story.append(Paragraph(text, normal))

        story.append(Spacer(1, 0.1 * inch))

        doc.build(story)
        win32api.ShellExecute(0, "print", pdf_file_name, None, ".", 0)

    # let's the user open up any kind of file from the computer with the GUI
    def open_file(self):
        self.master.fileName = askopenfilename(title="Select file")
        # print(self.master.fileName)
        if self.master.fileName:
            os.startfile(self.master.fileName)

    # To open up the help document
    def open_help(self):
        help_add = "Help.txt"
        if help_add:
            os.startfile(help_add)
        else:
            tkm.showinfo('Message Info', "Sorry the help isn't available")

    # To open the wiring diagram
    def open_wiring_diag(self):
        diag_add = "wiring_diagram.jpg"
        if diag_add:
            os.startfile(diag_add)
        else:
            tkm.showinfo('Message Info', "Sorry the help isn't available")

    # This function is called when the start button is clicked
    def start_clicked(self):
        print("Start is clicked")
        print('the Operator is: ', self.entry_operator.get())
        print("the vessel Number is: ", self.entry_vessel.get())
        if self.check_but_1.get() == 1:
            print("Testing for ESM 1")
        if self.check_but_2.get() == 1:
            print("Testing for ESM 2")

    # This function is just a test function assigned to buttons which don't have a specifc function
    def nothing(self):
        print("I am working perfectly")


window = tk.Tk()
window.title("Example for Tkinter")
c = MainApplication(window)
window.mainloop()  # keeps the application open
