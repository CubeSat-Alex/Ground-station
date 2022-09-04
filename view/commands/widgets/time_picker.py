from datetime import datetime
from tkinter import *
from tkcalendar import *
from logic.constant.constants import time_format
from logic.data import Data


class Picker(Frame):

    def __init__(self, date, type, *args):
        Frame.__init__(self, *args, borderwidth=10, highlightbackground="black", highlightthickness=0.2,
                       background="white")

        self.ws = None
        self.hour_string = StringVar(value=date.hour)
        self.min_string = StringVar(value=date.minute)
        self.sec_string = StringVar(value=date.second)

        self.actionBtn = None
        self.sec_hour = None
        self.min_sb = None
        self.sec = None
        self.cal = None
        self.date = date
        self.type = type

        self.f = ('Times', 20)

    def display_msg(self):
        date = self.cal.get_date()
        h = self.min_sb.get()
        m = self.sec_hour.get()
        s = self.sec.get()

        if self.type == "start_session_time":
            print(date)
            Data.start_session_time = datetime(2022, int(str(date).split('/')[0]),
                                               int(str(date).split('/')[1]),
                                               int(h), int(m), int(s))
            Data.start_button.config(text=str(Data.start_session_time.strftime(time_format)))
            print(Data.start_session_time)

        elif self.type == "end_session_time":
            Data.end_session_time = datetime(2022, int(str(date).split('/')[0]),
                                             int(str(date).split('/')[1]),
                                             int(h), int(m), int(s))
            Data.end_button.config(text=str(Data.end_session_time.strftime(time_format)))

        elif self.type == 'long_term_start':
            Data.long_start_session_time = datetime(2022, int(str(date).split('/')[0]),
                                             int(str(date).split('/')[1]),
                                             int(h), int(m), int(s))
            Data.long_start_button.config(text=str(Data.long_start_session_time.strftime(time_format)))

        elif self.type == 'long_term_end':
            Data.long_end_session_time = datetime(2022, int(str(date).split('/')[0]),
                                             int(str(date).split('/')[1]),
                                             int(h), int(m), int(s))
            Data.long_end_button.config(text=str(Data.long_end_session_time.strftime(time_format)))

        self.ws.destroy()

    def show(self):

        self.ws = Tk()
        self.ws.title("Picker")
        self.ws.geometry("500x400")
        self.ws.config(bg="#eeeeee")

        fone = Frame(self.ws)
        ftwo = Frame(self.ws)

        fone.pack(pady=10)
        ftwo.pack(pady=10)

        self.cal = Calendar(
            fone,
            selectmode="day",
            year=self.date.year,
            month=self.date.month,
            day=self.date.day
        )
        self.cal.pack()

        self.min_sb = Spinbox(
            ftwo,
            from_=0,
            to=23,
            wrap=True,
            textvariable=self.hour_string,
            width=3,
            font=self.f,
            justify=CENTER
        )

        self.sec_hour = Spinbox(
            ftwo,
            from_=0,
            to=59,
            wrap=True,
            textvariable=self.min_string,
            font=self.f,
            width=3,
            justify=CENTER
        )

        self.sec = Spinbox(
            ftwo,
            from_=0,
            to=59,
            wrap=True,
            textvariable=self.sec_string,
            width=3,
            font=self.f,
            justify=CENTER
        )

        self.min_sb.pack(side=LEFT, fill=X, expand=True)
        self.sec_hour.pack(side=LEFT, fill=X, expand=True)
        self.sec.pack(side=LEFT, fill=X, expand=True)

        msg = Label(
            self.ws,
            text="Hour  Minute  Seconds",
            font=("Times", 12),
            bg="#eeeeee"
        )
        msg.pack(side=TOP)

        self.actionBtn = Button(
            self.ws,
            text="Select",
            padx=10,
            pady=10,
            relief='flat',
            bg="#54FA9B",
            font=('Times', 20, 'bold'),
            command=self.display_msg
        )
        self.actionBtn.pack(pady=10)

        self.ws.mainloop()
