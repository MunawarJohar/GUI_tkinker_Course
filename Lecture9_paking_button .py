#button in GUI Tkinter

from tkinter import*
root=Tk()

def submit():
    print("data is submited")

def this():
    print("more about this")

root.geometry("555x600")
frame=Frame(root,borderwidth=7,bg="grey",relief=SUNKEN)
frame.pack(side=LEFT,anchor="nw")

b1=Button(frame,fg="green",text="Click here",command=submit)
b1.pack(side=LEFT,padx=12)

b2=Button(frame,fg="black",text="Click more",command=this)
b2.pack(side=LEFT,padx=12)

b3=Button(frame,fg="red",text="Click now")
b3.pack(side=LEFT,padx=12)

b4=Button(frame,fg="blue",text="Click me")
b4.pack(side=LEFT,padx=12)

b5=Button(frame,fg="yellow",text="learn moe")
b5.pack(side=LEFT,padx=12)

root.mainloop()