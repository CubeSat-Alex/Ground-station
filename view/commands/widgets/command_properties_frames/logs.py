import _thread
from tkinter import *
from datetime import datetime
from logic.constant.constants import time_format
from logic.constant.orders import Orders
from logic.data import Data
from logic.functions.server import request, receive_fromOBC


class LogsFrame(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.config(borderwidth=0, highlightbackground="white", highlightthickness=0.2, bg="white", height=100)
        self.controller = controller

        label = Label(self, text="Logs", font=("", 14, "bold"), background="white")
        label.pack(side="top", fill="x")

        content_frame = Frame(self, bg="white")
        content_frame.pack(anchor="center", pady=20, fill="both", expand=1)

        button = Button(self, text="Get Logs", font=("", 14, "bold"), command=self.get_all_logs_button_clicked,
                        relief="flat")
        button.pack(side="bottom", fill="x")

        button = Button(self, text="Delete Logs", font=("", 14, "bold"), command=self.delete_all_logs_button_clicked,
                        relief="flat")
        button.pack(side="bottom", fill="x")

    def get_all_logs_button_clicked(self):
        Data.commands_counter = Data.commands_counter + 1
        Data.command_list_table.insert(parent='', index='end', text='', values=(
            str(Data.commands_counter), "get logs", datetime.now().strftime(time_format),
            Data.mission_entry.get(), ' - '
        ))
        _thread.start_new_thread(self.get_logs_thread, ())

    def get_logs_thread(self):
        request(Orders.getLogs, str(datetime.now().strftime(time_format)))
        receive_fromOBC()
        Data.dataBase.addLogs(Data.data_received)
        self.add_to_table()

    def add_to_table(self):
        jsn = Data.dataBase.getLogs()

        for i in range(jsn.shape[0]):
            orbit_num = jsn["orbit"][i]
            command = jsn["details"][i]
            time = jsn["date"][i]
            status = jsn["state"][i]

            Data.logs_table.insert(parent='', index='end', text='', values=(
                orbit_num, command, time, status
            ))

    def delete_all_logs_button_clicked(self):
        Data.commands_counter = Data.commands_counter + 1
        Data.command_list_table.insert(parent='', index='end', text='', values=(
            str(Data.commands_counter), "delete logs", datetime.now().strftime(time_format),
            Data.mission_entry.get(), ' - '
        ))
        request(Orders.deleteLogs, str(datetime.now().strftime(time_format)))
