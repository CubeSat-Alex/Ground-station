from tkinter import *
from datetime import datetime
from logic.constant.constants import time_format
from logic.constant.orders import Orders
from logic.data import Data
from logic.functions.server import add_request


class TakeImageFrame(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.config(borderwidth=0, highlightbackground="white", highlightthickness=0.2, bg="white", height=100)

        self.controller = controller
        label = Label(self, text="Take Image", font=("", 14, "bold"), background="white")
        label.pack(side="top", fill="x")

        content_frame = Frame(self, bg="white")
        content_frame.pack(anchor="center", pady=20, fill="both", expand=1)

        Label(self, text="camera angle", bg="white", font=("Segoe UI", 14), foreground="#0ba9bc").pack(side="top", fill='x')

        angle_frame = Frame(self, bg="white")
        angle_frame.pack(anchor="center", pady=20, fill="both", expand=1)

        self.angleX_entry = Entry(angle_frame, bg="white", font=("Segoe UI", 18), foreground="#0ba9bc",
                                width=4, fg='black')

        self.angleY_entry = Entry(angle_frame, bg="white", font=("Segoe UI", 18), foreground="#0ba9bc",
                                 width=2, fg='black')

        Label(angle_frame, text=" X: ", bg="white", font=("Segoe UI", 14), foreground="#0ba9bc").pack(side="left")
        self.angleX_entry.pack(side="left")
        Label(angle_frame, text=" Y: ", bg="white", font=("Segoe UI", 14), foreground="#0ba9bc").pack(side="left")
        self.angleY_entry.pack(side="left")

        self.angleX_entry.insert(0, "60")
        self.angleY_entry.insert(0, "45")

        time_frame = Frame(self, bg="white")
        time_frame.pack(anchor="center", pady=20, fill="both", expand=1)

        self.entry_year = Entry(time_frame, bg="white", font=("Segoe UI", 18), foreground="#0ba9bc",
                                width=4, fg='black')

        self.entry_month = Entry(time_frame, bg="white", font=("Segoe UI", 18), foreground="#0ba9bc",
                                 width=2, fg='black')
        self.entry_day = Entry(time_frame, bg="white", font=("Segoe UI", 18), foreground="#0ba9bc",
                               width=2, fg='black')

        self.entry_hours = Entry(time_frame, bg="white", font=("Segoe UI", 18), foreground="#0ba9bc",
                                 width=2, fg='black')
        self.entry_minutes = Entry(time_frame, bg="white", font=("Segoe UI", 18), foreground="#0ba9bc",
                                   width=2, fg='black')
        self.entry_seconds = Entry(time_frame, bg="white", font=("Segoe UI", 18), foreground="#0ba9bc",
                                   width=2, fg='black')

        Label(time_frame, text=" Y: ", bg="white", font=("Segoe UI", 14), foreground="#0ba9bc").pack(side="left")
        self.entry_year.pack(side="left")
        Label(time_frame, text=" M: ", bg="white", font=("Segoe UI", 14), foreground="#0ba9bc").pack(side="left")
        self.entry_month.pack(side="left")
        Label(time_frame, text=" D: ", bg="white", font=("Segoe UI", 14), foreground="#0ba9bc").pack(side="left")
        self.entry_day.pack(side="left")
        Label(time_frame, text="            H: ", bg="white", font=("Segoe UI", 14), foreground="#0ba9bc").pack(side="left")
        self.entry_hours.pack(side="left")
        Label(time_frame, text=" M: ", bg="white", font=("Segoe UI", 14), foreground="#0ba9bc").pack(side="left")
        self.entry_minutes.pack(side="left")
        Label(time_frame, text=" S: ", bg="white", font=("Segoe UI", 14), foreground="#0ba9bc").pack(side="left")
        self.entry_seconds.pack(side="left")

        self.entry_year.insert(0, Data.execution_time.year)
        self.entry_month.insert(0, Data.execution_time.month)
        self.entry_day.insert(0, Data.execution_time.day)
        self.entry_hours.insert(0, Data.execution_time.hour)
        self.entry_minutes.insert(0, Data.execution_time.minute)
        self.entry_seconds.insert(0, Data.execution_time.second)

        button = Button(self, text="List", font=("", 14, "bold"), command=self.send_button_clicked,
                        relief="flat")
        button.pack(side="bottom", fill="x")

    def send_button_clicked(self):
        Data.commands_counter = Data.commands_counter + 1
        Data.command_list_table.insert(parent='', index='end', text='', values=(
            str(Data.commands_counter), "take image", datetime.now().strftime(time_format),
            Data.mission_entry.get(), " angle :" + self.angleX_entry.get()+", "+self.angleY_entry.get()
        ))
        year = self.entry_year.get()
        month = self.entry_month.get()
        day = self.entry_day.get()
        hour = self.entry_hours.get()
        minute = self.entry_minutes.get()
        second = self.entry_seconds.get()

        anglex = self.angleX_entry.get()
        angley = self.angleY_entry.get()

        add_request(Orders.takeImageAt, datetime(int(year), int(month), int(day), int(hour), int(minute),
                                             int(second)).strftime(time_format),
                x=anglex, y=angley, name=Data.mission_entry.get())


class TakeVideoFrame(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.config(borderwidth=0, highlightbackground="white", highlightthickness=0.2, bg="white", height=100)

        self.controller = controller

        label = Label(self, text="Take Video", font=("", 14, "bold"), background="white")
        label.pack(side="top", fill="x")

        content_frame = Frame(self, bg="white")
        content_frame.pack(anchor="center", pady=20, fill="both", expand=1)

        angle_frame = Frame(self, bg="white")
        angle_frame.pack(anchor="center", pady=20, fill="both", expand=1)

        duration_frame = Frame(self, bg="white")
        duration_frame.pack(anchor="center", pady=20, fill="both", expand=1)

        self.duration_entry = Entry(duration_frame, bg="white", font=("Segoe UI", 18), foreground="#0ba9bc",
                                  width=4, fg='black')
        Label(duration_frame, text=" Duration :   ", bg="white", font=("Segoe UI", 14), foreground="#0ba9bc").pack(side="left")
        self.duration_entry.pack(side="left")

        self.angleX_entry = Entry(angle_frame, bg="white", font=("Segoe UI", 18), foreground="#0ba9bc",
                                  width=4, fg='black')

        self.angleY_entry = Entry(angle_frame, bg="white", font=("Segoe UI", 18), foreground="#0ba9bc",
                                  width=2, fg='black')

        Label(angle_frame, text=" X: ", bg="white", font=("Segoe UI", 14), foreground="#0ba9bc").pack(side="left")
        self.angleX_entry.pack(side="left")
        Label(angle_frame, text=" Y: ", bg="white", font=("Segoe UI", 14), foreground="#0ba9bc").pack(side="left")
        self.angleY_entry.pack(side="left")

        self.angleX_entry.insert(0, "60")
        self.angleY_entry.insert(0, "45")

        time_frame = Frame(self, bg="white")
        time_frame.pack(anchor="center", pady=20, fill="both", expand=1)

        self.entry_year = Entry(time_frame, bg="white", font=("Segoe UI", 18), foreground="#0ba9bc",
                                width=4, fg='black')

        self.entry_month = Entry(time_frame, bg="white", font=("Segoe UI", 18), foreground="#0ba9bc",
                                 width=2, fg='black')
        self.entry_day = Entry(time_frame, bg="white", font=("Segoe UI", 18), foreground="#0ba9bc",
                               width=2, fg='black')

        self.entry_hours = Entry(time_frame, bg="white", font=("Segoe UI", 18), foreground="#0ba9bc",
                                 width=2, fg='black')
        self.entry_minutes = Entry(time_frame, bg="white", font=("Segoe UI", 18), foreground="#0ba9bc",
                                   width=2, fg='black')
        self.entry_seconds = Entry(time_frame, bg="white", font=("Segoe UI", 18), foreground="#0ba9bc",
                                   width=2, fg='black')

        Label(time_frame, text=" Y: ", bg="white", font=("Segoe UI", 14), foreground="#0ba9bc").pack(side="left")
        self.entry_year.pack(side="left")
        Label(time_frame, text=" M: ", bg="white", font=("Segoe UI", 14), foreground="#0ba9bc").pack(side="left")
        self.entry_month.pack(side="left")
        Label(time_frame, text=" D: ", bg="white", font=("Segoe UI", 14), foreground="#0ba9bc").pack(side="left")
        self.entry_day.pack(side="left")
        Label(time_frame, text="            H: ", bg="white", font=("Segoe UI", 14), foreground="#0ba9bc").pack(
            side="left")
        self.entry_hours.pack(side="left")
        Label(time_frame, text=" M: ", bg="white", font=("Segoe UI", 14), foreground="#0ba9bc").pack(side="left")
        self.entry_minutes.pack(side="left")
        Label(time_frame, text=" S: ", bg="white", font=("Segoe UI", 14), foreground="#0ba9bc").pack(side="left")
        self.entry_seconds.pack(side="left")

        self.entry_year.insert(0, Data.execution_time.year)
        self.entry_month.insert(0, Data.execution_time.month)
        self.entry_day.insert(0, Data.execution_time.day)
        self.entry_hours.insert(0, Data.execution_time.hour)
        self.entry_minutes.insert(0, Data.execution_time.minute)
        self.entry_seconds.insert(0, Data.execution_time.second)

        button = Button(self, text="List", font=("", 14, "bold"), command=self.send_button_clicked,
                        relief="flat")
        button.pack(side="bottom", fill="x")

    def send_button_clicked(self):
        Data.commands_counter = Data.commands_counter + 1
        Data.command_list_table.insert(parent='', index='end', text='', values=(
            str(Data.commands_counter), "take video", datetime.now().strftime("%d_%m_%Y %H-%M-%S"),
            Data.mission_entry.get(), " angle :" + self.angleX_entry.get()+", "+self.angleY_entry.get()
            + "  Duration :" + self.duration_entry.get()
        ))

        year = self.entry_year.get()
        month = self.entry_month.get()
        day = self.entry_day.get()
        hour = self.entry_hours.get()
        minute = self.entry_minutes.get()
        second = self.entry_seconds.get()

        anglex = self.angleX_entry.get()
        angley = self.angleY_entry.get()

        duration = self.duration_entry.get()

        add_request(Orders.takeVideoAt, datetime(int(year), int(month), int(day), int(hour), int(minute),
                                             int(second)).strftime(time_format),
                x=anglex, y=angley, duration=duration, name=Data.mission_entry.get())
