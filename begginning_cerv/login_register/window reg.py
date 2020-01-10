import tkinter as tk



global log_run




def login():
    window_1.destroy()

    global log_run
    log_run = True


def register():
    window_1.destroy()

    global reg_run
    reg_run = True




window_1 = tk.Tk()
canvas_1 = tk.Canvas(window_1, width=200, height=100)
window_1.title('login/register')

frame_1 = tk.Frame(window_1, bg='#2ad15f', bd=5)
frame_1.place(relx=0.5, rely=0.5, relwidth=0.75, relheight=0.75, anchor='n')

log_bt = tk.Button(frame_1, text='login', bg='#942ad1', fg='black', font=('Courier', 18), command=login)
log_bt.place(rely=37.5, relx=37.5)

reg_bt = tk.Button(frame_1, text='register', bg='#942ad1', fg='black', font=('Courier', 18), command=register)


if reg_run:
    window_log = tk.Tk()



