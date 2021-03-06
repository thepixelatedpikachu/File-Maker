# Author: John Paul Antonovich

import tkinter
from tkinter import messagebox
from classTools import NeatStuff
import tkinter as tk
import random

getStuff = NeatStuff()

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

    # makes a simple txt file
	def makeTxt(self):
        tFileThing = open("new.txt", "w")
        tFileThing.write('Author: \n')
        tFileThing.write(getStuff.formDocDate())
        tFileThing.close()
        messagebox.showinfo("Info", "A new txt file named 'new' has been created")

	# makes a simple Go file
    def makeGo(self):
        gFileThing = open("new.go", "w")
        gFileThing.write("package main \n")
        gFileThing.write("// Author: \n")
        gFileThing.write("// " + getStuff.formDocDate() + " \n\n")
        gFileThing.write("func main() { \n")
        gFileThing.write("    // add code here \n")
        gFileThing.write("}")
        gFileThing.close()
        messagebox.showinfo("Info", "A new Go file named 'new' has been created")

	# makes a simple python file
    def makePy(self):
        pFileThing = open("new.py", "w")
        pFileThing.write('# Author: \n')
        pFileThing.write('# '+str(getStuff.formDocDate()) + '\n')
        pFileThing.write('import random \n')
        pFileThing.write('import datetime \n')
        pFileThing.write('import pprint \n')
        pFileThing.write('import os \n')
        pFileThing.write('import tkinter \n')
        pFileThing.close()
        messagebox.showinfo("Info", "A new Python file named 'new' has been created")

	# makes a simple c++ file
    def makeCpp(self):
        cFileThing = open("new.cpp", "w")
        cFileThing.write('// Author: \n')
        cFileThing.write('// '+str(getStuff.formDocDate()) + '\n\n')
        cFileThing.write('#include <iostream>\n')
        cFileThing.write('#include <string>\n')
        cFileThing.write('using namespace std;\n\n')
        cFileThing.write('int main() {\n\n')
        cFileThing.write('  string y;\n')
        cFileThing.write('  getline(cin, y);\n\n')
        cFileThing.write('  return 0;\n')
        cFileThing.write('}')
        cFileThing.close()
        messagebox.showinfo("Info", "A C++ new file named 'new' has been created")

	# makes a simple Java file
    def makeJava(self):
        jFileThing = open("new.java", "w")
        jFileThing.write('// Author: \n')
        jFileThing.write('// '+str(getStuff.formDocDate()) + '\n\n')
        jFileThing.write('import java.io.Console;\n\n')
        jFileThing.write('public class new {\n\n')
        jFileThing.write('public static void(String[] args) {\n')
        jFileThing.write('Console console = System.console();\n')
        jFileThing.write('console.printf("New");\n\n')
        jFileThing.write('\t}\n')
        jFileThing.write('}\n')
        jFileThing.close()
        messagebox.showinfo("Info", "A new java file named 'new' has been created")

# safely runs program
if __name__ == '__main__':
    app = FileMaker()
    app.master.minsize(200, 200)
    app.master.maxsize(200, 200)
    app.master.title("File Maker")
    app.mainloop()
