import datetime
from tkinter import *
from logic.functions import *


class SessionPeriodFrame(Frame):

    def __init__(self, *args):
        Frame.__init__(self, *args, borderwidth=10, highlightbackground="black", highlightthickness=0.2,
                       background="white")

        self.top = None
        self.time_picker = None
        header_frame = Frame(self, bg="white")
        bottom_frame = Frame(self, bg="white")
        button_frame = Frame(self, bg="white")
        from_frame = Frame(bottom_frame, bg="white")
        entry_from_frame = Frame(from_frame, bg="white")
        to_frame = Frame(bottom_frame, bg="white")
        entry_to_frame = Frame(to_frame, bg="white")

        #         --------- elements -----------

        header_lbl = Label(header_frame, text="Session Duration", bg="white", font=("Segoe UI", 14, "bold"))
        from_lbl = Label(from_frame, text="From", bg="white", font=("Segoe UI", 18))
        to_lbl = Label(to_frame, text="To", bg="white", font=("Segoe UI", 18))

        self.entry_from_hours = Entry(entry_from_frame, bg="white", font=("Segoe UI", 18), foreground="#0ba9bc",
                                      width=2)

        self.entry_from_minutes = Entry(entry_from_frame, bg="white", font=("Segoe UI", 18), foreground="#0ba9bc",
                                        width=2)
        self.entry_from_seconds = Entry(entry_from_frame, bg="white", font=("Segoe UI", 18), foreground="#0ba9bc",
                                        width=2)

        self.entry_to_hours = Entry(entry_to_frame, bg="white", font=("Segoe UI", 18), foreground="#0ba9bc",
                                    width=2)
        self.entry_to_minutes = Entry(entry_to_frame, bg="white", font=("Segoe UI", 18), foreground="#0ba9bc",
                                      width=2)
        self.entry_to_seconds = Entry(entry_to_frame, bg="white", font=("Segoe UI", 18), foreground="#0ba9bc",
                                      width=2)

        self.change_session_button = Button(button_frame, text="Apply", command=self.apply_button_clicked,
                                            relief="flat",
                                            bg="white", activebackground="white", font=("Segoe UI", 18),
                                            foreground="#0ba9bc")

        #         --------- packing -----------

        header_frame.pack(side="top")
        bottom_frame.pack(side="top")
        from_frame.pack(side="top")
        to_frame.pack(side="top")
        button_frame.pack(side="top")

        header_lbl.pack(anchor="center", expand=1)
        from_lbl.pack(side="top")
        to_lbl.pack(side="top")

        self.entry_from_hours.pack(side="left", padx=5)
        Label(entry_from_frame, text=":", bg="white", font=("Segoe UI", 18), foreground="#0ba9bc").pack(side="left")
        self.entry_from_minutes.pack(side="left", padx=5)
        Label(entry_from_frame, text=":", bg="white", font=("Segoe UI", 18), foreground="#0ba9bc").pack(side="left")
        self.entry_from_seconds.pack(side="left", padx=5)

        self.entry_to_hours.pack(side="left", padx=5)
        Label(entry_to_frame, text=":", bg="white", font=("Segoe UI", 18), foreground="#0ba9bc").pack(side="left")
        self.entry_to_minutes.pack(side="left", padx=5)
        Label(entry_to_frame, text=":", bg="white", font=("Segoe UI", 18), foreground="#0ba9bc").pack(side="left")
        self.entry_to_seconds.pack(side="left", padx=5)

        self.change_session_button.pack(side="top", padx=5)

        entry_from_frame.pack(side="top")
        entry_to_frame.pack(side="top")

        self.entry_from_hours.insert(0, Data.start_session_time.hour)
        self.entry_from_minutes.insert(0, Data.start_session_time.minute)
        self.entry_from_seconds.insert(0, Data.start_session_time.second)
        self.entry_to_hours.insert(0, Data.end_session_time.hour)
        self.entry_to_minutes.insert(0, Data.end_session_time.minute)
        self.entry_to_seconds.insert(0, Data.end_session_time.second)

    def apply_button_clicked(self):
        Data.start_session_time = datetime(datetime.now().year, datetime.now().month, datetime.now().day,
                                           int(self.entry_from_hours.get()),
                                           int(self.entry_from_minutes.get()),
                                           int(self.entry_from_seconds.get()))

        Data.end_session_time = datetime(datetime.now().year, datetime.now().month, datetime.now().day,
                                         int(self.entry_to_hours.get()),
                                         int(self.entry_to_minutes.get()),
                                         int(self.entry_to_seconds.get()))
