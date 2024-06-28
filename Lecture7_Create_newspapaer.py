from tkinter import*

newspaper=Tk()
newspaper.title("Newspaper")
newspaper.geometry("1000x700")


news_name=Label(text="Baltistan Times",bg="blue",pady=10,font=20)
news_name.pack()


para=Label(text="This is our news paper the letest news and update ",bg="green",pady=10,padx=12,font=14)
para.pack()

newspaper.main.loop()