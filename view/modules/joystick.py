import socket
import time
from tkinter import *
import PIL
import cv2
import pickle
import struct


class Joystick(Frame):

    def __init__(self, *args):
        Frame.__init__(self, *args)
        self.time_picker = None
        self.config(bg="white")

        #         --------- Frames -----------
        couple_button_frame = Frame(self, bg="white")
        #         --------- Elements -----------

        self.up_button_image = PhotoImage(file="images/arrow-up.png").subsample(7, 7)
        up_button = Button(self, image=self.up_button_image, relief="flat", bg="white", command=self.up_button_click)

        self.down_button_image = PhotoImage(file="images/arrow-down.png").subsample(7, 7)
        down_button = Button(self, image=self.down_button_image, relief="flat", bg="white", command=self.down_button_click)

        self.right_button_image = PhotoImage(file="images/arrow-right.png").subsample(7, 7)
        right_button = Button(couple_button_frame, image=self.right_button_image, relief="flat", bg="white", command=self.right_button_click)

        self.left_button_image = PhotoImage(file="images/arrow-left.png").subsample(7, 7)
        left_button = Button(couple_button_frame, image=self.left_button_image, relief="flat", bg="white", command=self.left_button_click)

        #         --------- packing -----------

        up_button.pack(side="top")
        couple_button_frame.pack(side="top")
        right_button.pack(side="right")
        left_button.pack(side="left")
        down_button.pack(side="top")

    def up_button_click(self):
        pass
    def down_button_click(self):
        pass
    def right_button_click(self):
        pass
    def left_button_click(self):
        pass
