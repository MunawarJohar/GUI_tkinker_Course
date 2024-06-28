from tkinter import*
root=Tk()

def s():
   print("the form is submited")

root.geometry("550x600")

 
name=Label(root,text="Name")

password=Label(root,text="password")

#row0 column 0 by default
name.grid()
password.grid(row=1)

#Entry widget is widget thruogh we take input

#Classes of  variabe in tkinter
#BooleenVar,DoubleVar,IntVar,StringVar

namevalue=StringVar()
passvalue=StringVar()


nameentry=Entry(root,textvariable=namevalue)
passentry=Entry(root,textvariable=passvalue)

nameentry.grid(row=0,column=1)
passentry.grid(row=1,column=1)

Button(text="Submit",command=s).grid(row=2)

root.mainloop()