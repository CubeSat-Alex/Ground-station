from tkinter import *
from logic.functions.general import *
import numpy as np


class LDRPanel(Frame):
    ldr_list = [0, 0, 100, 200]
    val = 0

    def __init__(self, *args):
        Frame.__init__(self, *args, background="white", borderwidth=0, highlightbackground="white",
                             highlightthickness=0.2, highlightcolor="white")

        self.canvas = Canvas(self, width=220, height=220, bg="white", borderwidth=0, highlightbackground="white",
                             highlightthickness=0.2, background="white", highlightcolor="white")
        self.canvas.pack(pady=20)

        self.ldr_body_image = PhotoImage(file='images/ldr_body.png').subsample(4, 4)
        self.ldr_body = self.canvas.create_image(0, 0, anchor=NW, image=self.ldr_body_image)

        self.sun_image = PhotoImage(file='images/sun.png').subsample(17, 17)
        self.canvas.create_image(0, 0, anchor=NW, image=self.sun_image)

        self.after(200,  self.chanposition)

    def pol2cart(self, rho, phi):
        x = rho * np.cos((phi/180) * np.pi)
        y = rho * np.sin((phi/180) * np.pi)
        return x+65, y+65


    def get_position(self):

        if max(self.ldr_list) == self.ldr_list[0]:
            if self.ldr_list[1] > self.ldr_list[3]:
                return self.ldr_list[1] * 45 / self.ldr_list[0]
            else:
                return 360 - (self.ldr_list[3] * 45 / self.ldr_list[0])

        elif max(self.ldr_list) == self.ldr_list[1]:
            if self.ldr_list[0] > self.ldr_list[2]:
                return 90 - (self.ldr_list[0] * 45 / self.ldr_list[1])
            else:
                return 90 + (self.ldr_list[2] * 45 / self.ldr_list[1])

        elif max(self.ldr_list) == self.ldr_list[2]:
            if self.ldr_list[1] > self.ldr_list[3]:
                return 180 - (self.ldr_list[1] * 45 / self.ldr_list[2])
            else:
                return 180 + (self.ldr_list[3] * 45 / self.ldr_list[2])

        else:
            # max(self.ldr_list) == self.ldr_list[3]:
            if self.ldr_list[0] > self.ldr_list[2]:
                return 270 + (self.ldr_list[0] * 45 / self.ldr_list[3])
            else:
                return 270 - (self.ldr_list[2] * 45 / self.ldr_list[3])


    def chanposition(self):

        position = self.get_position()
        x, y = self.pol2cart(70, position)
        self.canvas.delete("all")

        self.canvas.create_image(0, 0, anchor=NW, image=self.ldr_body_image)
        self.canvas.create_image(x, y, anchor=NW, image=self.sun_image)

        self.after(300, self.chanposition)
