from tkinter import*
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os
#if _ _name _ _ =='_ _main_ _':

root=Tk()
root.title("Untitled -Notepad")

root.geometry("600x600")


def newFile():
    global file
    root.title("Untitled  Notepad")
    file=None
    TextArea.dlete(1.0,END)


def openFile():
    global file
    file=askopenfilename(defaultextension=".txt",filetypes=[("ALL Files","*.*"),("TextDocument","*.txt")])
    if file == "":
        file:None
    else:
        root.title(os.path.basename(file)+"- Notepad")
        TextArea.delete(1.0,END)
        f=open(file,"r")
        TextArea.inser(1.0,f.read())
        f.close()
     


def saveFile():
    global file
    if file==None:
        file=askopenfilename(initialfile='Untitled.txt',defaultextension=".txt",filetypes=[("ALL Files","*.*"),("TextDocument","*.txt")])
        if file=="":
            file=None

        else:
         f=open(file,"w")
         f.write(TextArea.get(1.0,END))
         f.close()

         root.title(os.path.basename(file)+"-Notepad")
         print("Saved As File")
    
    else:
     f=open(file,"w")
     f.write(TextArea.grt(1.0,END))
     f.close()


def quitApp():
    root.destroy()

def cut():
    TextArea.event_generate(("<<Cut>>"))
def copy():
    TextArea.event_generate(("<<Copy>>"))

def paste():
    TextArea.event_generate(("<<Paste>>"))

def about():
    showinfo("Notepad","Notepad by Munawar Johar")



TextArea=Text(root,font="lucida 13")
file=None
TextArea.place(expand=True,file=BOTH)

MenuBar=Menu(root)

#File Menu
FileMenu=Menu(MenuBar)
FileMenu.add_command(Label="New",command=newFile)

FileMenu.add_command(Label="Open",command=openFile)

FileMenu.add_command(Label="Save",command=saveFile)

FileMenu.add_separator()
FileMenu.add_command(Label="Exit",command=quitApp)
MenuBar.add_cascade(Label="File",menu=FileMenu)

#EditMenu
EditMenu=Menu(MenuBar)
EditMenu.add_command(Label="Cut",command=cut)
EditMenu.add_command(Label="Copy",command=copy)
EditMenu.add_command(Label="Paste",command=paste)
MenuBar.add_cascade(Label="Edit",menu=EditMenu)


#Help menu

HelpMenu=Menu(MenuBar)
HelpMenu.add_command(Label="About Notepad",command=about)

MenuBar.add_command(Label="Help",)



root.config(menu=MenuBar)


#Scollbar
Scrollbar=Scrollbar(TextArea)
Scrollbar.place(side=RIGHT,fill=Y)
Scrollbar.config(command=TextArea.yview)
TextArea.config(ysrcollcommand=Scrollbar.set)
