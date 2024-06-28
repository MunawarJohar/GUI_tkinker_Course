from tkinter import*

root=Tk()

def update():
    print("GUI Updating is process") 
    root.geometry(f"{width.get()}x{height.get()}")
root.geometry("400x600")

width=StringVar()
height=StringVar()


Entry(root,textvariable=width).pack()
Entry(root,textvariable=height).pack()


Button(root,text="Apply",command=update).pack()
root.mainloop()
