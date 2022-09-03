from tkinter import *


class EmptyCommands(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.config(borderwidth=0, highlightbackground="white", highlightthickness=0.2, bg="white", height=10)

        self.controller = controller
        label = Label(self, text="select a command", font=("", 20, "bold"))
        label.pack(anchor="center", fill="both", expand=1, pady=10)



