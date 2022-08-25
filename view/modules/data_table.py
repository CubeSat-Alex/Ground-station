from tkinter import *
from tkinter.ttk import Treeview
from logic.data import Data
from tkinter import messagebox


class DataTableFrame(Frame):

    def __init__(self, *args):
        Frame.__init__(self, *args, borderwidth=10, highlightbackground="black", highlightthickness=0.2,
                       background="white")

        all_frame = Frame(self, background="white")
        all_frame.pack()

        Data.data_table = Treeview(all_frame, height=60)
        self.control_button = Button(all_frame, text=" Export to CSV", command=self.export_button_click, relief="flat",
                                     bg="white", activebackground="white")

        Data.data_table['columns'] = ('Time', 'Temperature', 'Pressure', 'Acceleration', 'Angle')

        Data.data_table.column("#0", width=0, stretch=NO)
        Data.data_table.column("Time", anchor=CENTER, width=80)
        Data.data_table.column("Temperature", anchor=CENTER, width=80)
        Data.data_table.column("Pressure", anchor=CENTER, width=80)
        Data.data_table.column("Acceleration", anchor=CENTER, width=80)
        Data.data_table.column("Angle", anchor=CENTER, width=80)

        Data.data_table.heading("#0", text="", anchor=CENTER)
        Data.data_table.heading("Time", text="Time", anchor=CENTER)
        Data.data_table.heading("Temperature", text="Temperature", anchor=CENTER)
        Data.data_table.heading("Pressure", text="Pressure", anchor=CENTER)
        Data.data_table.heading("Acceleration", text="Acceleration", anchor=CENTER)
        Data.data_table.heading("Angle", text="Angle", anchor=CENTER)

        Data.data_table.insert(parent='', index='end', text='',
                       values=('20:22:23', '20', '1.5', '330', 'x = 30, y = 40'))
        Data.data_table.insert(parent='', index='end', text='',
                       values=('20:22:24', '21', '1.2', '323', 'x = 30, y = 40'))
        Data.data_table.insert(parent='', index='end', text='',
                       values=('20:22:25', '20', '1.5', '323', 'x = 30, y = 40'))
        Data.data_table.insert(parent='', index='end', text='',
                       values=('20:22:26', '21', '1.6', '353', 'x = 30, y = 40'))
        Data.data_table.insert(parent='', index='end', text='',
                       values=('20:22:27', '22', '1.5', '300', 'x = 30, y = 40'))
        Data.data_table.insert(parent='', index='end', text='',
                       values=('20:22:28', '23', '1.5', '300', 'x = 30, y = 40'))

        self.control_button.pack(anchor="se")
        Data.data_table.pack(side="top")


    def export_button_click(self):
        Data.dataBase.export()
        messagebox.showinfo("info", "Data Exported successfully")




