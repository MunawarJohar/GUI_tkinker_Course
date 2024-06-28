from tkinter import*


root=Tk()
root.geometry("555x600")
root.title("Slider Tutorial")

Label(root,text="Slider ko khancho bhai").pack()

#myslider=Scale(root,from=0,to=200)
#myslider.pack()

myslider2=Scale(root,from=0,to=200,orient=HORIZONTAL)
myslider2.pack()




root.mainloop()