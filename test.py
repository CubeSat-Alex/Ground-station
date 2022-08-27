from tkinter import *


def clicked():
    button.config(bg="blue")


root = Tk()
root.wm_geometry("500x500+180+50")
root.config(bg="green")
root.iconbitmap('images/satelite.ico')

frame = Frame(root, bg="white")

button = Button(frame, text="button", bg="red", command=clicked, relief="flat")
logo = PhotoImage(file="images/EgsaLogo.png")
angle_lbl = Label(root, image=logo, bg="blue")

button.pack(ipady=50, ipadx=50)
frame.pack(ipady=50, ipadx=50)
angle_lbl.pack(side="right", ipady=50, ipadx=50)

root.mainloop()

e = Entry(root, width=6, fg='black', font=('Arial', 16), background="#e8e8e8")

