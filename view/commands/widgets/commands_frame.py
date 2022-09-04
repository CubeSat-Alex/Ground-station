from tkinter import *
from logic.constant.orders import *
from logic.functions.general import *
from view.commands.widgets.command_properties_frames.download import DownloadsFrame
from view.commands.widgets.command_properties_frames.empty_command_frame import EmptyCommands
from view.commands.widgets.command_properties_frames.direct import *
from view.commands.widgets.command_properties_frames.logs import LogsFrame
from view.commands.widgets.command_properties_frames.mission import *
from view.commands.widgets.command_properties_frames.playback import *


class CommandsFrame(Frame):

    def __init__(self, *args):
        Frame.__init__(self, *args, borderwidth=10, highlightbackground="black", highlightthickness=1,
                       background="white")

        #         --------- Frames -----------
        container = Frame(self, bg="white")
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

    def add_to_schedule(self):

        Data.execution_time = datetime(int(self.entry_year.get()),
                                       int(self.entry_month.get()),
                                       int(self.entry_day.get()),
                                       int(self.entry_hours.get()),
                                       int(self.entry_minutes.get()),
                                       int(self.entry_seconds.get()))

        temp_map = {"task": getImageAt if Data.selected_switch == 1 else getVideoAt,
                    "angle": self.angle1_entry.get() + ", " + self.angle2_entry.get(),
                    "duration": self.duration_entry.get(),
                    "atTime": str(Data.execution_time.strftime("%d/%m/%Y %H:%M:%S")),
                    "name": self.mission_name_entry.get().strip()}

        Data.command_map.append(temp_map)

        Data.command_list_table.delete(*Data.command_list_table.get_children())

        index = 0
        for task in Data.command_map:
            index = index + 1
            Data.command_list_table.insert(parent='', index='end', text='',
                                           values=(str(index),
                                                   'take image' if task["task"] == getImageAt else 'take video',
                                                   task["angle"],
                                                   task["duration"],
                                                   task["atTime"],
                                                   task["name"]))
