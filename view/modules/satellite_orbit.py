from tkinter import *
from logic.functions import *
import numpy as np
from datetime import datetime, timedelta


class SatelliteOrbit(Frame):
    on_duration_degrees = 55
    off_duration_degrees = 305

    def __init__(self, *args):
        Frame.__init__(self, *args, background="white")

        self.canvas = Canvas(self, width=220, height=220, bg="white")
        self.canvas.pack(pady=20)

        self.planet_image = PhotoImage(file='images/orbit.png').subsample(10, 10)
        self.planet = self.canvas.create_image(0, 0, anchor=NW, image=self.planet_image)

        self.after(1000, self.chanposition)

    def pol2cart(self, rho, phi):
        x = rho * np.cos((phi/180) * np.pi)
        y = rho * np.sin((phi/180) * np.pi)
        return x+105, y+105

    def create_circle(self, x, y, r, canvasName):
        x0 = x - r
        y0 = y - r
        x1 = x + r
        y1 = y + r
        return canvasName.create_oval(x0, y0, x1, y1, fill="#00659f", outline="#00659f")

    def get_position(self):
        on_time_in_seconds = (Data.end_session_time - Data.start_session_time).total_seconds()
        off_time_in_seconds = 86400 - on_time_in_seconds

        if datetime.now() < Data.start_session_time:
            # 22  =>  327
            time_diff = Data.start_session_time - datetime.now()
            seconds = time_diff.total_seconds()
            ratio = seconds / off_time_in_seconds
            return 327 - (305 * ratio)

        elif datetime.now() > Data.end_session_time:
            # 22  =>  327
            time_diff = datetime.now() - Data.end_session_time
            seconds = time_diff.total_seconds()
            # print(seconds)
            ratio = seconds / off_time_in_seconds
            return (305 * ratio) + 22

        else:
            # 327  =>  22
            time_diff = datetime.now() - Data.start_session_time
            seconds = time_diff.total_seconds()
            ratio = seconds / on_time_in_seconds
            return 327 + (55 * ratio)

    def chanposition(self):

        position = self.get_position()

        x, y = self.pol2cart(82, position)

        self.canvas.delete("all")

        self.planet = self.canvas.create_image(0, 0, anchor=NW, image=self.planet_image)

        self.create_circle(x, y, 10, self.canvas)

        self.after(1000, self.chanposition)
