from tkinter import*

root=Tk()

#def select():
#    Print("Your favourite Game is {var.get()}.thanks for choice"

root.geometry("500x600")
root.title("Check Radio Button")

var=IntVar()
#var.set(2)  #if we uncomment this line then check football automitically

Label(root,text="What is your favourite Game",justify=LEFT,padx=16).pack()

radio=Radiobutton(root,text="Cricket",padx=16,variable=var,value=1).pack(anchor="w")
radio=Radiobutton(root,text="Football",padx=16,variable=var,value=2).pack(anchor="w")
radio=Radiobutton(root,text="walliball",padx=16,variable=var,value=3).pack(anchor="w")
radio=Radiobutton(root,text="tenise",padx=16,variable=var,value=4).pack(anchor="w")
radio=Radiobutton(root,text="badmenten",padx=16,variable=var,value=5).pack(anchor="w")

Button(root,text="You favourite game is").pack()
#Button(root,text="You favourite game is",command=select).pack()
root.mainloop()