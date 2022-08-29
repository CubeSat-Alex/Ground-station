from tkinter import *
from tkinter.ttk import Treeview, Style
from logic.functions.general import *
from tkvideo import tkvideo


class FilesTableFrame(Frame):

    def __init__(self, *args):
        Frame.__init__(self, *args, borderwidth=10, highlightbackground="black", highlightthickness=0.2,
                       background="white")

        self.window = None
        all_frame = Frame(self, background="white")
        buttons_frame = Frame(all_frame, background="white")
        all_frame.pack()

        style = Style()
        style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Calibri', 11))
        style.configure("mystyle.Treeview.Heading", font=('Calibri', 12, 'bold'))
        style.configure("mystyle.Treeview", font=('Calibri', 12))

        Data.files_table = Treeview(all_frame, height=50, style="mystyle.Treeview")

        Data.files_table['columns'] = ('time', 'mission_name', 'command', 'angle', 'duration')

        Data.files_table.column("#0", width=0, stretch=NO)
        Data.files_table.column("time", anchor=CENTER, width=150)
        Data.files_table.column("mission_name", anchor=CENTER, width=120)
        Data.files_table.column("command", anchor=CENTER, width=100)
        Data.files_table.column("angle", anchor=CENTER, width=80)
        Data.files_table.column("duration", anchor=CENTER, width=80)

        Data.files_table.heading("#0", text="", anchor=CENTER)
        Data.files_table.heading("time", text="Time", anchor=CENTER)
        Data.files_table.heading("mission_name", text="mission name", anchor=CENTER)
        Data.files_table.heading("command", text="command", anchor=CENTER)
        Data.files_table.heading("angle", text="angle", anchor=CENTER)
        Data.files_table.heading("duration", text="duration", anchor=CENTER)

        buttons_frame.pack(side="top")
        Data.files_table.bind("<Double-1>", self.OnDoubleClick)
        Data.files_table.pack(side="top", fill="y")

        self.fill_table()

        self.button_time = PhotoImage(file="images/buttons/time.png").subsample(18, 18)
        self.button_duration = PhotoImage(file="images/buttons/duration.png").subsample(18, 18)
        self.button_mission = PhotoImage(file="images/buttons/mission.png").subsample(18, 18)

        sort_by_time_button = Button(buttons_frame, command=self.sort_by_time_button_click,
                                     relief="flat", bg="white", activebackground="white", foreground="black",
                                     font=("Segoe UI", 14), image=self.button_time)

        sort_by_duration_button = Button(buttons_frame, command=self.sort_by_duration_button_click,
                                     relief="flat", bg="white", activebackground="white", foreground="black",
                                         font=("Segoe UI", 14), highlightthickness=10, highlightcolor="black"
                                         , image=self.button_duration,)

        sort_by_mission_button = Button(buttons_frame, command=self.sort_by_mission_button_click,
                                     font=("Segoe UI", 14), relief="flat", bg="white", activebackground="white",
                                        foreground="black", image=self.button_mission)
        sort_lbl = Label(buttons_frame, text="Sort by : ",
                                     font=("Segoe UI", 14), relief="flat", bg="white", activebackground="white",
                                        foreground="black")

        sort_lbl.pack(side="left", padx= 15)
        sort_by_time_button.pack(side="left")
        sort_by_duration_button.pack(side="left")
        sort_by_mission_button.pack(side="left")

    def sort_by_time_button_click(self):
        Data.files = sortGallery(Data.files, SortType.date)
        self.fill_table()

    def sort_by_duration_button_click(self):
        Data.files = sortGallery(Data.files, SortType.duration)
        self.fill_table()

    def sort_by_mission_button_click(self):
        Data.files = sortGallery(Data.files, SortType.mission)
        self.fill_table()

    def fill_table(self):
        for i in Data.files_table.get_children():
            Data.files_table.delete(i)

        for i in range(len(Data.files)):
            line = (Data.files[i].date, Data.files[i].mission,
                    'video' if str(Data.files[i].mission).find('avi') else 'image',
                    Data.files[i].x + ", " + Data.files[i].y, Data.files[i].duration)

            Data.files_table.insert(parent='', index='end', text=Data.files[i].path, values=line)

    def play_video(self, path):
        self.window = Toplevel()
        my_label = Label(self.window)
        my_label.pack()
        player = tkvideo(path, my_label, loop=0, size=(1280, 720))
        player.play()
        self.window.mainloop()

    def OnDoubleClick(self, event):
        item = Data.files_table.identify('item', event.x, event.y)
        print("you clicked on")
        path = Data.files_table.item(item, 'text')

        print("path : ", path)

        if str(path).strip().find('.avi') != -1:
            print('entered')
            self.play_video(Data.files_table.item(item, 'text'))
        else:
            # play image
            pass
