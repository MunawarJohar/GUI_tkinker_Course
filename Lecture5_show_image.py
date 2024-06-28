#who to show image in tkinter

#image is label
from tkinter import*
#from PIL import Image,ImageTk

root=Tk()
root.geometry("900x900")
photo=PhotoImage(file="profile.PNG")

label=Label(image=photo)
label.pack()

root.mainloop()
    
#pip install pillow