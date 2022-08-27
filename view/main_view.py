import _thread
import json
from tkinter import *

from matplotlib.backends._backend_tk import NavigationToolbar2Tk
from tkvideo import tkvideo
from logic import ssp
from logic.constants import *
from logic.data import Data
from logic.orders import *
from logic.ssp import *
from view.leo_control import Control
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
        # self.test_button.place(x=0, y=0)
        Data.data_timer_number_lbl.pack(side="right", expand=1, fill="x")
        Data.data_timer_lbl.pack(side="left")

    def dashboard_clicked(self):
        self.p1.lift()

        list = [
                0.5148329879633158, 0.09603074134407774, 0.2334185652622287, 0.991726555623464, 0.2400938649406048,
                0.8886339217942552, 0.35463799802475904, 0.19064301191446675, 0.8753111647210065, 0.3459825849600511,
                0.5148329879633158, 0.09603074134407774, 0.2334185652622287, 0.991726555623464, 0.2400938649406048,
                0.8886339217942552, 0.35463799802475904, 0.19064301191446675, 0.8753111647210065, 0.3459825849600511,
                0.5148329879633158, 0.09603074134407774, 0.2334185652622287, 0.991726555623464, 0.2400938649406048]

        Dmy_dict = {"Acceleration": list}
        df = pd.DataFrame(data=Dmy_dict)
        fig3 = df.plot.line(figsize=(8, 2), title="Acceleration", legend="").get_figure()
        Data.plot1.figure = fig3
        # NavigationToolbar2Tk(Data.acceleration_Card.plot, self)
        Data.acceleration_Card.plot.draw()

        self.dashboard_button.config(bg=color_select)
        self.control_button.config(bg=color_deselect)

    def control_clicked(self):
        self.p2.lift()
        self.dashboard_button.config(bg=color_deselect)
        self.control_button.config(bg=color_select)









