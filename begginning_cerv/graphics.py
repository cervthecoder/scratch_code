from tkinter import *


def run():
    name_1 = name_storage.get()
    print(name_1)
    new_text = Label(text=name_1, fg="black", bg="white")
    new_text.place(x=50, y=100)
    name.delete(0, END)


screen = Tk()
screen.title("My first graphics")
screen.geometry("500x500")

welcome_text = Label(text="Hello world", fg="green", bg="blue")
welcome_text.pack()

click_me = Button(text="Click me", fg="black", bg="white", command=run)
click_me.place(x=50, y=80)

name_storage = StringVar()
name = Entry(textvariable=name_storage)
name.place(x=125, y=30)



screen.mainloop()
