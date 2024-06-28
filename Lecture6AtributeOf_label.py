from tkinter import*
root=Tk()
root.geometry("444x333")
root.title("This is GUI tutorail harry Bhai")

#import label options

# text=adds the text
# bd=background
# fg=foregruond
# font=sets the font
# padx=x padding
# pady= y padding
# relief=border styling -SUNKEN,RAISED,GROOVE,RIDGE

title_label=Label(text="This is a paragraph \n more about paragraph",bg="red",fg="black",padx=20,pady=12,font=("bold",12))
title_label.pack()

root.mainloop()