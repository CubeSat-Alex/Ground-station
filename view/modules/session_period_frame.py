import datetime
from tkinter import *
from tktimepicker import AnalogPicker, constants, SpinTimePickerModern
from logic.data import Data
from logic.functions import *


class SessionPeriodFrame(Frame):

    def __init__(self, *args):
        Frame.__init__(self, *args, borderwidth=10, highlightbackground="black", highlightthickness=0.2,
                       background="white")

        self.top = None
        self.time_picker = None
        header_frame = Frame(self, bg="white")
        bottom_frame = Frame(self, bg="white")
        from_frame = Frame(bottom_frame, bg="white")
        to_frame = Frame(bottom_frame, bg="white")

        #         --------- elements -----------

        header_lbl = Label(header_frame, text="Session Duration", bg="white", font=("Segoe UI", 14, "bold"))
        from_lbl = Label(from_frame, text="From", bg="white", font=("Segoe UI", 18))
        to_lbl = Label(to_frame, text="To", bg="white", font=("Segoe UI", 18))

        self.from_button = Button(from_frame, text="12:7:00", command=self.from_button_clicked, relief="flat", bg="white",
                             activebackground="white", font=("Segoe UI", 18), foreground="#0ba9bc")

        self.to_button = Button(to_frame, text="12:8:00", command=self.to_button_clicked, relief="flat", bg="white",
                           activebackground="white", font=("Segoe UI", 18), foreground="#0ba9bc")

        #         --------- packing -----------

        header_frame.pack(side="top")
        bottom_frame.pack(side="top")
        from_frame.pack(side="left")
        to_frame.pack(side="left")

        header_lbl.pack(anchor="center", expand=1)
        from_lbl.pack(side="top")
        to_lbl.pack(side="top")
        self.from_button.pack(side="top", padx=5)
        self.to_button.pack(side="top", padx=5)

    def from_button_clicked(self):
        self.top = Toplevel()
        self.top.title("Time picker")
        self.time_picker = SpinTimePickerModern(self.top)
        self.time_picker.pack(expand=True, fill="both", pady=20, padx=20)

        ok_btn = Button(self.top, text="Set", command=self.update_time_from_button, bg="black",
                        font=("Courier", 14, "bold"), foreground="white", relief="flat")
        ok_btn.pack(ipadx=80)

    def update_time_from_button(self):
        Data.start_session_time = datetime(2022, 8, 24, self.time_picker.time()[0], self.time_picker.time()[1], 0)
        text = Data.start_session_time.strftime("%H:%M:%S")
        self.from_button.configure(text=text)
        self.top.destroy()

    def to_button_clicked(self):
        self.top = Toplevel()
        self.top.title("Time picker")
        self.time_picker = AnalogPicker(self.top, type=constants.HOURS24)
        self.time_picker.pack(expand=True, fill="both", pady=20, padx=20)
        ok_btn = Button(self.top, text="Set", command=self.update_time_to_button, bg="black",
                        font=("Courier", 14, "bold"), foreground="white", relief="flat")
        ok_btn.pack(ipadx=80)

    def update_time_to_button(self):
        temp = self.time_picker.time()[0]
        Data.end_session_time = datetime(2022, 8, 24, temp, self.time_picker.time()[1], 0)
        text = Data.end_session_time.strftime("%H:%M:%S")
        self.to_button.configure(text=text)
        self.top.destroy()

