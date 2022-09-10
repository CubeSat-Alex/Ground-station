from tkinter import *
from logic.constant.orders import *
from logic.functions.general import *
from view.commands.widgets.command_properties_frames.download import DownloadsFrame
from view.commands.widgets.command_properties_frames.empty_command_frame import EmptyCommands
from view.commands.widgets.command_properties_frames.direct import *
from view.commands.widgets.command_properties_frames.logs import LogsFrame
from view.commands.widgets.command_properties_frames.mission import *
from view.commands.widgets.command_properties_frames.playback import *
import customtkinter


class CommandsFrame(Frame):

    def __init__(self, *args):
        Frame.__init__(self, *args, borderwidth=10, highlightbackground="black", highlightthickness=1,
                       background="white")

        #         --------- Frames -----------
        container = customtkinter.CTkFrame(self, bg="white")
        container.pack(side="top", fill="both")
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        Data.commands_frames = {}
        for F in (GetTimeDifferenceFrame, SetOnBoardTimeFrame, SetSessionTimeFrame, ADCSFrame, GPSFrame,
                  OpenRealTimeFrame, EmptyCommands, DownloadsFrame, LogsFrame,
                  GETTelemetryFrame, TakeImageFrame, TakeVideoFrame, StorageFrame):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            Data.commands_frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        change_command_frame("EmptyCommands")
