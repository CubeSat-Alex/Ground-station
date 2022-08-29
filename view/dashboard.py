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

        cards_frame = Frame(self, bg="white")
        left_frame = Frame(self, bg="white")

        #         --------- Elements -----------

        Data.data_table_frame = DataTableFrame(left_frame)

        Data.Temp_Card = Card("Temperature", "22.5 C", [1.5, 1.2, 1.5, 1.6, 1.5], cards_frame)
        Data.pressure_Card = Card("Pressure", "66 F",         [1.5, 1.2, 1.5, 1.6, 1.5], cards_frame)
        Data.acceleration_Card = Card("Acceleration", "22.5", [330, 323, 323, 353, 300], cards_frame)
        Data.Map = MapCard(30.057236, 31.323368, self)

        last30 = Data.dataBase.getLast30()

        # change_location(last30["lang"].tolist()[0], last30["lat"].tolist()[0])
        change_acceleration_figure(last30["acceleration"].tolist())
        change_pressure_figure(last30["pressure"].tolist())
        change_temp_figure(last30["tempreture"].tolist())

        #         --------- packing -----------

        Data.data_table_frame.pack(side="top")
        left_frame.pack(side="left")

        cards_frame.pack(side="left")

        Data.Temp_Card.grid(row=0, column=0, padx=10, pady=10)
        Data.pressure_Card.grid(row=1, column=0, padx=10, pady=10)
        Data.acceleration_Card.grid(row=2, column=0, padx=10, pady=10)

        Data.Map.pack(side="right", padx=10, pady=10, fill="y")



