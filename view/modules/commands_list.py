from tkinter import *
from tkinter.ttk import Treeview


class CommandsListFrame(Frame):

    def __init__(self, *args):
        Frame.__init__(self, *args, borderwidth=10, highlightbackground="black", highlightthickness=0.2,
                       background="white")
        # e = Entry(self, width=20, fg='blue', font=('Arial', 16, 'bold'))
        #
        # e.pack()

        table_frame = Frame(self)
        table_frame.pack()

        self.table_list = Treeview(table_frame)

        self.table_list['columns'] = ('ID', 'Command',  'Angle', 'Duration', 'Execution')

        self.table_list.column("#0", width=0, stretch=NO)
        self.table_list.column("ID", anchor=CENTER, width=80)
        self.table_list.column("Command", anchor=CENTER, width=80)
        self.table_list.column("Angle", anchor=CENTER, width=80)
        self.table_list.column("Duration", anchor=CENTER, width=80)
        self.table_list.column("Execution", anchor=CENTER, width=80)

        self.table_list.heading("#0", text="", anchor=CENTER)
        self.table_list.heading("ID", text="ID", anchor=CENTER)
        self.table_list.heading("Command", text="Command", anchor=CENTER)
        self.table_list.heading("Angle", text="Angle", anchor=CENTER)
        self.table_list.heading("Duration", text="Duration", anchor=CENTER)
        self.table_list.heading("Execution", text="Execution", anchor=CENTER)

        self.table_list.insert(parent='', index='end', text='', values=('1', 'take image', '30,45', '0', '14:30:00'))

        self.table_list.pack()

