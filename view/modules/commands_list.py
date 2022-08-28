from tkinter import *
from tkinter.ttk import Treeview

from logic.data import Data


class CommandsListFrame(Frame):

    def __init__(self, *args):
        Frame.__init__(self, *args, borderwidth=10, highlightbackground="black", highlightthickness=0.2,
                       background="white")

        table_frame = Frame(self)
        table_frame.pack(fill="both", expand=1)

        Data.command_list_table = Treeview(table_frame)

        Data.command_list_table['columns'] = ('ID', 'Command',  'Angle', 'Duration', 'Execution')

        Data.command_list_table.column("#0", width=0, stretch=NO)
        Data.command_list_table.column("ID", anchor=CENTER, width=80)
        Data.command_list_table.column("Command", anchor=CENTER, width=80)
        Data.command_list_table.column("Angle", anchor=CENTER, width=80)
        Data.command_list_table.column("Duration", anchor=CENTER, width=80)
        Data.command_list_table.column("Execution", anchor=CENTER, width=120)

        Data.command_list_table.heading("#0", text="", anchor=CENTER)
        Data.command_list_table.heading("ID", text=" ", anchor=CENTER)
        Data.command_list_table.heading("Command", text="Command", anchor=CENTER)
        Data.command_list_table.heading("Angle", text="Angle", anchor=CENTER)
        Data.command_list_table.heading("Duration", text="Duration", anchor=CENTER)
        Data.command_list_table.heading("Execution", text="Execution Time", anchor=CENTER)

        # Data.command_list_table.insert(parent='', index='end', text='', values=('1', 'take image', '30,45', '0', '14:30:00'))

        Data.command_list_table.pack(fill="both", expand=1)



