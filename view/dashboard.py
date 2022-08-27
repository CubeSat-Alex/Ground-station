from tkinter import *
from logic.functions import *
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
        list = [0.8886339217942552, 0.35463799802475904, 0.19064301191446675, 0.8753111647210065, 0.3459825849600511,
         0.5148329879633158, 0.09603074134407774, 0.2334185652622287, 0.991726555623464, 0.2400938649406048,
         0.8886339217942552, 0.35463799802475904, 0.19064301191446675, 0.8753111647210065, 0.3459825849600511,
         0.5148329879633158, 0.09603074134407774, 0.2334185652622287, 0.991726555623464, 0.2400938649406048,
         0.8886339217942552, 0.35463799802475904, 0.19064301191446675, 0.8753111647210065, 0.3459825849600511,
         0.5148329879633158, 0.09603074134407774, 0.2334185652622287, 0.991726555623464, 0.2400938649406048]

        Data.Temp_Card = Card("Temperature", "22.5 C", list, cards_frame)
        Data.pressure_Card = Card("Pressure", "66 F",         [1.5, 1.2, 1.5, 1.6, 1.5], cards_frame)
        Data.acceleration_Card = Card("Acceleration", "22.5", [330, 323, 323, 353, 300], cards_frame)
        Data.Map = MapCard(30.057236, 31.323368, self)

        last30 = Data.dataBase.getLast30()

        change_location(last30["lang"].tolist()[0], last30["lat"].tolist()[0])
        change_acceleration_figure(last30["acceleration"].tolist())
        change_pressure_figure(last30["pressure"].tolist())
        change_temp_figure(last30["tempreture"].tolist())

        #         --------- packing -----------
        logo_head_frame.pack(side="top")
        Data.data_table_frame.pack(side="top")
        left_frame.pack(side="left")
        self.logo_lbl.pack(side="left")
        self.dashboard_lbl.pack(side="left", expand=1)

        cards_frame.pack(side="left")

        Data.Temp_Card.grid(row=0, column=0, padx=10, pady=10)
        Data.pressure_Card.grid(row=1, column=0, padx=10, pady=10)
        Data.acceleration_Card.grid(row=2, column=0, padx=10, pady=10)

        Data.Map.pack(side="right", padx=10, pady=10, fill="y")



