from tkinter import *
from tkinter.ttk import Style, Treeview
from logic.data import Data


class LongTermFrame(Frame):

    def __init__(self, *args):
        Frame.__init__(self, *args, borderwidth=10, highlightbackground="black", highlightthickness=0.2,
                       background="white")

        ws = Tk()
        ws.title("Python Guides")
        ws.geometry("1200x900")
        ws.config(bg="white")

        header_frame = Frame(ws)
        second_frame = Frame(ws)
        third_frame = Frame(ws)
        forth_frame = Frame(ws)
        table_frame = Frame(ws)
        bottom_frame = Frame(ws)

        header_frame.pack(side="top")
        second_frame.pack(side="top")
        third_frame.pack(side="top")
        forth_frame.pack(side="top")
        table_frame.pack(side="top")
        bottom_frame.pack(side="top")

        Label(header_frame, text="Long-term plan", font=("", 15, "bold"), bg="white").pack(fill="x")

        Label(second_frame, text="Start session time", font=("", 17), bg="white").pack()
        Button(second_frame, text="2022-8-22 22:13:22", font=("", 17), bg="white").pack(fill="y")

        Label(third_frame, text="End session time", font=("", 17), bg="white").pack()
        Button(third_frame, text="2022-8-22 22:13:22", font=("", 17), bg="white").pack(fill="y")

        Button(forth_frame, text="add to list", font=("", 17), bg="green").pack(fill="y", side="left")
        Button(forth_frame, text="remove last row", font=("", 17), bg="red").pack(fill="y", side="left")

        style = Style()
        style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Calibri', 11))
        style.configure("mystyle.Treeview.Heading", font=('Calibri', 14, 'bold'))
        style.configure("mystyle.Treeview", font=('Calibri', 13))

        Data.long_term_table = Treeview(ws, style="mystyle.Treeview", height=15)

        Data.long_term_table['columns'] = ('index', 'from', 'to')

        Data.long_term_table.column("#0", width=0)
        Data.long_term_table.column("index", anchor=CENTER, width=50)
        Data.long_term_table.column("from", anchor=CENTER, width=250)
        Data.long_term_table.column("to", anchor=CENTER, width=250)

        Data.long_term_table.heading("#0", text="", anchor=CENTER)
        Data.long_term_table.heading("index", text="", anchor=CENTER)
        Data.long_term_table.heading("from", text="From", anchor=CENTER)
        Data.long_term_table.heading("to", text="TO", anchor=CENTER)

        Data.long_term_table.insert(parent='', index='end', text='', values=(
            "1", "2022-8-26 14:12:00", "2022-8-26 14:12:00"
        ))
        Data.long_term_table.insert(parent='', index='end', text='', values=(
            "2", "2022-8-26 14:12:00", "2022-8-26 14:12:00"
        ))

        Data.long_term_table.pack()

        ws.mainloop()
