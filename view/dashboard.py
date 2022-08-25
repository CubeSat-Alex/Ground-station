from tkinter import *
from logic.constants import *
from logic.data import Data
from view.modules.data_table import DataTableFrame
from view.modules.page import Page
from view.modules.card import Card, MapCard


class Dashboard(Page):

    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.config(bg="white")

        #            --------- Frames -----------

        # image_frame = Frame(self)
        cards_frame = Frame(self, bg="white")
        left_frame = Frame(self, bg="white")
        logo_head_frame = Frame(left_frame, bg="white")

        #         --------- Elements -----------

        # self.background = PhotoImage(file="images/bg.png").subsample(4, 4)
        # background_lbl = Label(cards_frame, image=self.background)

        self.logo = PhotoImage(file="images/EgsaLogo.png").subsample(2, 2)
        self.logo_lbl = Label(logo_head_frame, image=self.logo, bg="white")
        self.dashboard_lbl = Label(logo_head_frame, text="Dashboard", bg="white", font=("Segoe UI", 30, "bold"),
                                   background="white")

        Data.data_table_frame = DataTableFrame(left_frame)

        # canvas = Canvas(image_frame, width=300, height=300, background=color_background, highlightthickness=0)
        # self.img = PhotoImage(file="images/satelite.png").subsample(2, 2)
        # canvas.create_image(150, 150, anchor="center", image=self.img)

        Data.Temp_Card = Card("Temperature", "22.5 C", [20, 21, 20, 21, 22, 23], cards_frame)
        Data.pressure_Card = Card("Pressure", "66 F",         [1.5, 1.2, 1.5, 1.6, 1.5], cards_frame)
        Data.acceleration_Card = Card("Acceleration", "22.5", [330, 323, 323, 353, 300], cards_frame)

        Data.Map = MapCard(30.057236, 31.323368, self)

        #         --------- packing -----------
        logo_head_frame.pack(side="top")
        Data.data_table_frame.pack(side="top")
        left_frame.pack(side="left")
        self.logo_lbl.pack(side="left")
        self.dashboard_lbl.pack(side="left", expand=1)

        # background_lbl.place(x=0, y=0)
        # image_frame.pack(anchor="center", pady=20)
        cards_frame.pack(side="left")
        # canvas.pack()

        Data.Temp_Card.grid(row=0, column=0, padx=10, pady=10)
        Data.pressure_Card.grid(row=1, column=0, padx=10, pady=10)
        Data.acceleration_Card.grid(row=2, column=0, padx=10, pady=10)

        Data.Map.pack(side="right", padx=10, pady=10, fill="y")



