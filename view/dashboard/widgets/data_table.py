from tkinter import *
from tkinter.ttk import Treeview, Style
from logic.data import Data
from tkinter import messagebox
from logic.functions.general import add_new_line_table


class DataTableFrame(Frame):

    def __init__(self, *args):
        Frame.__init__(self, *args, borderwidth=10, highlightbackground="black", highlightthickness=0.2,
                       background="white")

        all_frame = Frame(self, background="white")
        all_frame.pack()

        style = Style(self)
        style.configure('Treeview', rowheight=70)  # SOLUTION

        # self.empty_space = Label(all_frame, text="0", bg="white", font=("Segoe UI", 30, "bold"), background="white",
        #                          foreground="white")

        Data.data_table = Treeview(all_frame, height=60)
        self.control_button = Button(all_frame, text=" Export to CSV", command=self.export_button_click, relief="flat",
                                     bg="white", activebackground="white")

        Data.data_table['columns'] = ('Time', 'Temperature', 'Pressure', 'Acceleration', 'Angle', 'altitude', 'LDR')

        Data.data_table.column("#0", width=0, stretch=NO)
        Data.data_table.column("Time", anchor=CENTER, width=130)
        Data.data_table.column("Temperature", anchor=CENTER, width=80)
        Data.data_table.column("Pressure", anchor=CENTER, width=80)
        Data.data_table.column("Acceleration", anchor=CENTER, width=80)
        Data.data_table.column("Angle", anchor=CENTER, width=80)
        Data.data_table.column("altitude", anchor=CENTER, width=80)
        Data.data_table.column("LDR", anchor=CENTER, width=80)

        Data.data_table.heading("#0", text="", anchor=CENTER)
        Data.data_table.heading("Time", text="Time", anchor=CENTER)
        Data.data_table.heading("Temperature", text="Temperature", anchor=CENTER)
        Data.data_table.heading("Pressure", text="Pressure", anchor=CENTER)
        Data.data_table.heading("Acceleration", text="Acceleration", anchor=CENTER)
        Data.data_table.heading("Angle", text="Angle", anchor=CENTER)
        Data.data_table.heading("altitude", text="Altitude", anchor=CENTER)
        Data.data_table.heading("LDR", text="LDR", anchor=CENTER)

        # self.empty_space.pack(anchor="center", pady=10)
        self.control_button.pack(anchor="se")
        Data.data_table.pack(side="top")

        self.add_data_to_table()

    def export_button_click(self):
        Data.dataBase.export()
        messagebox.showinfo("info", "Data Exported successfully")

    def add_data_to_table(self):

        data = Data.dataBase.getData()
        # delete rows
        for i in Data.data_table.get_children():
            Data.data_table.delete(i)

        for i in range(data.shape[0]):
            line = (data["date"][i], data["tempreture"][i], data["pressure"][i], data["acceleration"][i],
                    "X: " + str(data["angleX"][i])
                    + "\nY: " + str(data["angleY"][i])
                    + "\nZ: " + str(data["angleZ"][i]),
                    data["altitude"][i],
                    "F:" + str(data["ldr1"][i])
                    + "\nB:" + str(data["ldr2"][i])
                    + "\nR:" + str(data["ldr3"][i])
                    + "\nL:" + str(data["ldr4"][i]))
            add_new_line_table(line)

