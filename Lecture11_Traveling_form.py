from tkinter import*

root=Tk()

def getvals():
    print("working is processing")

root.geometry("550x600")

#Checkbox and input values

Label(root,text="Wellcome to munawar blogs and tours",font="bold").grid(row=0,column=3)
name=Label(root,text="Name")
phone=Label(root,text="Phone")
gender=Label(root,text="Gender")
email=Label(root,text="Email")

#visit=Label(root,text="Visit which place")



name.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)
email.grid(row=4,column=2)
visit.grid(row=5,column=2)

#tkinter variables 

namevalue=StringVar()
phonevalue=StringVar()
gendervalue=StringVar()
emailvalue=StringVar()
tiketpricevalue=IntVar()

#entries for forms
nameentry=Entry(root,textvariable=namevalue)
phoneentry=Entry(root,textvariable=phonevalue)
genderentry=Entry(root,textvariable=gendervalue)
emailentry=Entry(root,textvariable=emailvalue)


nameentry.grid(row=1,column=3)
phoneentry.grid(row=2,column=3)
genderentry.grid(row=3,column=3)
emailentry.grid(row=4,column=3)

#checkbox
tiketprice=Checkbutton(text="Which tiket do you want?",variable=tiketpricevalue)
tiketprice.grid(row=6,column=3)

#button $ packing it and asssigning it a command
Button(text="Submit Form",command=getvals).grid(row=7,column=3)


root.mainloop()