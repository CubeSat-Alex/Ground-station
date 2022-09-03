from tkinter import *
from tkinter.ttk import Treeview, Style
from logic.data import Data
from datetime import datetime


class CommandsListFrame(Frame):

    def __init__(self, *args):
        Frame.__init__(self, *args, borderwidth=10, highlightbackground="black", highlightthickness=0.2,
                       background="white")

        style = Style()
        style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Calibri', 11))
        style.configure("mystyle.Treeview.Heading", font=('Calibri', 14, 'bold'))
        style.configure("mystyle.Treeview", font=('Calibri', 13))

        Data.command_list_table = Treeview(self, style="mystyle.Treeview", height=15)

        Data.command_list_table['columns'] = ('ID', 'Command', 'Execution', 'name', 'arguments')

        Data.command_list_table.column("#0", width=0)
        Data.command_list_table.column("ID", anchor=CENTER, width=25)
        Data.command_list_table.column("Command", anchor=CENTER, width=250)
        Data.command_list_table.column("Execution", anchor=CENTER, width=250)
        Data.command_list_table.column("name", anchor=CENTER, width=150)
        Data.command_list_table.column("arguments", anchor=CENTER, width=250)

        Data.command_list_table.heading("#0", text="", anchor=CENTER)
        Data.command_list_table.heading("ID", text="", anchor=CENTER)
        Data.command_list_table.heading("Command", text="Command", anchor=CENTER)
        Data.command_list_table.heading("Execution", text="Upload Time", anchor=CENTER)
        Data.command_list_table.heading("name", text="Mission name", anchor=CENTER)
        Data.command_list_table.heading("arguments", text="Arguments", anchor=CENTER)

        # Data.command_list_table.insert(parent='', index='end', text='', values=(
        #     "1", "take image", datetime.now(), "alex", "angle: 30,60"
        # ))
        # Data.command_list_table.insert(parent='', index='end', text='', values=(
        #     "2", "take video", datetime.now(), "alex", "angle: 30,60 , duration : 3 min"
        # ))

        Data.command_list_table.pack()
