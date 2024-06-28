from tkinter import*

root=Tk()

def upload():
    statusvar.set("Bussy.....")
    sbar.update()
    import time
    time.sleep(2)
    statusvar.set("Ready study go")

root.geometry("500x600")
root.title("Satus Bar")

statusvar=StringVar()
statusvar.set("Ready")

sbar=Label(root,textvariable=statusvar,relief=SUNKEN,anchor"w")
sbar.pack(side=BOTTOM,fill=X)
Button(root,text="Upload File",command=upload).pack()



root.mainloop()