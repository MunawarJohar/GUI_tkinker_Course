from tkinter import*
#ingasulation
class GUI(Tk):
     def __init__(self):
     super().__init()
     self.geometry("500x660")


     def status(self):
         self.var=StringVar()
         self.var.set("Ready")
         self.statusbar=Label(self,textvar=self.var,relief=SUNKEN,anchor"w")
         self.statusbar.pack()


if __name__ == '__main__':
    window = GUI()
    Window.mainloop()