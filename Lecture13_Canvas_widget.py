from tkinter import*

root=Tk()


canvas_width=800
canvas_height=400

root.geometry(f"{canvas_width}x{canvas_height}")
can_widget=Canvas(root,width=canvas_width,height=canvas_height)
can_widget.pack()

#the line goes from the point x1,y1,x2,y2

can_widget.create_line(0,0,800,400,fill="green")
can_widget.create_line(0,400,800,0,fill="red")

#To create a rectangle specify in this order of top left
#and corner of bottom right
can_widget.create_rectangle(3,5,700,300,fill="yellow")

can_widget.create_text(100,100,text="Tkinter Tutorial")

can_widget.create_oval(30,25,224,235)




root.mainloop()