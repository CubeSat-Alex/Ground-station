import _thread
import json
from tkinter import *
from datetime import datetime
from tkinter.ttk import Progressbar
from logic.constant.constants import time_format
from logic.constant.orders import Orders
from logic.data import Data
from logic.functions.server import request, receive_fromOBC, add_request
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
        add_request(Orders.getTime, "0", str(datetime.now().strftime(time_format)))


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
        add_request(Orders.setOnBoardTime, str(datetime.now().strftime(time_format)))


class SetSessionTimeFrame(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        self.config(borderwidth=0, highlightbackground="white", highlightthickness=0.2, bg="white", height=100)

        self.controller = controller
        label = Label(self, text="Set next session time", font=("", 14, "bold"), background="white")
        label.pack(side="top", fill="x")

        content_frame = Frame(self, bg="white")
        bottom_frame = Frame(self, bg="white")
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

        long_term = Button(bottom_frame, text="          Long Term Plan           ",
                                   font=("", 14, "bold"), command=self.setup_long_term_click, relief="flat")
        bottom_frame.pack(anchor='center', fill="x")
        long_term.pack(side="left", fill="x")

        list_long_term = Button(bottom_frame, text="  list  + ",
                                font=("", 14, "bold"), bg='white', command=self.setup_long_term_click, relief="flat",
                                padx=20)
        list_long_term.pack(side="left")

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

        add_request(Orders.setNextSession, str(datetime.now().strftime(time_format)),
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
        add_request(Orders.controlSubsystem, '0', sys="ADCS", command='angle', x=self.x_entry.get(), y=self.y_entry.get())

    def on_button_clicked(self):
        Data.commands_counter = Data.commands_counter + 1
        Data.command_list_table.insert(parent='', index='end', text='', values=(
            str(Data.commands_counter), "ADCS", datetime.now().strftime(time_format),
            Data.mission_entry.get(), "ON"
        ))
        add_request(Orders.controlSubsystem, str(datetime.now().strftime(time_format)), sys="ADCS", command="ON")

    def off_button_clicked(self):
        Data.commands_counter = Data.commands_counter + 1
        Data.command_list_table.insert(parent='', index='end', text='', values=(
            str(Data.commands_counter), "ADCS", datetime.now().strftime(time_format),
            Data.mission_entry.get(), "OFF"
        ))
        add_request(Orders.controlSubsystem, str(datetime.now().strftime(time_format)), sys="ADCS", command="OFF")


    def reset_button_clicked(self):
        Data.commands_counter = Data.commands_counter + 1
        Data.command_list_table.insert(parent='', index='end', text='', values=(
            str(Data.commands_counter), "ADCS", datetime.now().strftime(time_format),
            Data.mission_entry.get(), "RESET"
        ))
        add_request(Orders.controlSubsystem, str(datetime.now().strftime(time_format)), sys="ADCS", command="RESET")

    def check_button_clicked(self):
        Data.commands_counter = Data.commands_counter + 1
        Data.command_list_table.insert(parent='', index='end', text='', values=(
            str(Data.commands_counter), "ADCS", datetime.now().strftime(time_format),
            Data.mission_entry.get(), "Check status"
        ))
        add_request(Orders.controlSubsystem, str(datetime.now().strftime(time_format)), sys="ADCS", command="LIVE")


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
        add_request(Orders.controlSubsystem, str(datetime.now().strftime(time_format)), sys="TT", command="ON")

    def off_button_clicked(self):
        Data.commands_counter = Data.commands_counter + 1
        Data.command_list_table.insert(parent='', index='end', text='', values=(
            str(Data.commands_counter), "Telemetry", datetime.now().strftime(time_format),
            Data.mission_entry.get(), "OFF"
        ))
        add_request(Orders.controlSubsystem, str(datetime.now().strftime(time_format)), sys="TT", command="OFF")

    def reset_button_clicked(self):
        Data.commands_counter = Data.commands_counter + 1
        Data.command_list_table.insert(parent='', index='end', text='', values=(
            str(Data.commands_counter), "Telemetry", datetime.now().strftime(time_format),
            Data.mission_entry.get(), "RESET"
        ))
        add_request(Orders.controlSubsystem, str(datetime.now().strftime(time_format)), sys="TT", command="RESET")

    def check_button_clicked(self):
        Data.commands_counter = Data.commands_counter + 1
        Data.command_list_table.insert(parent='', index='end', text='', values=(
            str(Data.commands_counter), "Telemetry", datetime.now().strftime(time_format),
            Data.mission_entry.get(), "Check status"
        ))
        add_request(Orders.controlSubsystem, str(datetime.now().strftime(time_format)), sys="TT", command="LIVE")


class OpenRealTimeFrame(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.config(borderwidth=0, highlightbackground="white", highlightthickness=0.2, bg="white", height=100)
        self.controller = controller

        label = Label(self, text="real time", font=("", 14, "bold"), background="white")
        label.pack(side="top", fill="x")

        content_frame = Frame(self, bg="white")
        content_frame.pack(anchor="center", pady=20, fill="both", expand=1)

        duration_lbl = Label(self, text="Time Interval in seconds", font=("", 14, "bold"), relief="flat", bg='white')

        self.duration_entry = Entry(self, font=("", 14, "bold"))

        self.duration_entry.pack(side="bottom", fill="x")
        duration_lbl.pack(side="bottom", fill="x", pady=30)

        button = Button(self, text="Open real time data transfer", font=("", 14, "bold"),
                        command=self.open_real_time_button_clicked,
                        relief="flat")
        button.pack(side="bottom", fill="x")

        button = Button(self, text="close real time data transfer", font=("", 14, "bold"),
                        command=self.close_real_time_button_clicked,
                        relief="flat")
        button.pack(side="bottom", fill="x")

        # self.duration_entry.

    def open_real_time_button_clicked(self):
        Data.commands_counter = Data.commands_counter + 1
        Data.command_list_table.insert(parent='', index='end', text='', values=(
            str(Data.commands_counter), "open real time communication", datetime.now().strftime(time_format),
            Data.mission_entry.get(), " - "
        ))
        # _thread.start_new_thread(self.realtime_communication, ())
        Data.realtime_bool = True
        self.after(500, self.realtime_communication)

    def realtime_communication(self):
        request(Orders.openRealTime, '0')
        try:
            receive_fromOBC()
        except:
            if Data.realtime_bool:
                self.after(int(self.duration_entry.get()) * 1000, self.realtime_communication)
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
            self.after(int(self.duration_entry.get()) * 1000, self.realtime_communication)

    def close_real_time_button_clicked(self):

        Data.commands_counter = Data.commands_counter + 1
        Data.command_list_table.insert(parent='', index='end', text='', values=(
            str(Data.commands_counter), "close real time data", datetime.now().strftime(time_format),
            Data.mission_entry.get(), " - "
        ))
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

        # ---------------------------------

        image_lbl = Label(content_frame, text="Images", font=("Segoe UI Light", 20), background="white")
        image_lbl.grid(row=0, column=0, padx=0)

        Data.image_prog = Progressbar(content_frame, orient='horizontal', mode='determinate', length=120, value=80)
        Data.image_prog.grid(row=0, column=1, padx=5)

        Data.image_lbl_var = Label(content_frame, text="5 GB", font=("", 17, "bold"), background="white",
                              foreground="#000799")
        Data.image_lbl_var.grid(row=0, column=2)

        image_lbl2 = Label(content_frame, text="/ 5 GB", font=("", 14, "bold"), background="white")
        image_lbl2.grid(row=0, column=3)

        # images_details = Label(content_frame, text="M: 30 img , E: 6000 img", font=("", 10), background="white",
        #                       foreground="#000799")
        # images_details.grid(row=0, column=4)

        # ---------------------------------

        videos_lbl = Label(content_frame, text="Videos", font=("Segoe UI Light", 20), background="white")
        videos_lbl.grid(row=1, column=0, padx=0)

        Data.videos_prog = Progressbar(content_frame, orient='horizontal', mode='determinate', length=120, value=1)
        Data.videos_prog.grid(row=1, column=1, padx=5)

        Data.videos_lbl_var = Label(content_frame, text="10 GB ", font=("", 17, "bold"), background="white",
                              foreground="#000799")
        Data.videos_lbl_var.grid(row=1, column=2)

        videos_lbl2 = Label(content_frame, text="/ 10 GB", font=("", 14, "bold"), background="white")
        videos_lbl2.grid(row=1, column=3)

        # videos_details = Label(content_frame, text="M: 3 min , E: 6.3 Hr", font=("", 10), background="white",
        #                        foreground="#000799")
        # videos_details.grid(row=1, column=4)

        # ---------------------------------

        telemetry_lbl = Label(content_frame, text="Telemetry", font=("Segoe UI Light", 20), background="white")
        telemetry_lbl.grid(row=2, column=0, padx=0)

        Data.telemetry_prog = Progressbar(content_frame, orient='horizontal', mode='determinate', length=120, value=1)
        Data.telemetry_prog.grid(row=2, column=1, padx=5)

        Data.telemetry_var = Label(content_frame, text="2 GB", font=("", 17, "bold"), background="white",
                                   foreground="#000799")
        Data.telemetry_var.grid(row=2, column=2)

        telemetry2 = Label(content_frame, text="/ 2 GB", font=("", 14, "bold"), background="white")
        telemetry2.grid(row=2, column=3)

        # telemetry_details = Label(content_frame, text="M: 16 hr , E: 4.3 day", font=("", 10), background="white",
        #                        foreground="#000799")
        # telemetry_details.grid(row=2, column=4)

        # ---------------------------------

        logs_lbl = Label(content_frame, text="Logs", font=("Segoe UI Light", 20), background="white")
        logs_lbl.grid(row=3, column=0, padx=0)

        Data.logs_prog = Progressbar(content_frame, orient='horizontal', mode='determinate', length=120, value=10)
        Data.logs_prog.grid(row=3, column=1, padx=5)

        Data.logs_lbl_var = Label(content_frame, text="3 GB", font=("", 17, "bold"), background="white",
                                  foreground="#000799")
        Data.logs_lbl_var.grid(row=3, column=2)

        logs_lbl2 = Label(content_frame, text="/ 3 GB", font=("", 14, "bold"), background="white")
        logs_lbl2.grid(row=3, column=3)

        # logs_details = Label(content_frame, text="M: 20 hr , E: 5 day", font=("", 10), background="white",
        #                        foreground="#000799")
        # logs_details.grid(row=3, column=4)

        # ---------------------------------

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
        logs_size = str(int(jsn['Logs'])/1000)+' KB' if jsn['Logs'] < 1000000 else str(int(jsn['Logs']) /1000000) + ' MB'
        image_size = str(int(jsn['Images'])/1000)+' KB' if jsn['Images'] < 1000000 else str(int(jsn['Images']) /1000000) +' MB'

        Data.image_lbl_var.config(text=image_size)
        Data.videos_lbl_var.config(text=video_size)
        Data.telemetry_var.config(text=telemetry_size)
        Data.logs_lbl_var.config(text=logs_size)

        Data.image_prog.config(value=int(int(jsn['Images'])/1000000000))
        Data.videos_prog.config(value=int(int(jsn['Videos'])/1000000000))
        Data.telemetry_prog.config(value=int(int(jsn['Telemtry'])/1000000000))
        Data.logs_prog.config(value=int(int(jsn['Logs'])/1000000000))

    def list_button_click(self):
        Data.commands_counter = Data.commands_counter + 1
        Data.command_list_table.insert(parent='', index='end', text='', values=(
            str(Data.commands_counter), "Get Storage", datetime.now().strftime(time_format),
            Data.mission_entry.get(), " - "
        ))
        add_request(Orders.getStorage, str(datetime.now().strftime(time_format)))
        # _thread.start_new_thread(self.storage_thread, ())

    # def storage_thread(self):
    #     add_request(Orders.getStorage, str(datetime.now().strftime(time_format)))
