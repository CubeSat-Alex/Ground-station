from tkinter import *
from datetime import datetime
from logic.data import Data


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
        Data.commands_counter = Data.commands_counter + 1
        Data.command_list_table.insert(parent='', index='end', text='', values=(
            str(Data.commands_counter), "get time difference", datetime.now().strftime("%d_%m_%Y %H-%M-%S"),
            Data.mission_entry.get(), " - "
        ))


class SetOnBoardTimeFrame(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        self.config(borderwidth=0, highlightbackground="white", highlightthickness=0.2, bg="white", height=100)

        self.controller = controller
        label = Label(self, text="Set on board time", font=("", 14, "bold"), background="white")
        label.pack(side="top", fill="x")

        # content_frame = Frame(self, bg="white")
        # content_frame.pack(anchor="center", pady=20, fill="both", expand=1)
        #
        # self.entry_year = Entry(content_frame, bg="white", font=("Segoe UI", 18), foreground="#0ba9bc",
        #                         width=4, fg='black')
        #
        # self.entry_month = Entry(content_frame, bg="white", font=("Segoe UI", 18), foreground="#0ba9bc",
        #                          width=2, fg='black')
        # self.entry_day = Entry(content_frame, bg="white", font=("Segoe UI", 18), foreground="#0ba9bc",
        #                        width=2, fg='black')
        #
        # self.entry_hours = Entry(content_frame, bg="white", font=("Segoe UI", 18), foreground="#0ba9bc",
        #                          width=2, fg='black')
        # self.entry_minutes = Entry(content_frame, bg="white", font=("Segoe UI", 18), foreground="#0ba9bc",
        #                            width=2, fg='black')
        # self.entry_seconds = Entry(content_frame, bg="white", font=("Segoe UI", 18), foreground="#0ba9bc",
        #                            width=2, fg='black')
        #
        # Label(content_frame, text=" Y: ", bg="white", font=("Segoe UI", 14), foreground="#0ba9bc").pack(side="left")
        # self.entry_year.pack(side="left")
        # Label(content_frame, text=" M: ", bg="white", font=("Segoe UI", 14), foreground="#0ba9bc").pack(side="left")
        # self.entry_month.pack(side="left")
        # Label(content_frame, text=" D: ", bg="white", font=("Segoe UI", 14), foreground="#0ba9bc").pack(side="left")
        # self.entry_day.pack(side="left")
        # Label(content_frame, text="      H: ", bg="white", font=("Segoe UI", 14), foreground="#0ba9bc").pack(side="left")
        # self.entry_hours.pack(side="left")
        # Label(content_frame, text=" M: ", bg="white", font=("Segoe UI", 14), foreground="#0ba9bc").pack(side="left")
        # self.entry_minutes.pack(side="left")
        # Label(content_frame, text=" S: ", bg="white", font=("Segoe UI", 14), foreground="#0ba9bc").pack(side="left")
        # self.entry_seconds.pack(side="left")
        #
        # self.entry_year.insert(0, Data.execution_time.year)
        # self.entry_month.insert(0, Data.execution_time.month)
        # self.entry_day.insert(0, Data.execution_time.day)
        # self.entry_hours.insert(0, Data.execution_time.hour)
        # self.entry_minutes.insert(0, Data.execution_time.minute)
        # self.entry_seconds.insert(0, Data.execution_time.second)

        button = Button(self, text="List", font=("", 14, "bold"), command=self.set_time_button_clicked,
                        relief="flat")
        button.pack(side="bottom", fill="x")

    def set_time_button_clicked(self):
        Data.commands_counter = Data.commands_counter + 1
        Data.command_list_table.insert(parent='', index='end', text='', values=(
            str(Data.commands_counter), "set on-board time", datetime.now().strftime("%d_%m_%Y %H-%M-%S"),
            Data.mission_entry.get(), " - "
        ))


class SetSessionTimeFrame(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        self.config(borderwidth=0, highlightbackground="white", highlightthickness=0.2, bg="white", height=100)

        self.controller = controller
        label = Label(self, text="Set on board time", font=("", 14, "bold"), background="white")
        label.pack(side="top", fill="x")

        content_frame = Frame(self, bg="white")
        content_frame.pack(anchor="center", pady=20, fill="both", expand=1)

        content_frame2 = Frame(self, bg="white")
        content_frame2.pack(anchor="center", pady=20, fill="both", expand=1)

        self.entry_year = Entry(content_frame, bg="white", font=("Segoe UI", 18), foreground="#0ba9bc",
                                width=4, fg='black')

        self.entry_month = Entry(content_frame, bg="white", font=("Segoe UI", 18), foreground="#0ba9bc",
                                 width=2, fg='black')
        self.entry_day = Entry(content_frame, bg="white", font=("Segoe UI", 18), foreground="#0ba9bc",
                               width=2, fg='black')

        self.entry_hours = Entry(content_frame, bg="white", font=("Segoe UI", 18), foreground="#0ba9bc",
                                 width=2, fg='black')
        self.entry_minutes = Entry(content_frame, bg="white", font=("Segoe UI", 18), foreground="#0ba9bc",
                                   width=2, fg='black')
        self.entry_seconds = Entry(content_frame, bg="white", font=("Segoe UI", 18), foreground="#0ba9bc",
                                   width=2, fg='black')

        Label(content_frame, text=" Y: ", bg="white", font=("Segoe UI", 14), foreground="#0ba9bc").pack(side="left")
        self.entry_year.pack(side="left")
        Label(content_frame, text=" M: ", bg="white", font=("Segoe UI", 14), foreground="#0ba9bc").pack(side="left")
        self.entry_month.pack(side="left")
        Label(content_frame, text=" D: ", bg="white", font=("Segoe UI", 14), foreground="#0ba9bc").pack(side="left")
        self.entry_day.pack(side="left")
        Label(content_frame, text="      H: ", bg="white", font=("Segoe UI", 14), foreground="#0ba9bc").pack(side="left")
        self.entry_hours.pack(side="left")
        Label(content_frame, text=" M: ", bg="white", font=("Segoe UI", 14), foreground="#0ba9bc").pack(side="left")
        self.entry_minutes.pack(side="left")
        Label(content_frame, text=" S: ", bg="white", font=("Segoe UI", 14), foreground="#0ba9bc").pack(side="left")
        self.entry_seconds.pack(side="left")

        self.entry_year.insert(0, Data.start_session_time.year)
        self.entry_month.insert(0, Data.start_session_time.month)
        self.entry_day.insert(0, Data.start_session_time.day)
        self.entry_hours.insert(0, Data.start_session_time.hour)
        self.entry_minutes.insert(0, Data.start_session_time.minute)
        self.entry_seconds.insert(0, Data.start_session_time.second)

        self.entry_year2 = Entry(content_frame2, bg="white", font=("Segoe UI", 18), foreground="#0ba9bc",
                                width=4, fg='black')

        self.entry_month2 = Entry(content_frame2, bg="white", font=("Segoe UI", 18), foreground="#0ba9bc",
                                 width=2, fg='black')
        self.entry_day2 = Entry(content_frame2, bg="white", font=("Segoe UI", 18), foreground="#0ba9bc",
                               width=2, fg='black')

        self.entry_hours2 = Entry(content_frame2, bg="white", font=("Segoe UI", 18), foreground="#0ba9bc",
                                 width=2, fg='black')
        self.entry_minutes2 = Entry(content_frame2, bg="white", font=("Segoe UI", 18), foreground="#0ba9bc",
                                   width=2, fg='black')
        self.entry_seconds2 = Entry(content_frame2, bg="white", font=("Segoe UI", 18), foreground="#0ba9bc",
                                   width=2, fg='black')

        Label(content_frame2, text=" Y: ", bg="white", font=("Segoe UI", 14), foreground="#0ba9bc").pack(side="left")
        self.entry_year2.pack(side="left")
        Label(content_frame2, text=" M: ", bg="white", font=("Segoe UI", 14), foreground="#0ba9bc").pack(side="left")
        self.entry_month2.pack(side="left")
        Label(content_frame2, text=" D: ", bg="white", font=("Segoe UI", 14), foreground="#0ba9bc").pack(side="left")
        self.entry_day2.pack(side="left")
        Label(content_frame2, text="      H: ", bg="white", font=("Segoe UI", 14), foreground="#0ba9bc").pack(side="left")
        self.entry_hours2.pack(side="left")
        Label(content_frame2, text=" M: ", bg="white", font=("Segoe UI", 14), foreground="#0ba9bc").pack(side="left")
        self.entry_minutes2.pack(side="left")
        Label(content_frame2, text=" S: ", bg="white", font=("Segoe UI", 14), foreground="#0ba9bc").pack(side="left")
        self.entry_seconds2.pack(side="left")

        self.entry_year2.insert(0, Data.end_session_time.year)
        self.entry_month2.insert(0, Data.end_session_time.month)
        self.entry_day2.insert(0, Data.end_session_time.day)
        self.entry_hours2.insert(0, Data.end_session_time.hour)
        self.entry_minutes2.insert(0, Data.end_session_time.minute)
        self.entry_seconds2.insert(0, Data.end_session_time.second)

        button = Button(self, text="List", font=("", 14, "bold"), command=self.set_time_button_clicked,
                        relief="flat")
        button.pack(side="bottom", fill="x")

    def set_time_button_clicked(self):
        Data.commands_counter = Data.commands_counter + 1
        Data.command_list_table.insert(parent='', index='end', text='', values=(
            str(Data.commands_counter), "set session time", datetime.now().strftime("%d_%m_%Y %H-%M-%S"),
            Data.mission_entry.get(), Data.start_session_time
        ))


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

    def on_button_clicked(self):
        Data.commands_counter = Data.commands_counter + 1
        Data.command_list_table.insert(parent='', index='end', text='', values=(
            str(Data.commands_counter), "ADCS", datetime.now().strftime("%d_%m_%Y %H-%M-%S"),
            Data.mission_entry.get(), "ON"
        ))

    def off_button_clicked(self):
        Data.commands_counter = Data.commands_counter + 1
        Data.command_list_table.insert(parent='', index='end', text='', values=(
            str(Data.commands_counter), "ADCS", datetime.now().strftime("%d_%m_%Y %H-%M-%S"),
            Data.mission_entry.get(), "OFF"
        ))

    def reset_button_clicked(self):
        Data.commands_counter = Data.commands_counter + 1
        Data.command_list_table.insert(parent='', index='end', text='', values=(
            str(Data.commands_counter), "ADCS", datetime.now().strftime("%d_%m_%Y %H-%M-%S"),
            Data.mission_entry.get(), "RESET"
        ))

    def check_button_clicked(self):
        Data.commands_counter = Data.commands_counter + 1
        Data.command_list_table.insert(parent='', index='end', text='', values=(
            str(Data.commands_counter), "ADCS", datetime.now().strftime("%d_%m_%Y %H-%M-%S"),
            Data.mission_entry.get(), "Check status"
        ))


class GPSFrame(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.config(borderwidth=0, highlightbackground="white", highlightthickness=0.2, bg="white", height=100)
        self.controller = controller

        label = Label(self, text="GPS Subsystem", font=("", 14, "bold"), background="white")
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
            str(Data.commands_counter), "GPS", datetime.now().strftime("%d_%m_%Y %H-%M-%S"),
            Data.mission_entry.get(), "ON"
        ))

    def off_button_clicked(self):
        Data.commands_counter = Data.commands_counter + 1
        Data.command_list_table.insert(parent='', index='end', text='', values=(
            str(Data.commands_counter), "GPS", datetime.now().strftime("%d_%m_%Y %H-%M-%S"),
            Data.mission_entry.get(), "OFF"
        ))

    def reset_button_clicked(self):
        Data.commands_counter = Data.commands_counter + 1
        Data.command_list_table.insert(parent='', index='end', text='', values=(
            str(Data.commands_counter), "GPS", datetime.now().strftime("%d_%m_%Y %H-%M-%S"),
            Data.mission_entry.get(), "RESET"
        ))

    def check_button_clicked(self):
        Data.commands_counter = Data.commands_counter + 1
        Data.command_list_table.insert(parent='', index='end', text='', values=(
            str(Data.commands_counter), "GPS", datetime.now().strftime("%d_%m_%Y %H-%M-%S"),
            Data.mission_entry.get(), "Check status"
        ))


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
            str(Data.commands_counter), "open real time data", datetime.now().strftime("%d_%m_%Y %H-%M-%S"),
            Data.mission_entry.get(), " - "
        ))

    def close_real_time_button_clicked(self):
        Data.commands_counter = Data.commands_counter + 1
        Data.command_list_table.insert(parent='', index='end', text='', values=(
            str(Data.commands_counter), "close real time data", datetime.now().strftime("%d_%m_%Y %H-%M-%S"),
            Data.mission_entry.get(), " - "
        ))
