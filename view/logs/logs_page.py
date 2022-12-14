from tkinter import *
from tkinter.ttk import Treeview, Style
from logic.data import Data
from datetime import datetime
from model.page import Page


class LogsPage(Page):

    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        self.config(bg="white")

        style = Style()
        style.configure("mystyle.Treeview", highlightthickness=1, bd=1, font=('Calibri', 11))
        style.configure("mystyle.Treeview.Heading", font=('Calibri', 14,))
        style.configure("mystyle.Treeview", font=('Calibri', 13))

        scrollbar = Scrollbar(self)
        scrollbar.pack(side=RIGHT, fill=Y)

        Data.logs_table = Treeview(self, style="mystyle.Treeview", height=3, yscrollcommand=scrollbar.set)

        Data.logs_table['columns'] = ('orbit_number', 'command', 'time', 'status')

        Data.logs_table.column("#0", width=0, stretch=NO)
        Data.logs_table.column("orbit_number", anchor=CENTER, width=200)
        Data.logs_table.column("command", anchor=CENTER, width=200)
        Data.logs_table.column("time", anchor=CENTER, width=200)
        Data.logs_table.column("status", anchor=CENTER, width=200)

        Data.logs_table.heading("#0", text="", anchor=CENTER)
        Data.logs_table.heading("orbit_number", text="orbit number", anchor=CENTER)
        Data.logs_table.heading("command", text="command", anchor=CENTER)
        Data.logs_table.heading("time", text="time", anchor=CENTER)
        Data.logs_table.heading("status", text="status", anchor=CENTER)

        Label(self, font=("", 20), foreground="white", text="txt").pack(side="top", pady=30)
        Data.logs_table.pack(side="bottom", expand=1, fill="both", ipady=20)

        jsn = Data.dataBase.getLogs()

        for i in range(jsn.shape[0]):
            orbit_num = jsn["orbit"][i]
            command = jsn["details"][i]
            time = jsn["date"][i]
            status = jsn["state"][i]

            Data.logs_table.insert(parent='', index='end', text='', values=(
                orbit_num, command, time, status
            ))

        scrollbar.config(command=Data.logs_table.yview)
        #         --------- Frames -----------

        #         --------- Elements -----------

        #         --------- packing -----------
