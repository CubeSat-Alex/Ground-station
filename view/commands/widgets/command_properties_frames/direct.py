import _thread
import json
from tkinter import *
from datetime import datetime
from tkinter import messagebox
from logic.constant.constants import time_format
from logic.constant.orders import Orders
from logic.data import Data
from logic.functions.server import request, receive_fromOBC
from logic.shared_prefrence import cache
from view.commands.widgets.long_term_plan_window import LongTermFrame
from view.commands.widgets.time_picker import Picker


class GetTimeDifferenceFrame(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.config(borderwidth=0, highlightbackground="white", highlightthickness=0.2, bg="white", height=100)

        self.controller = controller
        label = Label(self, text="Get time difference", font=("", 14, "bold"), background="white")
        label.pack(side="top", fill="x")

        content_frame = Frame(self, bg="white")
        content_frame.pack(anchor="center", pady=20, fill="both", expand=1)

        # text1 = Label(content_frame, text="time now : ", font=("", 12), background="white")
        # text1.pack(anchor="w")
        # text2 = Label(content_frame, text=datetime.now().strftime("%H:%M:%S"), font=("", 12), background="white")
        # text2.pack(anchor="w")

        button = Button(self, text="List", font=("", 14, "bold"), command=self.get_time_difference_button_clicked,
                        relief="flat")
        button.pack(side="bottom", fill="x")

    def get_time_difference_button_clicked(self):
        _thread.start_new_thread(self.get_time_difference_thread, ())

    def get_time_difference_thread(self):
        Data.commands_counter = Data.commands_counter + 1
        Data.command_list_table.insert(parent='', index='end', text='', values=(
            str(Data.commands_counter), "get time difference", datetime.now().strftime(time_format),
            Data.mission_entry.get(), " - "
        ))

        request(Orders.getTime, "0", str(datetime.now().strftime(time_format)))
        receive_fromOBC()
        print(Data.data_received)

        obcDate = datetime.strptime(Data.data_received[1:-1], time_format)

        print(obcDate)
        difference = datetime.now() - obcDate
        print(difference.total_seconds())
        messagebox.showinfo("time difference", 'time difference is \n' + str(difference.total_seconds()) + " S")


class SetOnBoardTimeFrame(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        self.config(borderwidth=0, highlightbackground="white", highlightthickness=0.2, bg="white", height=100)

        self.controller = controller
        label = Label(self, text="Set on board time", font=("", 14, "bold"), background="white")
        label.pack(side="top", fill="x")

        button = Button(self, text="List", font=("", 14, "bold"), command=self.set_time_button_clicked,
                        relief="flat")
        button.pack(side="bottom", fill="x")

    def set_time_button_clicked(self):
        Data.commands_counter = Data.commands_counter + 1
        Data.command_list_table.insert(parent='', index='end', text='', values=(
            str(Data.commands_counter), "set on-board time", datetime.now().strftime(time_format),
            Data.mission_entry.get(), " - "
        ))
        request(Orders.setOnBoardTime, str(datetime.now().strftime(time_format)))


class SetSessionTimeFrame(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        self.config(borderwidth=0, highlightbackground="white", highlightthickness=0.2, bg="white", height=100)

        self.controller = controller
        label = Label(self, text="Set next session time", font=("", 14, "bold"), background="white")
        label.pack(side="top", fill="x")

        content_frame = Frame(self, bg="white")
        content_frame.pack(anchor="center", pady=20, fill="both", expand=1)

        Label(content_frame, text="Start Session Time", bg="white", font=("Segoe UI", 14)).pack(
            side="top")

        Data.start_button = Button(content_frame, text=str(Data.start_session_time.strftime(time_format)),
                              font=("", 14, "bold"), command=self.start_button_clicked, relief="flat")
        Data.start_button.pack(side="top", fill="x")

        Label(content_frame, text="End Session Time", bg="white", font=("Segoe UI", 14)).pack(
            side="top")

        Data.end_button = Button(content_frame, text=str(Data.end_session_time.strftime(time_format)),
                            font=("", 14, "bold"), command=self.end_button_clicked, relief="flat")
        Data.end_button.pack(side="top", fill="x")

        long_term = Button(self, text="Long Term Plan",
                                   font=("", 14, "bold"), command=self.setup_long_term_click, relief="flat")
        long_term.pack(side="bottom", fill="x")

        button = Button(content_frame, text="List", font=("", 14, "bold"), command=self.set_time_button_clicked,
                        relief="flat")
        button.pack(side="top", fill="x", pady=20)

    def setup_long_term_click(self):
        long_term_frame = LongTermFrame()
        long_term_frame.show()

    def start_button_clicked(self):
        picker = Picker(datetime.now(), "start_session_time")
        picker.show()

    def end_button_clicked(self):
        picker = Picker(datetime.now(), 'end_session_time')
        picker.show()

    def set_time_button_clicked(self):
        Data.commands_counter = Data.commands_counter + 1
        Data.command_list_table.insert(parent='', index='end', text='', values=(
            str(Data.commands_counter), "set session time", datetime.now().strftime(time_format),
            Data.mission_entry.get(), Data.start_session_time
        ))
        # if datetime.now().strftime("%d-%m-%Y") == Data.start_session_time.strftime("%d-%m-%Y"):
        #     Data.start_session_time = Data.start_session_time
        #     Data.end_session_time = Data.end_session_time

        request(Orders.setNextSession, str(datetime.now().strftime(time_format)),
                start=Data.start_session_time.strftime(time_format),
                end=Data.end_session_time.strftime(time_format))


class ADCSFrame(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.config(borderwidth=0, highlightbackground="white", highlightthickness=0.2, bg="white", height=100)
        self.controller = controller

        label = Label(self, text="ADCS Subsystem", font=("", 14, "bold"), background="white")
        label.pack(side="top", fill="x")

        content_frame = Frame(self, bg="white")
        content_frame.pack(anchor="center", pady=20, fill="both", expand=1)

        button = Button(self, text="Check status", font=("", 14, "bold"), command=self.check_button_clicked,
                        relief="flat")
        button.pack(side="bottom", fill="x")
        button = Button(self, text="Reset", font=("", 14, "bold"), command=self.reset_button_clicked, relief="flat")
        button.pack(side="bottom", fill="x")
        button = Button(self, text="Off", font=("", 14, "bold"), command=self.off_button_clicked, relief="flat")
        button.pack(side="bottom", fill="x")
        button = Button(self, text="On", font=("", 14, "bold"), command=self.on_button_clicked, relief="flat")
        button.pack(side="bottom", fill="x")

        self.x_entry = Entry(self,  font=("", 14, "bold"))
        self.x_entry.pack(side="bottom", fill="x")
        self.y_entry = Entry(self, font=("", 14, "bold"))
        self.y_entry.pack(side="bottom", fill="x")
        button = Button(self, text="To angle", font=("", 14, "bold"), command=self.to_angle_clicked, relief="flat")
        button.pack(side="bottom", fill="x")

    def to_angle_clicked(self):
        Data.commands_counter = Data.commands_counter + 1
        Data.command_list_table.insert(parent='', index='end', text='', values=(
            str(Data.commands_counter), "ADCS", datetime.now().strftime("%d_%m_%Y %H-%M-%S"),
            Data.mission_entry.get(), "to angle"
        ))
        request(Orders.controlSubsystem, '0', sys="ADCS", command='angle', x=self.x_entry.get(), y=self.y_entry.get())

    def on_button_clicked(self):
        Data.commands_counter = Data.commands_counter + 1
        Data.command_list_table.insert(parent='', index='end', text='', values=(
            str(Data.commands_counter), "ADCS", datetime.now().strftime(time_format),
            Data.mission_entry.get(), "ON"
        ))
        request(Orders.controlSubsystem, str(datetime.now().strftime(time_format)), sys="ADCS", command="ON")

    def off_button_clicked(self):
        Data.commands_counter = Data.commands_counter + 1
        Data.command_list_table.insert(parent='', index='end', text='', values=(
            str(Data.commands_counter), "ADCS", datetime.now().strftime(time_format),
            Data.mission_entry.get(), "OFF"
        ))
        request(Orders.controlSubsystem, str(datetime.now().strftime(time_format)), sys="ADCS", command="OFF")


    def reset_button_clicked(self):
        Data.commands_counter = Data.commands_counter + 1
        Data.command_list_table.insert(parent='', index='end', text='', values=(
            str(Data.commands_counter), "ADCS", datetime.now().strftime(time_format),
            Data.mission_entry.get(), "RESET"
        ))
        request(Orders.controlSubsystem, str(datetime.now().strftime(time_format)), sys="ADCS", command="RESET")

    def check_button_clicked(self):
        Data.commands_counter = Data.commands_counter + 1
        Data.command_list_table.insert(parent='', index='end', text='', values=(
            str(Data.commands_counter), "ADCS", datetime.now().strftime(time_format),
            Data.mission_entry.get(), "Check status"
        ))
        request(Orders.controlSubsystem, str(datetime.now().strftime(time_format)), sys="ADCS", command="LIVE")


class GPSFrame(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.config(borderwidth=0, highlightbackground="white", highlightthickness=0.2, bg="white", height=100)
        self.controller = controller

        label = Label(self, text="Telemetry Subsystem", font=("", 14, "bold"), background="white")
        label.pack(side="top", fill="x")

        content_frame = Frame(self, bg="white")
        content_frame.pack(anchor="center", pady=20, fill="both", expand=1)

        button = Button(self, text="Check status", font=("", 14, "bold"), command=self.check_button_clicked,
                        relief="flat")
        button.pack(side="bottom", fill="x")
        button = Button(self, text="Reset", font=("", 14, "bold"), command=self.reset_button_clicked, relief="flat")
        button.pack(side="bottom", fill="x")
        button = Button(self, text="Off", font=("", 14, "bold"), command=self.off_button_clicked, relief="flat")
        button.pack(side="bottom", fill="x")
        button = Button(self, text="On", font=("", 14, "bold"), command=self.on_button_clicked, relief="flat")
        button.pack(side="bottom", fill="x")

    def on_button_clicked(self):
        Data.commands_counter = Data.commands_counter + 1
        Data.command_list_table.insert(parent='', index='end', text='', values=(
            str(Data.commands_counter), "Telemetry", datetime.now().strftime(time_format),
            Data.mission_entry.get(), "ON"
        ))
        request(Orders.controlSubsystem, str(datetime.now().strftime(time_format)), sys="TT", command="ON")

    def off_button_clicked(self):
        Data.commands_counter = Data.commands_counter + 1
        Data.command_list_table.insert(parent='', index='end', text='', values=(
            str(Data.commands_counter), "Telemetry", datetime.now().strftime(time_format),
            Data.mission_entry.get(), "OFF"
        ))
        request(Orders.controlSubsystem, str(datetime.now().strftime(time_format)), sys="TT", command="OFF")

    def reset_button_clicked(self):
        Data.commands_counter = Data.commands_counter + 1
        Data.command_list_table.insert(parent='', index='end', text='', values=(
            str(Data.commands_counter), "Telemetry", datetime.now().strftime(time_format),
            Data.mission_entry.get(), "RESET"
        ))
        request(Orders.controlSubsystem, str(datetime.now().strftime(time_format)), sys="TT", command="RESET")

    def check_button_clicked(self):
        Data.commands_counter = Data.commands_counter + 1
        Data.command_list_table.insert(parent='', index='end', text='', values=(
            str(Data.commands_counter), "Telemetry", datetime.now().strftime(time_format),
            Data.mission_entry.get(), "Check status"
        ))
        request(Orders.controlSubsystem, str(datetime.now().strftime(time_format)), sys="TT", command="LIVE")


class OpenRealTimeFrame(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.config(borderwidth=0, highlightbackground="white", highlightthickness=0.2, bg="white", height=100)
        self.controller = controller

        label = Label(self, text="real time", font=("", 14, "bold"), background="white")
        label.pack(side="top", fill="x")

        content_frame = Frame(self, bg="white")
        content_frame.pack(anchor="center", pady=20, fill="both", expand=1)

        button = Button(self, text="Open real time data transfer", font=("", 14, "bold"),
                        command=self.open_real_time_button_clicked,
                        relief="flat")
        button.pack(side="bottom", fill="x")

        button = Button(self, text="close real time data transfer", font=("", 14, "bold"),
                        command=self.close_real_time_button_clicked,
                        relief="flat")
        button.pack(side="bottom", fill="x")

    def open_real_time_button_clicked(self):
        Data.commands_counter = Data.commands_counter + 1
        Data.command_list_table.insert(parent='', index='end', text='', values=(
            str(Data.commands_counter), "open real time communication", datetime.now().strftime(time_format),
            Data.mission_entry.get(), " - "
        ))
        # _thread.start_new_thread(self.realtime_communication, ())
        Data.realtime_bool = True
        self.after(3000, self.realtime_communication)

    def realtime_communication(self):

        request(Orders.openRealTime, '0')
        try:
            receive_fromOBC()
        except:
            if Data.realtime_bool:
                self.after(3000, self.realtime_communication)
            return
        st = json.loads(str(Data.data_received).strip())

        temp = str(st['TT']['T'])
        pressure = str(st['TT']['P'])
        acceleration = str(st['ADCS']['A'])
        angle = str(st['TT']['X']) + ', ' + str(st['TT']['Y'])
        altitude = str(st['TT']['A'])

        ldr1 = str(st['TT']['LDR1'])
        ldr2 = str(st['TT']['LDR2'])
        ldr3 = str(st['TT']['LDR3'])
        ldr4 = str(st['TT']['LDR4'])

        Data.realtime_table.insert(parent='', index='end', text='', values=(
            datetime.now().strftime(time_format), temp, pressure, acceleration, angle, altitude, ldr1, ldr2, ldr3, ldr4
        ))

        if Data.realtime_bool:
            self.after(3000, self.realtime_communication)

    def close_real_time_button_clicked(self):

        Data.commands_counter = Data.commands_counter + 1
        Data.command_list_table.insert(parent='', index='end', text='', values=(
            str(Data.commands_counter), "close real time data", datetime.now().strftime("%d_%m_%Y %H-%M-%S"),
            Data.mission_entry.get(), " - "
        ))
        print('converted to false')
        Data.realtime_bool = False


class StorageFrame(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.config(borderwidth=0, highlightbackground="white", highlightthickness=0.2, bg="white", height=100)
        self.controller = controller

        label = Label(self, text="get storage analysis", font=("", 14, "bold"), background="white")
        label.pack(side="top", fill="x")

        content_frame = Frame(self, bg="white")
        content_frame.pack(anchor="center", pady=20, fill="both", expand=1, padx=20)

        image_lbl = Label(content_frame, text="Images", font=("Segoe UI Light", 20), background="white")
        image_lbl.grid(row=0, column=0, padx=120)

        Data.image_lbl_var = Label(content_frame, text="5 MB", font=("", 17, "bold"), background="white",
                              foreground="#000799")
        Data.image_lbl_var.grid(row=0, column=1)

        image_lbl2 = Label(content_frame, text="/ 5 GB", font=("", 14, "bold"), background="white")
        image_lbl2.grid(row=0, column=2)

        # ---------------------------------

        videos_lbl = Label(content_frame, text="Videos", font=("Segoe UI Light", 20), background="white")
        videos_lbl.grid(row=1, column=0, padx=120)

        Data.videos_lbl_var = Label(content_frame, text="5 MB ", font=("", 17, "bold"), background="white",
                              foreground="#000799")
        Data.videos_lbl_var.grid(row=1, column=1)

        videos_lbl2 = Label(content_frame, text="/ 5 GB", font=("", 14, "bold"), background="white")
        videos_lbl2.grid(row=1, column=2)

        # ---------------------------------

        telemetry_lbl = Label(content_frame, text="Telemetry", font=("Segoe UI Light", 20), background="white")
        telemetry_lbl.grid(row=2, column=0, padx=120)

        Data.telemetry_var = Label(content_frame, text="5 MB", font=("", 17, "bold"), background="white",
                              foreground="#000799")
        Data.telemetry_var.grid(row=2, column=1)

        telemetry2 = Label(content_frame, text="/ 5 GB", font=("", 14, "bold"), background="white")
        telemetry2.grid(row=2, column=2)

        # ---------------------------------

        logs_lbl = Label(content_frame, text="Logs", font=("Segoe UI Light", 20), background="white")
        logs_lbl.grid(row=3, column=0, padx=120)

        Data.logs_lbl_var = Label(content_frame, text="5 MB", font=("", 17, "bold"), background="white",
                              foreground="#000799")
        Data.logs_lbl_var.grid(row=3, column=1)

        logs_lbl2 = Label(content_frame, text="/ 5 GB", font=("", 14, "bold"), background="white")
        logs_lbl2.grid(row=3, column=2)

        button = Button(self, text="List", font=("", 14, "bold"), command=self.list_button_click,
                        relief="flat")
        button.pack(side="bottom", fill="x")

        jsn = {
            "Images": Data.cache.get('Images'),
            'Videos': Data.cache.get('Videos'),
            'Telemtry': Data.cache.get('Telemtry'),
            'Logs': Data.cache.get('Logs')
        }

        video_size = str(int(jsn['Videos'])/1000)+' KB' if jsn['Videos'] < 1000000 else str(int(jsn['Videos']) /1000000) +' MB'
        telemetry_size = str(int(jsn['Telemtry'])/1000)+' KB' if jsn['Telemtry'] < 1000000 else str(int(jsn['Telemtry']) /1000000) +' MB'
        logs_size = str(int(jsn['Logs'])/1000)+' KB' if jsn['Logs'] < 1000000 else str(int(jsn['Logs']) /1000000) +' MB'
        image_size = str(int(jsn['Images'])/1000)+' KB' if jsn['Images'] < 1000000 else str(int(jsn['Images']) /1000000) +' MB'

        Data.image_lbl_var.config(text=image_size)
        Data.videos_lbl_var.config(text=video_size)
        Data.telemetry_var.config(text=telemetry_size)
        Data.logs_lbl_var.config(text=logs_size)

    def list_button_click(self):
        Data.commands_counter = Data.commands_counter + 1
        Data.command_list_table.insert(parent='', index='end', text='', values=(
            str(Data.commands_counter), "Get Storage", datetime.now().strftime(time_format),
            Data.mission_entry.get(), " - "
        ))
        _thread.start_new_thread(self.storage_thread, ())

    def storage_thread(self):
        request(Orders.getStorage, str(datetime.now().strftime(time_format)))
        receive_fromOBC()
        jsn = json.loads(Data.data_received)

        image_size = str(int(jsn['Images'])/1000)+' KB' if jsn['Images'] < 1000000 else str(int(jsn['Images']) /1000000) +' MB'
        video_size = str(int(jsn['Videos'])/1000)+' KB' if jsn['Videos'] < 1000000 else str(int(jsn['Videos']) /1000000) +' MB'
        telemetry_size = str(int(jsn['Telemtry'])/1000)+' KB' if jsn['Telemtry'] < 1000000 else str(int(jsn['Telemtry']) /1000000) +' MB'
        logs_size = str(int(jsn['Logs'])/1000)+' KB' if jsn['Logs'] < 1000000 else str(int(jsn['Logs']) /1000000) +' MB'

        Data.image_lbl_var.config(text=image_size)
        Data.videos_lbl_var.config(text=video_size)
        Data.telemetry_var.config(text=telemetry_size)
        Data.logs_lbl_var.config(text=logs_size)

        for key, value in jsn.items():
            Data.cache.add(key, value)
