from tkinter import *
from tkinter import Tk



def login():
    reg_button.destroy()
    log_button.destroy()


    window.quit()
    log_window = Tk()
    log_window.geometry("250x250")
    log_window.title("login window")

    title_text_l = Label(text="Log-in", fg="black", bg="white", font="courier", width=20)
    title_text_l.pack()

    username_l_storage = StringVar()
    username_l = Entry(textvariable=username_l_storage, width=20)
    username_l.place(x=100, y=30)
    username_l_use = username_l_storage.get()

    password_l_storage = StringVar()
    password_l = Entry(show="*", textvariable=password_l_storage, width=20)
    password_l.place(x=100, y=80)
    password_l_use = password_l_storage.get()

    enter_button_r = Button(text="Enter", fg="blue", bg="white", width=15,)
    enter_button_r.place(x=125, y=115)

    f_l = open(username_l_use, "r+")
    password_l_read = f_l.readline()
    password_l_limit = 5
    password_l_count = 0
    out_of_password_l = False

    while password_l_use != password_l_read and enter_button_r is True and out_of_password_l is False:
        if password_l_count < password_l_limit:
            password_l_count += 1

        else:
            out_of_password_l = True

    log_window.option_clear()




def register():
    log_button.destroy()
    reg_button.destroy()
    window.option_clear()

    title_text_r = Label(text="Register", fg="blue", bg="white", width=20)
    title_text_r.pack()

    username_r_storage = StringVar()
    username_r = Entry(textvariable=username_r_storage)
    username_r.place(x=100, y=30)
    username_r_use = username_r_storage.get()

    password_r_storage = StringVar()
    password_r = Entry(textvariable=password_r_storage, show="*")
    password_r.place(x=100, y=80)
    password_r_use = password_r_storage.get()

    enter_button_r = Button(text="Enter", fg="black", bg="white")
    enter_button_r.place(x=125, y=115)

    if enter_button_r:

        file = open(username_r_use, "r+")
        file.write(password_r_use)














window = Tk()
window.title("login/register")
window.geometry("250x250")

log_button = Button(text=" Login ", fg="black", bg="white", command=login)
reg_button = Button(text="Register", fg="black", bg="white", command=register)
log_button.place(x=50, y=125)
reg_button.place(x=150, y=125)







