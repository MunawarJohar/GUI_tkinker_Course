#Frame is box like div in html
from tkinter import*
root=Tk()
root.geometry("550x600")

f1=Frame(root,bg="green",borderwidhth=6)
f1.pack(side=LEFT,fill="y")


l=Label(f1,text="Project in tkinter",font="bold")
l.pack(pady=122)

f2=Frame(root,borderwidth=7,bg="grey",relief=SUNKEN)
f2.pack(side=TOP,fill="x")
l=Label(f2,text="Text Editor",fg="red",pady=20)
l.pack(pady=12)




root.mainloop()


