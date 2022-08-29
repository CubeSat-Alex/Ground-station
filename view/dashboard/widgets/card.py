from tkinter import *
import pandas as pd
from matplotlib.backends.backend_tkagg import *
from tkintermapview import TkinterMapView


class Card(Frame):
    title = "value"
    value = "20"
    graph_data = [50, 50, 60, 60]
    plot = None

    def __init__(self, title, value, graph_data, *args):
        Frame.__init__(self, *args, borderwidth=10, highlightbackground="black", highlightthickness=0.2,
                       background="white")
        self.title = title
        self.value = value

        my_dict = {title: graph_data}
        df = pd.DataFrame(data=my_dict)
        fig = df.plot.line(figsize=(8, 2), title=title, legend="").get_figure()

        self.plot = FigureCanvasTkAgg(fig, self)

        NavigationToolbar2Tk(self.plot, self)

        #         --------- packing -----------
        self.plot.get_tk_widget().pack(side="right")



class MapCard(Frame):
    long = 3220
    lat = 30
    map_widget = None

    def __init__(self, long, lat,  *args):
        Frame.__init__(self, *args, borderwidth=10, highlightbackground="black", highlightthickness=0.2,
                       background="white")
        self.long = long
        self.lat = lat

        self.value_lbl = Label(self, text=str(long)+", "+str(lat), font=("Segoe UI Light", 25), background="white",
                               foreground="#277BC0")

        self.map_widget = TkinterMapView(self, width=600, height=900, corner_radius=10)
        #         --------- packing -----------
        self.map_widget.pack(side="bottom")

        self.map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)
        self.map_widget.set_position(long, lat)
        self.map_widget.set_marker(long, lat, text="Here")
