from tkinter import*


root=Tk()

def click(event):
    global scvalue
    text=event.widget.cget("text")
    print(text)
    if text=="=":
       if scvalue.set(value).isdigit():
          value=int(scvalue.get())
       else:
           value=eval(screen.get())
       scvalue.set(value)
       screen.update()   
    elif text=="C":
       scvalue.set("")
       screen.update()
    else:
       scvalue.set(scvalue.get()+text)
       screen.update()
    
root.title("Calculator(munawar developers)")
root.geometry("600x800")

scvalue=StringVar()
scvalue=set("")

screen=Entry(root,textvar=scvalue,font="bold")
screen.pack(fill=X,pady=10,padx=10)

f1=Frame(root,bg="grey")
b=Button(f1,text="9",pady=12,padx=22,font="lucida 35 bold")
b.pack(side=LEFT,padx=12,pady=12)
b.bind("<Button-1>",click)

f1.pack()


b=Button(f1,text="8",pady=12,padx=22,font="lucida 35 bold")
b.pack(side=LEFT,padx=12,pady=12)
b.bind("<Button-1>",click)

b=Button(f1,text="7",pady=12,padx=22,font="lucida 35 bold")
b.pack(side=LEFT,padx=12,pady=12)
b.bind("<Button-1>",click)


f1=Frame(root,bg="grey")
b=Button(f1,text="6",pady=12,padx=22,font="lucida 35 bold")
b.pack(side=LEFT,padx=12,pady=12)
b.bind("<Button-1>",click)

f1.pack()


b=Button(f1,text="5",pady=12,padx=22,font="lucida 35 bold")
b.pack(side=LEFT,padx=12,pady=12)
b.bind("<Button-1>",click)

b=Button(f1,text="4",pady=12,padx=22,font="lucida 35 bold")
b.pack(side=LEFT,padx=12,pady=12)
b.bind("<Button-1>",click)

f1.pack()


f1=Frame(root,bg="grey")
b=Button(f1,text="3",pady=12,padx=22,font="lucida 35 bold")
b.pack(side=LEFT,padx=12,pady=12)
b.bind("<Button-1>",click)



b=Button(f1,text="2",pady=12,padx=22,font="lucida 35 bold")
b.pack(side=LEFT,padx=12,pady=12)
b.bind("<Button-1>",click)

b=Button(f1,text="1",pady=12,padx=22,font="lucida 35 bold")
b.pack(side=LEFT,padx=12,pady=12)
b.bind("<Button-1>",click)

f1.pack()

f1=Frame(root,bg="grey")
b=Button(f1,text="0",pady=12,padx=22,font="lucida 35 bold")
b.pack(side=LEFT,padx=12,pady=12)
b.bind("<Button-1>",click)



b=Button(f1,text="C",pady=12,padx=22,font="lucida 35 bold")
b.pack(side=LEFT,padx=12,pady=12)
b.bind("<Button-1>",click)

b=Button(f1,text="+",pady=12,padx=22,font="lucida 35 bold")
b.pack(side=LEFT,padx=12,pady=12)
b.bind("<Button-1>",click)

f1.pack()


f1=Frame(root,bg="grey")
b=Button(f1,text="*",pady=12,padx=12,font="lucida 35 bold")
b.pack(side=LEFT,padx=12,pady=12)
b.bind("<Button-1>",click)



b=Button(f1,text="%",pady=12,padx=22,font="lucida 35 bold")
b.pack(side=LEFT,padx=12,pady=12)
b.bind("<Button-1>",click)

b=Button(f1,text="=",pady=12,padx=22,font="lucida 35 bold")
b.pack(side=LEFT,padx=12,pady=12)
b.bind("<Button-1>",click)

f1.pack()

f1=Frame(root,bg="grey")
b=Button(f1,text="*",pady=12,padx=12,font="lucida 35 bold")
b.pack(side=LEFT,padx=12,pady=12)
b.bind("<Button-1>",click)



b=Button(f1,text="%",pady=12,padx=22,font="lucida 35 bold")
b.pack(side=LEFT,padx=12,pady=12)
b.bind("<Button-1>",click)

b=Button(f1,text="=",pady=12,padx=22,font="lucida 35 bold")
b.pack(side=LEFT,padx=12,pady=12)
b.bind("<Button-1>",click)

f1.pack()
root.mainloop()