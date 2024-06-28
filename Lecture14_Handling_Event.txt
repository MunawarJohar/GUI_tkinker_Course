#Handling and Events in Tkinter 
from tkinter import*

root=Tk()

def harry(event):
    print(f"You clicked on the button at {event.x},{event.y}")

root.title("Events in Tkinter")
root.geometry("550x600")

widget=Button(root,text="Click Here")
widget.pack()

widget.bind('Button-1>',harry)
widget.bind('<Double-1>',quit)

root.mainloop()