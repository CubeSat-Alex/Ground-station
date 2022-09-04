from datetime import datetime
from tkinter import *
from tkinter.ttk import Style, Treeview
from logic.constant.constants import time_format
from logic.data import Data
from view.commands.widgets.time_picker import Picker


class LongTermFrame:
    def __init__(self, *args):
        Data.long_term_plan_map = Data.dataBase.getPlanes()

    def show(self):

        ws = Tk()
        ws.title("Long Term Plan")
        ws.geometry("1200x900")
        ws.config(bg="white")

        header_frame = Frame(ws, bg="white")
        second_frame = Frame(ws, bg="white")
        third_frame = Frame(ws, bg="white")
        forth_frame = Frame(ws, bg="white")
        table_frame = Frame(ws, bg="white")
        bottom_frame = Frame(ws, bg="white")

        header_frame.pack(side="top")
        second_frame.pack(side="top")
        third_frame.pack(side="top")
        forth_frame.pack(side="top")
        table_frame.pack(side="top", expand=1, fill='y')
        bottom_frame.pack(side="top")

        # Label(header_frame, text="Long-term plan", font=("", 15, "bold"), bg="white").pack(fill="x")

        Label(second_frame, text="Start session time", font=("", 17), bg="white").pack(side='left', padx=30)
        Data.long_start_button = Button(second_frame, text=str(Data.long_start_session_time.strftime(time_format)),
                                        font=("", 15, 'bold'), bg="#eeeeee", relief='flat', command=self.start_time_button)
        Data.long_start_button.pack(fill="y", side='left')

        Label(third_frame, text="End session time  ", font=("", 17), bg="white").pack(side='left', padx=30)
        Data.long_end_button = Button(third_frame, text=str(Data.long_end_session_time.strftime(time_format)),
                                      font=("", 15, 'bold'), bg="#eeeeee", relief='flat', command=self.end_time_button)
        Data.long_end_button.pack(fill="y", side='left', pady=10)

        Button(forth_frame, text="add to list", font=("", 13), bg="green", command=self.add_to_list, foreground="white",
               relief='flat').pack(fill="x", side="left", padx=20, pady=15, ipadx=50)
        Button(bottom_frame, text="remove last row", font=("", 13), bg="red", command=self.remove_last, foreground="white",
               relief='flat').pack(fill="x", side="left", padx=20, pady=15, ipadx=50)

        style = Style()
        style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Calibri', 11))
        style.configure("mystyle.Treeview.Heading", font=('Calibri', 14, 'bold'))
        style.configure("mystyle.Treeview", font=('Calibri', 13))

        Data.long_term_table = Treeview(table_frame, style="mystyle.Treeview", height=15)

        Data.long_term_table['columns'] = ('index', 'from', 'to')

        Data.long_term_table.column("#0", width=0)
        Data.long_term_table.column("index", anchor=CENTER, width=50)
        Data.long_term_table.column("from", anchor=CENTER, width=250)
        Data.long_term_table.column("to", anchor=CENTER, width=250)

        Data.long_term_table.heading("#0", text="", anchor=CENTER)
        Data.long_term_table.heading("index", text="", anchor=CENTER)
        Data.long_term_table.heading("from", text="From", anchor=CENTER)
        Data.long_term_table.heading("to", text="TO", anchor=CENTER)

        Data.long_term_table.pack(expand=1, fill='y')
        self.fill_table()

        ws.mainloop()

    def start_time_button(self):
        picker = Picker(datetime.now(), 'long_term_start')
        picker.show()

    def end_time_button(self):
        picker = Picker(datetime.now(), 'long_term_end')
        picker.show()

    def add_to_list(self):
        item = {
            'from': Data.long_start_session_time.strftime(time_format),
            'to': Data.long_end_session_time.strftime(time_format)
                }
        Data.dataBase.addPlan(item)
        Data.long_term_plan_map.append(item)
        self.fill_table()

    def remove_last(self):
        if len(Data.long_term_plan_map) > 0:
            Data.long_term_plan_map.pop()
            Data.dataBase.deletePlan()
            self.fill_table()

    def fill_table(self):

        # delete rows
        for i in Data.long_term_table.get_children():
            Data.long_term_table.delete(i)

        counter = 0

        for item in Data.long_term_plan_map:
            counter = counter+1
            Data.long_term_table.insert(parent='', index='end', text='', values=(
                counter, item['from'], item['to']
            ))
