from tkinter import *
from datetime import datetime
from logic.data import Data


class LogsFrame(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.config(borderwidth=0, highlightbackground="white", highlightthickness=0.2, bg="white", height=100)
        self.controller = controller

        label = Label(self, text="Logs", font=("", 14, "bold"), background="white")
        label.pack(side="top", fill="x")

        content_frame = Frame(self, bg="white")
        content_frame.pack(anchor="center", pady=20, fill="both", expand=1)

        button = Button(self, text="Get Logs", font=("", 14, "bold"), command=self.get_all_logs_button_clicked,
                        relief="flat")
        button.pack(side="bottom", fill="x")

        button = Button(self, text="Delete Logs", font=("", 14, "bold"), command=self.delete_all_logs_button_clicked,
                        relief="flat")
        button.pack(side="bottom", fill="x")

    def get_all_logs_button_clicked(self):
        Data.commands_counter = Data.commands_counter + 1
        Data.command_list_table.insert(parent='', index='end', text='', values=(
            str(Data.commands_counter), "get logs", datetime.now().strftime("%d_%m_%Y %H-%M-%S"),
            Data.mission_entry.get(), ' - '
        ))

    def delete_all_logs_button_clicked(self):
        Data.commands_counter = Data.commands_counter + 1
        Data.command_list_table.insert(parent='', index='end', text='', values=(
            str(Data.commands_counter), "delete logs", datetime.now().strftime("%d_%m_%Y %H-%M-%S"),
            Data.mission_entry.get(), ' - '
        ))
