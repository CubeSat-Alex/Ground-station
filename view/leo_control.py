from tkinter import *
from view.modules.add_command_frame import CommandsFrame
from view.modules.files_table import FilesTableFrame
from view.modules.page import Page
from view.modules.request_data_frame import RequestDataFrame
from view.modules.session_period_frame import SessionPeriodFrame


class Control(Page):

    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        self.config(bg="white")

        #         --------- Frames -----------
        centered_frame = Frame(self, bg="white")

        #         --------- Elements -----------

        session_period_frame = SessionPeriodFrame(self)
        request_data_frame = RequestDataFrame(centered_frame)
        command_frame = CommandsFrame(centered_frame)
        files_table_frame = FilesTableFrame(centered_frame)

        #         --------- packing -----------

        centered_frame.pack(anchor="center", expand=1, fill="both")

        request_data_frame.pack(side="right", padx=100)
        session_period_frame.pack(anchor="sw")
        command_frame.pack(side="bottom")
        files_table_frame.pack(side="right")

