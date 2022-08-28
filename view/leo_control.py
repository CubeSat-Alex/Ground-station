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
        right_frame = Frame(self, bg="white")
        left_frame = Frame(self, bg="white")

        #         --------- Elements -----------

        session_period_frame = SessionPeriodFrame(left_frame) #
        request_data_frame = RequestDataFrame(right_frame) #
        command_frame = CommandsFrame(centered_frame)
        files_table_frame = FilesTableFrame(right_frame) #

        #         --------- packing -----------
        right_frame.pack(side="right")
        left_frame.pack(side="left", fill="y")
        centered_frame.pack(side="left")

        command_frame.pack(side="top")
        session_period_frame.pack(side="bottom", padx=40)
        request_data_frame.pack(side="top")
        files_table_frame.pack(side="top")

