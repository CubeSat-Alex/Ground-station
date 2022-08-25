import _thread
import json
from tkinter import *
from tkvideo import tkvideo
from logic import ssp
from logic.constants import *
from logic.data import Data
from logic.orders import *
from logic.ssp import *
from view.control import Control
from view.dashboard import Dashboard
from view.modules.timer import RepeatedTimer
from logic.functions import *


class MainView(Frame):

    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        #         --------- Pages -----------

        self.p1 = Dashboard(self)
        self.p2 = Control(self)
        self.counter_num = 0
        Data.repeater_session = RepeatedTimer(1, change_text_lbl)

        #         --------- Frames -----------

        bottom_navigation_bar = Frame(self, bg=color_background)
        button_frame = Frame(bottom_navigation_bar)
        container = Frame(self)
        Data.header_timer_frame = Frame(bottom_navigation_bar, background="#277BC0")

        #         --------- Elements -----------

        self.photo = PhotoImage(file="images/dash.png")
        self.control = PhotoImage(file="images/settings.png")

        self.dashboard_button = Button(button_frame, text="   Dashboard", command=self.dashboard_clicked,
                                       image=self.photo, compound="left", relief="flat", bg=color_select,
                                       activebackground="white")
        self.control_button = Button(button_frame, text="    Control", command=self.control_clicked, relief="flat",
                                     image=self.control, compound="left", bg=color_background, activebackground="white")

        Data.data_timer_lbl = Label(Data.header_timer_frame, text="the next update will be after", bg="white",
                               font=("Segoe UI", 14), background="#277BC0", foreground="white")

        Data.data_timer_number_lbl = Label(Data.header_timer_frame, text="5:33", bg="white", font=("Segoe UI", 22, "bold"),
                                    background="#277BC0", foreground="white")

        self.test_button = Button(text="   test button ", command=self.test)
        #         --------- packing -----------

        bottom_navigation_bar.pack(side="bottom", fill="x", expand=0)
        button_frame.pack(anchor="center")
        container.pack(side="top", fill="both", expand=1)

        self.p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        self.p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        self.dashboard_button.pack(side="left", ipadx=20, ipady=10)
        self.control_button.pack(side="left", ipadx=20, ipady=10)

        self.p1.show()
        # self.after(1000, self.counter)

        Data.header_timer_frame.place(x=0, y=0)
        self.test_button.place(x=0, y=0)
        Data.data_timer_number_lbl.pack(side="right", expand=1, fill="x")
        Data.data_timer_lbl.pack(side="left")

    def dashboard_clicked(self):
        self.p1.lift()
        self.dashboard_button.config(bg=color_select)
        self.control_button.config(bg=color_deselect)

    def control_clicked(self):
        self.p2.lift()
        self.dashboard_button.config(bg=color_deselect)
        self.control_button.config(bg=color_select)

    def test(self):
        # getImageAt
        request(getVideoAt)








