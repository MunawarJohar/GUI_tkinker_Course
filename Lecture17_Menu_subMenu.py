from tkinter import*

root=Tk()


root.geometry("555x600")
root.title("Pycharm")

def mfunction():
    print("Well come to this function")


#mymenu=Menu(root)
#mymenu.add_command(Label="File",command=mfunction)
#mymenu.add_command(Label="Exit",command=quit)
#root.config(menu=mfunction)

menubar=Menu(root)

m1=Menu(mfunction,teaoff=0)

m1.add_command(Label="New project",command=mfunction)
m1.add_command(Label="Save as",command=mfunction)
m1.add_separator()
m1.add_command(Label="Print",command=mfunction)
m1.add_command(Label="Share",command=mfunction)
m1.add_command(Label="Exict",command=mfunction)
root.config(menu=mfunction)

menubar.add_cascade(Label="File",menu=m1)


m2=Menu(mfunction)

m2.add_command(Label="New project",command=mfunction)
m2.add_command(Label="Save as",command=mfunction)
m2.add_command(Label="Print",command=mfunction)
m2.add_command(Label="Share",command=mfunction)
m2.add_separator()
m2.add_command(Label="Exict",command=mfunction)
root.config(menu=mfunction)

menubar.add_cascade(Label="Views",menu=m2)

root.mainloop()