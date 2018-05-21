import datetime

class makeFiles():	
	def __init__(self, docDate=None):
		self.docDate = str(
	
	def makeTxt(self):
        tFileThing = open("new.txt", "w")
        tFileThing.write('Author: \n')
        tFileThing.write(docDate)
        tFileThing.close()
        messagebox.showinfo("Info", "A new txt file named 'new' has been created")
		
	def makeHtml(self):
		hFileThing = open("new.html", "w")
		hFileThing.write("<!doctype html>\n")
		hFileThing.write("<html>\n")
		hFileThing.write("<head>\n")
		hFileThing.write("<title></title>\n")
		hFileThing.write("</head>\n")
		hFileThing.write("<body>\n")
		hFileThing.write("</body>\n")
		hFileThing.write("</html>\n")
		hFileThing.close()
		messagebox.showinfo("Info", "A new html file named 'new' has been created"

	# makes a simple Go file
    def makeGo(self):
        gFileThing = open("new.go", "w")
        gFileThing.write("package main \n")
        gFileThing.write("// Author: \n")
        gFileThing.write("// " + str(docDate) + " \n\n")
        gFileThing.write("func main() { \n")
        gFileThing.write("    // add code here \n")
        gFileThing.write("}")
        gFileThing.close()
        messagebox.showinfo("Info", "A new Go file named 'new' has been created")

	# makes a simple python file
    def makePy(self):
        pFileThing = open("new.py", "w")
        pFileThing.write('# Author: \n')
        pFileThing.write('# '+str(docDate) + '\n')
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
        cFileThing.write('// '+str(docDate) + '\n\n')
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
        jFileThing.write('// '+str(docDate) + '\n\n')
        jFileThing.write('import java.io.Console;\n\n')
        jFileThing.write('public class new {\n\n')
        jFileThing.write('public static void(String[] args) {\n')
        jFileThing.write('Console console = System.console();\n')
        jFileThing.write('console.printf("New");\n\n')
        jFileThing.write('\t}\n')
        jFileThing.write('}\n')
        jFileThing.close()
        messagebox.showinfo("Info", "A new java file named 'new' has been created")
