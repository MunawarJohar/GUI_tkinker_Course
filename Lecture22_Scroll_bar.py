from tkinter import*


root=Tk()

root.geometry("550x600")
root.title("Scroll Bar")

#for connecting scrollbar to a widget
#widget(yScrollcommand=scrolbar.et)
#scrollbar.config(command=widget.yview)

scrollbar=Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)


#listbox=Listbox(root,yscrollcommand=scrollbar.set)
#for i in range(40):
#    listbox.insert(END,f"Items{i}")

#listbox.pack()
#listbox.pack(fill="both")
#scrollbar.config(command=listbox.yview)



text=Text(root,yscrollcommand=scrollbar.set,font="bold",bg="green",fg="red")
text.pack(fill=BOTH)
scrollbar.config(command=listbox.yview)


root.mainloop()