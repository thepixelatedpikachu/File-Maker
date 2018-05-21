# Author: John Paul Antonovich

import tkinter
from tkinter import messagebox
import datetime
import os
from classTools import NeatStuff
import tkinter as tk

getStuff = NeatStuff()

class FileMaker(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.mainframe = tkinter.Frame(self.master, bg='white')
        self.mainframe.pack(fill=None, expand=True) #fill=tkinter.BOTH

        self.build_grid()
        self.build_banner()
        self.build_buttons()

    def build_grid(self):
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(0, weight=0)
        self.mainframe.rowconfigure(1, weight=1)
        self.mainframe.rowconfigure(2, weight=0)

    def build_banner(self):
        banner = tkinter.Label(
            self.mainframe,
            background='pink',
            text="File Maker",
            fg='black',
            font=('Helvetica', 24)
        )
        banner.grid(
            row=0, column=0,
            sticky='ew',
            padx=10, pady=10
        )

    def build_buttons(self):
        buttons_frame = tkinter.Frame(self.mainframe)
        buttons_frame.grid(row=2, column=0, sticky='nsew', padx=10, pady=10)
        buttons_frame.columnconfigure(0, weight=1)
        buttons_frame.columnconfigure(1, weight=1)

        self.txt_button = tkinter.Button(
            buttons_frame,
            text='Make new txt file',
            command = self.makeTxt
        )

        self.java_button = tkinter.Button(
            buttons_frame,
            text='Make new java file',
            command = self.makeJava
        )

        self.py_button = tkinter.Button(
            buttons_frame,
            text='Make new Python file',
            command = self.makePy
        )

        self.cpp_button = tkinter.Button(
            buttons_frame,
            text="Make new cpp file",
            command = self.makeCpp
        )
        
        self.go_button = tkinter.Button(
            buttons_frame,
            text="Make new go file",
            command = self.makeCpp
        )

        self.txt_button.grid(row=0, column=0, sticky='s')
        self.py_button.grid(row=1, column=0, sticky='s')
        self.cpp_button.grid(row=2, column=0, sticky='s')
        self.java_button.grid(row=3, column=0, sticky='s')
        self.go_button.grid(row=4, column=0, sticky='s')


    def makeTxt(self):
        tFileThing = open("new.txt", "w")
        tFileThing.write('Author: \n')
        tFileThing.write(getStuff.formDocDate())
        tFileThing.close()
        messagebox.showinfo("Info", "A txt file named 'new' has been created")
        
    def makeGo(self):
        gFileThing = open("new.go", "w")
        gFileThing.write("package main \n")
		gFileThing.write("// Author: \n")
        gFileThing.write("// " + getStuff.formDocDate() + " \n\n")
		gFileThing.write("func main() { \n")
		gFileThing.write("}")
        gFileThing.close()
        messagebox.showinfo("Info", "A Go file named 'new' has been created")

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
        messagebox.showinfo("Info", "A Python file named 'new' has been created")

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
        messagebox.showinfo("Info", "A C++ file named 'new' has been created")

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
        messagebox.showinfo("Info", "A java file named 'new' has been created")

if __name__ == '__main__':
    app = FileMaker()
    app.master.minsize(200, 200)
    app.master.maxsize(200, 200)
    app.master.title("File Maker")
    app.mainloop()
