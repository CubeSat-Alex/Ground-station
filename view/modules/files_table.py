from datetime import datetime
from tkinter import *
from tkinter.ttk import Treeview
from logic.data import Data
from tkinter import messagebox
from logic.functions import add_new_line_table


class FilesTableFrame(Frame):

    def __init__(self, *args):
        Frame.__init__(self, *args, borderwidth=10, highlightbackground="black", highlightthickness=0.2,
                       background="white")

        all_frame = Frame(self, background="white")
        all_frame.pack()

        Data.files_table = Treeview(all_frame, height=60)
        # self.control_button = Button(all_frame, text=" Export to CSV", relief="flat",
        #                              bg="white", activebackground="white")

        Data.files_table['columns'] = ('time', 'mission_name', 'command', 'angle', 'duration')

        Data.files_table.column("#0", width=0, stretch=NO)
        Data.files_table.column("time", anchor=CENTER, width=130)
        Data.files_table.column("mission_name", anchor=CENTER, width=80)
        Data.files_table.column("command", anchor=CENTER, width=80)
        Data.files_table.column("angle", anchor=CENTER, width=80)
        Data.files_table.column("duration", anchor=CENTER, width=80)

        Data.files_table.heading("#0", text="", anchor=CENTER)
        Data.files_table.heading("time", text="Time", anchor=CENTER)
        Data.files_table.heading("mission_name", text="mission_name", anchor=CENTER)
        Data.files_table.heading("command", text="command", anchor=CENTER)
        Data.files_table.heading("angle", text="angle", anchor=CENTER)
        Data.files_table.heading("duration", text="duration", anchor=CENTER)

        # data = Data.dataBase.getData()
        #
        # for i in Data.data_table.get_children():
        #     Data.data_table.delete(i)
        #
        # for i in range(data.shape[0]):
        #     line = (data["date"][i], data["tempreture"][i], data["pressure"][i], data["acceleration"][i],
        #             "X: " + str(data["angleX"][i]) + "Y: " + str(data["angleY"][i]) + "Z: " + str(data["angleZ"][i]),
        #             data["altitude"][i],
        #             "F:" + str(data["ldr1"][i]) + "B:" + str(data["ldr2"][i]) + "R:" + str(data["ldr3"][i]) + "L:" + str(data["ldr4"][i]))
        #     add_new_line_table(line)

        # self.control_button.pack(anchor="se")
        Data.files_table.pack(side="top", fill="y")

        Data.files_table.insert(parent='', index='end', text='',
                                values=(datetime.now().strftime("%H:%M:%S"), "alex", "take image", "x:20,y=45", "0"))

    # def export_button_click(self):
    #     Data.dataBase.export()
    #     messagebox.showinfo("info", "Data Exported successfully")




