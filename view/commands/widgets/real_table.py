from tkinter import *
from tkinter.ttk import Treeview, Style
from logic.data import Data
from datetime import datetime


class RealtimeTable(Frame):

    def __init__(self, *args):
        Frame.__init__(self, *args, borderwidth=10, highlightbackground="black", highlightthickness=0.2,
                       background="white")

        style = Style()
        style.configure("mystyle.Treeview", highlightthickness=3, bd=2, font=('Calibri', 11))
        style.configure("mystyle.Treeview.Heading", font=('Calibri', 14,))
        style.configure("mystyle.Treeview", font=('Calibri', 13))

        Data.realtime_table = Treeview(self, style="mystyle.Treeview", height=600)

        Data.realtime_table['columns'] = ('ID', 'Command',  'Angle', 'Duration', 'Execution', 'name')

        Data.realtime_table['columns'] = ('Time', 'Temperature', 'Pressure', 'Acceleration', 'Angle', 'altitude', 'LDR')

        Data.realtime_table.column("#0", width=0, stretch=NO)
        Data.realtime_table.column("Time", anchor=CENTER, width=130)
        Data.realtime_table.column("Temperature", anchor=CENTER, width=80)
        Data.realtime_table.column("Pressure", anchor=CENTER, width=80)
        Data.realtime_table.column("Acceleration", anchor=CENTER, width=80)
        Data.realtime_table.column("Angle", anchor=CENTER, width=80)
        Data.realtime_table.column("altitude", anchor=CENTER, width=80)
        Data.realtime_table.column("LDR", anchor=CENTER, width=80)

        Data.realtime_table.heading("#0", text="", anchor=CENTER)
        Data.realtime_table.heading("Time", text="Time", anchor=CENTER)
        Data.realtime_table.heading("Temperature", text="Temperature", anchor=CENTER)
        Data.realtime_table.heading("Pressure", text="Pressure", anchor=CENTER)
        Data.realtime_table.heading("Acceleration", text="Acceleration", anchor=CENTER)
        Data.realtime_table.heading("Angle", text="Angle", anchor=CENTER)
        Data.realtime_table.heading("altitude", text="Altitude", anchor=CENTER)
        Data.realtime_table.heading("LDR", text="LDR", anchor=CENTER)

        Data.realtime_table.insert(parent='', index='end', text='', values=(
            datetime.now(), "25", "12", "333.0", "45,60", 1500, "F: 200"
        ))
        Data.realtime_table.insert(parent='', index='end', text='', values=(
            datetime.now(), "33", "18", "278.0", "45,50", 1500, "F: 205"
        ))

        Data.realtime_table.pack()
