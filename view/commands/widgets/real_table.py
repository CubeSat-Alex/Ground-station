from tkinter import *
from tkinter.ttk import Treeview, Style
from logic.data import Data


class RealtimeTable(Frame):

    def __init__(self, *args):
        Frame.__init__(self, *args, borderwidth=10, highlightbackground="black", highlightthickness=0.2,
                       background="white")

        style = Style()

        style.configure("mystyle.Treeview", font=('Calibri', 11))
        style.configure("mystyle.Treeview.Heading", font=('Calibri', 14,"bold"))
        style.configure("mystyle.Treeview", font=('Calibri', 13))

        Data.realtime_table = Treeview(self, style="mystyle.Treeview", height=600)
        # Data.realtime_table = Treeview(self, height=600)

        Data.realtime_table['columns'] = ('Time', 'Temperature', 'Pressure', 'Acceleration', 'Angle',
                                          'altitude', 'FLDR', 'BLDR', 'RLDR', 'LLDR')

        Data.realtime_table.column("#0", width=0, stretch=NO)
        Data.realtime_table.column("Time", anchor=CENTER, width=150)
        Data.realtime_table.column("Temperature", anchor=CENTER, width=120)
        Data.realtime_table.column("Pressure", anchor=CENTER, width=100)
        Data.realtime_table.column("Acceleration", anchor=CENTER, width=110)
        Data.realtime_table.column("Angle", anchor=CENTER, width=80)
        Data.realtime_table.column("altitude", anchor=CENTER, width=80)
        Data.realtime_table.column("FLDR", anchor=CENTER, width=60)
        Data.realtime_table.column("BLDR", anchor=CENTER, width=60)
        Data.realtime_table.column("RLDR", anchor=CENTER, width=60)
        Data.realtime_table.column("LLDR", anchor=CENTER, width=60)

        Data.realtime_table.heading("#0", text="", anchor=CENTER)
        Data.realtime_table.heading("Time", text="Time", anchor=CENTER)
        Data.realtime_table.heading("Temperature", text="Temperature", anchor=CENTER)
        Data.realtime_table.heading("Pressure", text="Pressure", anchor=CENTER)
        Data.realtime_table.heading("Acceleration", text="Acceleration", anchor=CENTER)
        Data.realtime_table.heading("Angle", text="Angle", anchor=CENTER)
        Data.realtime_table.heading("altitude", text="Altitude", anchor=CENTER)
        Data.realtime_table.heading("FLDR", text="FLDR", anchor=CENTER)
        Data.realtime_table.heading("BLDR", text="BLDR", anchor=CENTER)
        Data.realtime_table.heading("RLDR", text="RLDR", anchor=CENTER)
        Data.realtime_table.heading("LLDR", text="LLDR", anchor=CENTER)

        # Data.realtime_table.insert(parent='', index='end', text='', values=(
        #     datetime.now(), "25", "12", "333.0", "45,60", 1500, "200", "200", "200", "200"
        # ))
        # Data.realtime_table.insert(parent='', index='end', text='', values=(
        #     datetime.now(), "33", "18", "278.0", "45,50", 1500, "44", "200", "200", "200"
        # ))

        Data.realtime_table.pack()
