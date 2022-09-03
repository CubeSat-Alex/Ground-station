import pandas as pd
from logic.data import Data


def change_temp_figure(data):
    my_dict = {"Temperature": data}
    df = pd.DataFrame(data=my_dict)
    fig1 = df.plot.line(figsize=(8, 2), title="Temperature", legend="").get_figure()
    Data.Temp_Card.plot.figure = fig1
    Data.Temp_Card.plot.draw()


def change_pressure_figure(data):
    my_dict = {"Pressure": data}
    df = pd.DataFrame(data=my_dict)
    fig2 = df.plot.line(figsize=(8, 2), title="Pressure", legend="").get_figure()
    Data.pressure_Card.plot.figure = fig2
    Data.pressure_Card.plot.draw()


def change_acceleration_figure(data):
    my_dict = {"Acceleration": data}
    df = pd.DataFrame(data=my_dict)
    fig3 = df.plot.line(figsize=(8, 2), title="Acceleration", legend="").get_figure()
    Data.acceleration_Card.plot.figure = fig3
    Data.acceleration_Card.plot.draw()


def change_location(long, lat):
    Data.Map.map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga",
                                        max_zoom=22)
    Data.Map.map_widget.set_position(long, lat)
    Data.Map.map_widget.set_marker(long, lat, text="Here")
