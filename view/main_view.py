import _thread
from tkinter import *
from logic.constant.constants import *
from logic.data import Data
from logic.functions.general import change_text_lbl
from model.timer import RepeatedTimer
from view.downloads.downloads import DownloadsPage
from view.geo.geo_control import GEOControl
from view.commands.leo_control import Control
from view.dashboard.dashboard import Dashboard
from view.logs.logs_page import LogsPage


class MainView(Frame):

    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        #         --------- Pages -----------

        self.p1 = Dashboard(self)
        self.p2 = Control(self)
        self.p3 = GEOControl(self)
        self.p4 = DownloadsPage(self)
        self.p5 = LogsPage(self)

        #         --------- Frames -----------

        bottom_navigation_bar = Frame(self, bg=color_background)
        button_frame = Frame(bottom_navigation_bar)
        container = Frame(self)
        Data.header_timer_frame = Frame(bottom_navigation_bar, background="#277BC0")

        # self.logo = PhotoImage(file="images/EgsaLogo.png").subsample(2, 2)
        # self.logo_lbl = Label(image=self.logo, bg="white")
        # self.dashboard_lbl = Label(text="Dashboard", bg="white", font=("Segoe UI", 30, "bold"),
        #                            background="white")

        #         --------- Elements -----------

        self.photo = PhotoImage(file="images/dash.png")
        self.control = PhotoImage(file="images/command-line.png")
        self.downloading = PhotoImage(file="images/downloading.png")
        self.logs = PhotoImage(file="images/log.png")
        self.geo = PhotoImage(file="images/planet.png")

        self.dashboard_button = Button(button_frame, text="   Dashboard", command=self.dashboard_clicked,
                                       image=self.photo, compound="left", relief="flat", bg=color_select,
                                       activebackground="white")
        self.control_button = Button(button_frame, text="    LEO Control", command=self.control_clicked, relief="flat",
                                     image=self.control, compound="left", bg=color_background, activebackground="white")
        self.geo_control_button = Button(button_frame, text="    GEO Control", command=self.geo_control_clicked,
                                         relief="flat", image=self.geo, compound="left", bg=color_background,
                                         activebackground="white")

        self.downloads_button = Button(button_frame, text="    Downloads", command=self.download_clicked,
                                         relief="flat", image=self.downloading, compound="left", bg=color_background,
                                         activebackground="white")

        self.logs_button = Button(button_frame, text="    Logs", command=self.logs_page_clicked,
                                         relief="flat", image=self.logs, compound="left", bg=color_background,
                                         activebackground="white")

        Data.data_timer_lbl = Label(Data.header_timer_frame, text="the next update will be after", bg="white",
                               font=("Segoe UI", 14), background="#277BC0", foreground="white")

        Data.data_timer_number_lbl = Label(Data.header_timer_frame, text="5:33", bg="white", font=("Segoe UI", 22,
                                                                                                   "bold"),
                                           background="#277BC0", foreground="white")

        #         --------- packing -----------

        bottom_navigation_bar.pack(side="bottom", fill="x", expand=0)
        button_frame.pack(anchor="center")
        container.pack(side="top", fill="both", expand=1)

        self.p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        self.p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        self.p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        self.p4.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        self.p5.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        self.dashboard_button.pack(side="left", ipadx=20, ipady=10)
        self.control_button.pack(side="left", ipadx=20, ipady=10)
        self.downloads_button.pack(side="left", ipadx=20, ipady=10)
        self.logs_button.pack(side="left", ipadx=20, ipady=10)
        self.geo_control_button.pack(side="left", ipadx=20, ipady=10)

        self.p1.show()
        Data.repeater_session = RepeatedTimer(1, change_text_lbl)

        Data.header_timer_frame.place(x=0, y=0)
        Data.data_timer_number_lbl.pack(side="right", expand=1, fill="x")
        Data.data_timer_lbl.pack(side="left")

        # self.logo_lbl.place(x=900, y=5)

    def clear_button_color(self):
        self.dashboard_button.config(bg=color_deselect)
        self.control_button.config(bg=color_deselect)
        self.geo_control_button.config(bg=color_deselect)
        self.downloads_button.config(bg=color_deselect)
        self.logs_button.config(bg=color_deselect)

    def dashboard_clicked(self):
        self.p1.lift()
        self.clear_button_color()
        self.dashboard_button.config(bg=color_select)

    def control_clicked(self):
        self.p2.lift()
        self.clear_button_color()
        self.control_button.config(bg=color_select)

    def geo_control_clicked(self):
        self.p3.lift()
        self.clear_button_color()
        self.geo_control_button.config(bg=color_select)

    def logs_page_clicked(self):
        self.p5.lift()
        self.clear_button_color()
        self.logs_button.config(bg=color_select)

    def download_clicked(self):
        self.p4.lift()
        self.clear_button_color()
        self.downloads_button.config(bg=color_select)

