from tkinter import*
computer_root=Tk()

#width and height 

computer_root.geometry("444x440")

#for minsize
computer_root.minsize(300,100)

#for max size
computer_root.maxsize(1200,900)

munawar=Label(text="This is a tkinter GUI tutorial",bg="green",pady=12)
munawar.pack()

computer_root.mainloop()