import _thread
from tkinter import *
from datetime import datetime
from logic.constant.constants import time_format
from logic.constant.orders import Orders
from logic.data import Data
from logic.functions.server import request, receive_fromOBC, get_telemetry, add_request


class GETTelemetryFrame(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.config(borderwidth=0, highlightbackground="white", highlightthickness=0.2, bg="white", height=100)

        self.controller = controller
        label = Label(self, text="Telemetry", font=("", 14, "bold"), background="white")
        label.pack(side="top", fill="x")

        content_frame = Frame(self, bg="white")
        content_frame.pack(anchor="center", pady=20, fill="both", expand=1)

        button = Button(self, text="Get telemetry", font=("", 14, "bold"), command=self.get_telemetry_button_clicked,
                        relief="flat")
        button.pack(side="bottom", fill="x")

        button = Button(self, text="Delete telemetry", font=("", 14, "bold"), command=self.del_telemetry_button_clicked,
                        relief="flat")
        button.pack(side="bottom", fill="x")

    def get_telemetry_button_clicked(self):
        Data.commands_counter = Data.commands_counter + 1
        Data.command_list_table.insert(parent='', index='end', text='', values=(
            str(Data.commands_counter), "get telemetry", datetime.now().strftime(time_format),
            Data.mission_entry.get(), " - "
        ))
        add_request(Orders.getTelemetry, '')
        # _thread.start_new_thread(get_telemetry, ())

    def del_telemetry_button_clicked(self):
        Data.commands_counter = Data.commands_counter + 1
        Data.command_list_table.insert(parent='', index='end', text='', values=(
            str(Data.commands_counter), "delete telemetry", datetime.now().strftime(time_format),
            Data.mission_entry.get(), " - "
        ))
        add_request(Orders.deleteTelemetry, '0')
