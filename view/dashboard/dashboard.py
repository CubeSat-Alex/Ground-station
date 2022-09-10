from tkinter import *
from logic.functions.figures import *
from logic.functions.general import *
from view.dashboard.widgets.data_table import DataTableFrame
from model.page import Page
from view.dashboard.widgets.card import Card, MapCard
from view.dashboard.widgets.ldr_panel import LDRPanel
from view.dashboard.widgets.satellite_orbit import SatelliteOrbit


class Dashboard(Page):

    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.config(bg="white")

        #            --------- Frames -----------

        cards_frame = Frame(self, bg="white")
        left_frame = Frame(self, bg="white")
        right_frame = Frame(self, bg="white")
        right_top_frame = Frame(right_frame, bg="white")

        #         --------- Elements -----------

        Data.data_table_frame = DataTableFrame(left_frame)

        Data.Temp_Card = Card("Temperature", "22.5 C", [1.5, 1.2, 1.5, 1.6, 1.5], cards_frame)
        Data.pressure_Card = Card("Pressure", "66 F",         [1.5, 1.2, 1.5, 1.6, 1.5], cards_frame)
        Data.acceleration_Card = Card("Acceleration", "22.5", [330, 323, 323, 353, 300], cards_frame)
        Data.ldr_panel = LDRPanel(right_top_frame)
        Data.satellite_orbit = SatelliteOrbit(right_top_frame)
        Data.Map = MapCard(right_frame, lat=30.057236, long=31.323368)

        last30 = Data.dataBase.getLast30()

        change_location(last30["lang"].tolist()[0], last30["lat"].tolist()[0])
        change_acceleration_figure(last30["acceleration"].tolist())
        change_pressure_figure(last30["pressure"].tolist())
        change_temp_figure(last30["tempreture"].tolist())

        #         --------- packing -----------

        Data.data_table_frame.pack(side="top")
        left_frame.pack(side="left")
        right_frame.pack(side="right")
        right_top_frame.pack(side="top")

        cards_frame.pack(side="left")

        Data.Temp_Card.grid(row=0, column=0,)
        Data.pressure_Card.grid(row=1, column=0,)
        Data.acceleration_Card.grid(row=2, column=0,)

        Data.ldr_panel.pack(side="right", padx=10)
        Data.satellite_orbit.pack(side="right", padx=10)
        Data.Map.pack(side="right", padx=10, fill="y")
