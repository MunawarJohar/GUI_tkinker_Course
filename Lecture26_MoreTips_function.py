from tkinter import*

root=Tk()
root.geometry("577x600")
root.title("More tips and insert icon")
root.wm_iconbitmap("s.ico")
root.configure(background="green")

width=root.winfo_screenwidth()
height=root.winfo_screenheight()

print(f"{width}x{height}")
Button(text="Closed",command=root.destroy).pack(side=BOTTOM)
root.mainloop()