# Author: John Paul Antonovich

import tkinter
from tkinter import messagebox
import tkinter as tk
import random


docDate = str(datetime.today().strftime('%Y-%m-%d')) # using 'str' will increase app performance

class FileMaker(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.mainframe = tkinter.Frame(self.master)
        self.mainframe.pack(fill=None, expand=True)

        self.build_grid()
        self.build_tip()
        self.build_banner()
        self.build_buttons()

	# builds a random tip
    def build_tip(self):
        assortedTips = [
			"the moon is NOT \n made of cheese!",
            "Never forget to commit \n your projects in Git.",
            "Never import more \n libraries than you use in Python.",
            "Read more books!"
        ]

        coolTip = tkinter.Label(
            self.mainframe,
            background="white",
            text=str("Tip: " + random.choice(assortedTips)),
            fg='black',
        )

        coolTip.grid(
            row=0, column=0,
            sticky='ew',
            padx=10, pady=10
        )

	# builds a grid for contents of the tkinter frame
    def build_grid(self):
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(0, weight=0)
        self.mainframe.rowconfigure(1, weight=1)
        self.mainframe.rowconfigure(2, weight=0)

	# builds a mini header
    def build_banner(self):
        banner = tkinter.Label(
            self.mainframe,
            background='orange',
            text="File Maker",
            fg='black',
            font=('Helvetica', 24)
        )
        banner.grid(
            row=0, column=0,
            sticky='ew',
            padx=10, pady=10
        )
	# builds buttons
    def build_buttons(self):
        buttons_frame = tkinter.Frame(self.mainframe)
        buttons_frame.grid(row=2, column=0, sticky='nsew', padx=10, pady=10)
        buttons_frame.columnconfigure(0, weight=1)
        buttons_frame.columnconfigure(1, weight=1)

        self.html_button = tkinter.Button(
			buttons_frame,
			text="Make new Html file",
			command = self.makeHtml,
			fg = "blue"
		)
		
		self.txt_button = tkinter.Button(
            buttons_frame,
            text='Make new txt file',
            command = self.makeTxt,
			fg = "grey"
        )

        self.java_button = tkinter.Button(
            buttons_frame,
            text='Make new java file',
            command = self.makeJava,
			fg = "green"
        )

        self.py_button = tkinter.Button(
            buttons_frame,
            text='Make new Python file',
            command = self.makePy,
	    	fg = "pink"
        )

        self.cpp_button = tkinter.Button(
            buttons_frame,
            text="Make new cpp file",
            command = self.makeCpp,
			fg = "lightblue"
        )

        self.go_button = tkinter.Button(
            buttons_frame,
            text="Make new go file",
            command = self.makeCpp,
			fg = "brown"
        )

        self.txt_button.grid(row=0, column=0, sticky='s')
        self.py_button.grid(row=1, column=0, sticky='s')
        self.cpp_button.grid(row=2, column=0, sticky='s')
        self.java_button.grid(row=3, column=0, sticky='s')
        self.go_button.grid(row=4, column=0, sticky='s')
		self.html_button.grid(row=5, column=0, sticky='s')



# safely runs program
if __name__ == '__main__':
    app = FileMaker()
    app.master.minsize(200, 200)
    app.master.maxsize(200, 200)
    app.master.title("File Maker")
    app.mainloop()
