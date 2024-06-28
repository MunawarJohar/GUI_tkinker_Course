from tkinter import *


root=Tk()

def add():
    global i
    lbx.insert(ACTIVE,f"{i}")
    i+=1
i=0

root.geometry("555x600")

root.title("List Box Lecture")
lbx=Listbox(root)
lbx.pack()

lbx.insert(END,"First_item")

Button(root,text="Add Items",command=add).pack()

root.mainloop()