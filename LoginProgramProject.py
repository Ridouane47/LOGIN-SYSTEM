from tkinter import *
from tkinter import ttk

window = Tk()
window.title("LOGIN SYSTEM")
window.geometry("500x500")
window.resizable(0,0)
window.iconbitmap(r"C:\Users\Pc\OneDrive\Desktop\Login Program Project\password_ico.ico")
window.config(bg="#2C3E50")

#---------Title---------
title = Label(window, text="LOGIN SYSTEM", font=("MS Sans Serif", 15), bg= "black", fg= "white")
title.pack(fill = X)

#---------Frame---------
fr1 = Frame(window, width= "300", height= "350", bg="whitesmoke")
fr1.pack(pady = 30)

#---------photo---------
photo = PhotoImage(file=r"C:\Users\Pc\OneDrive\Desktop\Login Program Project\rsz_1rsz_user (1).png")
p1 = Label(window, image = photo)
p1.place(x = 250 - 128//2, y = 61)

#---------Label---------
lb1 = Label(fr1, text="USERNAME :", bg="whitesmoke", font=("MS Sans Serif", 14))
lb1.place(x = 1, y = 150)
lb2 = Label(fr1, text="PASSWORD :", bg="whitesmoke", font=("MS Sans Serif", 14))
lb2.place(x = 1, y = 200)

#---------Entry---------
en1 = Entry(fr1)
en1.place(x = 130, y = 157)
en2 = Entry(fr1)
en2.place(x = 130, y = 205)

#---------Button---------
bt1 = Button(fr1, text= "LOGIN", font=("MS Sans Serif", 14), bg="whitesmoke", width= 10)
bt1.place(x = 20, y = 280)
bt2 = Button(fr1, text= "SIGN IN", font=("MS Sans Serif", 14), bg="whitesmoke", width= 10)
bt2.place(x = 150, y = 280)

#---------Checkbox---------
ch1 = Checkbutton(fr1, text = "Forget password!", font=("MS Sans Serif", 14), bg="whitesmoke")
ch1.place(x = 40, y = 240)
thanks = Label(fr1, text = "Devaloped by RIDOUANE 2024", font=("MS Sans Serif", 9), bg="whitesmoke")
thanks.place(x = 65, y = 335)

window.mainloop()
#My program is ended