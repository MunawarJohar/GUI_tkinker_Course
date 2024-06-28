from tkinter import*
import tkinter.messagebox as tmsg

root=Tk()


def mfunction():
    print("Well come to this function")

def help():
    print("i will help you")
    tmsg.showinfo("Help","GUI Help")

def see():
    print("See for visit our website")
    value=tmsg.askquestion("what is your exprience","Are you used tkinter gui")
    if vaule=="Yes"):
       msg="thanks for rating"
    else:
    msg="Sorry we improve the apps"
   tmsg.showinfo("Experience",msg)

def fun():
    answer=tmsg.askretrycancel("Dost ap say karna  hy","sorry Mujay ap say doste nhe karne")
    if answer:
       print("Koshis to karo")
    else:
       print("Koshis say be kuch  nhe hoga")


root.geometry("555x600")
root.title("Pycharm")

#mymenu=Menu(root)
#mymenu.add_command(Label="File",command=mfunction)
#mymenu.add_command(Label="Exit",command=quit)
#root.config(menu=mfunction)

menubar=Menu(root)

m1=Menu(mfunction,teaoff=0)

m1.add_command(Label="New project",command=mfuncion)
m1.add_command(Label="Save as",command=mfuncion)
m1.add_separator()
m1.add_command(Label="Print",command=mfuncion)
m1.add_command(Label="Share",command=mfuncion)
m1.add_command(Label="Exict",command=mfuncion)
root.config(menu=mfunction)

menubar.add_cascade(Label="File",menu=m1)


m2=Menu(mfunction)

m2.add_command(Label="New project",command=mfuncion)
m2.add_command(Label="Save as",command=mfuncion)
m2.add_command(Label="Print",command=mfuncion)
m2.add_command(Label="Share",command=mfuncion)
m2.add_separator()
m2.add_command(Label="Exict",command=mfuncion)
root.config(menu=mfunction)

menubar.add_cascade(Label="Views",menu=m2)




m3=Menu(mfunction)

m3.add_command(Label="Help",command=help)
m3.add_command(Label="See more",command=see)
root.config(menu=mfunction)

root.mainloop()