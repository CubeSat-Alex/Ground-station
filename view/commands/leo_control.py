from tkinter import *
from logic.data import Data
from view.commands.widgets.commands_frame import CommandsFrame
from view.commands.widgets.commands_list import CommandsListFrame
from view.commands.widgets.commands_tree_view import TreeView
from model.page import Page
from view.commands.widgets.real_table import RealtimeTable
import customtkinter


class Control(Page):

    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        self.config(bg="white")

        #         --------- Frames -----------
        right_frame = Frame(self, bg="white")
        left_frame = Frame(self, bg="white")
        bottom_frame = Frame(self, bg="white")
        mission_name_frame = Frame(self, bg="white", height=300)

        #         --------- Elements -----------

        tree_view = TreeView(left_frame)
        command_list = CommandsListFrame(bottom_frame)
        commands_frame = CommandsFrame(bottom_frame)
        realtime_table = RealtimeTable(right_frame)

        Data.mission_entry = customtkinter.CTkEntry(master=mission_name_frame, text_font=("Segoe UI", 18), width=500)
        customtkinter.CTkLabel(mission_name_frame, text=" Mission Name: ", text_font=("Segoe UI", 14), text_color='black').pack(side="left")
        Data.mission_entry.pack(side="left")

        Data.mission_entry.insert(0, "General Mission")
        Label(mission_name_frame, text=" Mission Name: ", bg="red", font=("Segoe UI", 14), foreground='white').pack(side="top",ipady=300, pady=300)

        Data.overlay_lbl = Label(bottom_frame, text='Ready', font=('', 16), bg='#54FA9B')
        Data.overlay_lbl.pack(side='top', fill='x')

        #         --------- packing -----------
        right_frame.pack(side="right", fill="y")
        left_frame.pack(side="left", fill="y")
        bottom_frame.pack(side="bottom", fill="x")

        tree_view.pack(side="left", fill='y')
        realtime_table.pack(side="left", fill='y')
        mission_name_frame.pack(side="top", fill='x')
        commands_frame.pack(side="top", fill='x')
        command_list.pack(side="top", fill='x')




