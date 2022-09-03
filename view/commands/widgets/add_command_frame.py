import _thread
from tkinter import *
from logic.constant.orders import *
from logic.functions.general import *
from logic.functions.server import send_command_list
from view.commands.widgets.commands_list import CommandsListFrame


class OldCommandsFrame(Frame):

    def __init__(self, *args):
        Frame.__init__(self, *args, borderwidth=10, highlightbackground="black", highlightthickness=0,
                       background="white")

        #         --------- Frames -----------
        self.time_picker = None
        self.top = None
        self.image_video_selector = 1

        body_frame = Frame(self, bg="white")
        right_frame = Frame(body_frame, bg="white")
        left_frame = Frame(body_frame, bg="white")
        table_frame = Frame(right_frame, bg="white")
        table_buttons_frame = Frame(right_frame, bg="white")

        add_command_frame = Frame(left_frame, bg="white", width=1000, height=310, borderwidth=10,
                                  highlightbackground="black", highlightthickness=1, background="white")

        entry_frame = Frame(add_command_frame, bg="white")

        #         --------- Elements -----------

        self.button_background1 = PhotoImage(file="images/buttons/send.png").subsample(15, 15)
        send_button = Button(table_buttons_frame, text="   Send", command=self.send_button_clicked, relief="flat",
                             bg="white", activebackground="white", foreground="white", image=self.button_background1)

        self.button_background2 = PhotoImage(file="images/buttons/remove.png").subsample(15, 15)
        remove_row_button = Button(table_buttons_frame, text="   remove last row",
                                   command=self.remove_row_button_clicked,
                                   relief="flat", bg="white", activebackground="white", foreground="white",
                                   image=self.button_background2)

        add_command_lbl = Label(add_command_frame, text="Add command", bg="white", font=("Segoe UI", 14, "bold"))

        mission_name_lbl = Label(add_command_frame, text="Mission name", bg="white", font=("Segoe UI", 14))

        self.mission_name_entry = Entry(add_command_frame, width=20, fg='black', font=('Segoe UI', 16),
                                    background="white")

        self.take_image_button = Button(add_command_frame, text="take image", command=self.switch_button_image,
                                        relief="flat",
                                        bg="#0ba9bc", activebackground="white", font=("Segoe UI", 14, "bold"),
                                        foreground="white")
        self.take_video_button = Button(add_command_frame, text="take video", command=self.switch_button_video,
                                        relief="flat",
                                        bg="white", activebackground="white", font=("Segoe UI", 14, "bold"))

        with_angle_lbl = Label(add_command_frame, text="Camera Angle", bg="white", font=("Segoe UI", 14))
        x_lbl = Label(add_command_frame, text="X : ", bg="white", font=("Segoe UI", 14), foreground="#0ba9bc")
        y_lbl = Label(add_command_frame, text="Y : ", bg="white", font=("Segoe UI", 14), foreground="#0ba9bc")
        degree_lbl = Label(add_command_frame, text="degree", bg="white", font=("Segoe UI", 14), foreground="#0ba9bc")
        self.angle1_entry = Entry(add_command_frame, width=6, fg='black', font=('Arial', 16, 'bold'),
                                  background="white")
        self.angle2_entry = Entry(add_command_frame, width=6, fg='black', font=('Arial', 16, 'bold'),
                                  background="white")

        duration_lbl = Label(add_command_frame, text="Duration", bg="white", font=("Segoe UI", 14))
        self.duration_entry = Entry(add_command_frame, width=5, fg='black', font=('Arial', 16, 'bold'),
                                    background="white")
        minutes_lbl = Label(add_command_frame, text="min", bg="white", font=("Segoe UI", 14), foreground="#0ba9bc")

        execution_time_lbl = Label(add_command_frame, text="Execution Time", bg="white", font=("Segoe UI", 14))

        self.entry_year = Entry(entry_frame, bg="white", font=("Segoe UI", 18), foreground="#0ba9bc",
                                width=4, fg='black')

        self.entry_month = Entry(entry_frame, bg="white", font=("Segoe UI", 18), foreground="#0ba9bc",
                                 width=2, fg='black')
        self.entry_day = Entry(entry_frame, bg="white", font=("Segoe UI", 18), foreground="#0ba9bc",
                               width=2, fg='black')

        self.entry_hours = Entry(entry_frame, bg="white", font=("Segoe UI", 18), foreground="#0ba9bc",
                                 width=2, fg='black')
        self.entry_minutes = Entry(entry_frame, bg="white", font=("Segoe UI", 18), foreground="#0ba9bc",
                                   width=2, fg='black')
        self.entry_seconds = Entry(entry_frame, bg="white", font=("Segoe UI", 18), foreground="#0ba9bc",
                                   width=2, fg='black')

        self.button_background3 = PhotoImage(file="images/buttons/schedule.png").subsample(15, 15)
        add_to_table_button = Button(add_command_frame, text="Add to the Schedule", command=self.add_to_schedule,
                                     relief="flat", bg="white", activebackground="white", image=self.button_background3,
                                     foreground="white")

        #         --------- packing -----------

        body_frame.pack()
        left_frame.pack(side="top", fill="x")
        right_frame.pack(side="top", fill="x")
        table_frame.pack(side="top", expand=1, fill="both")
        table_buttons_frame.pack(side="top")
        add_command_frame.pack(side="top", ipady=10)

        send_button.pack(side="left", ipadx=20)
        remove_row_button.pack(side="left")

        add_command_lbl.place(x=10, y=0)
        mission_name_lbl.place(x=0, y=50)
        self.mission_name_entry.place(x=160, y=50)

        self.take_image_button.place(x=500, y=45)
        self.take_video_button.place(x=620, y=45)
        with_angle_lbl.place(x=0, y=120)
        x_lbl.place(x=150, y=120)
        y_lbl.place(x=280, y=120)
        degree_lbl.place(x=410, y=120)
        self.angle1_entry.place(x=180, y=120)
        self.angle2_entry.place(x=310, y=120)

        execution_time_lbl.place(x=0, y=235)
        entry_frame.place(x=170, y=230)
        # self.time_picker_button.place(x=170, y=230)
        Label(entry_frame, text=" Y: ", bg="white", font=("Segoe UI", 14), foreground="#0ba9bc").pack(side="left")
        self.entry_year.pack(side="left")
        Label(entry_frame, text=" M: ", bg="white", font=("Segoe UI", 14), foreground="#0ba9bc").pack(side="left")
        self.entry_month.pack(side="left")
        Label(entry_frame, text=" D: ", bg="white", font=("Segoe UI", 14), foreground="#0ba9bc").pack(side="left")
        self.entry_day.pack(side="left")
        Label(entry_frame, text="      H: ", bg="white", font=("Segoe UI", 14), foreground="#0ba9bc").pack(side="left")
        self.entry_hours.pack(side="left")
        Label(entry_frame, text=" M: ", bg="white", font=("Segoe UI", 14), foreground="#0ba9bc").pack(side="left")
        self.entry_minutes.pack(side="left")
        Label(entry_frame, text=" S: ", bg="white", font=("Segoe UI", 14), foreground="#0ba9bc").pack(side="left")
        self.entry_seconds.pack(side="left")

        duration_lbl.place(x=0, y=180)
        self.duration_entry.place(x=120, y=180)
        minutes_lbl.place(x=200, y=180)

        add_to_table_button.place(x=500, y=280)

        self.entry_year.insert(0, Data.execution_time.year)
        self.entry_month.insert(0, Data.execution_time.month)
        self.entry_day.insert(0, Data.execution_time.day)
        self.entry_hours.insert(0, Data.execution_time.hour)
        self.entry_minutes.insert(0, Data.execution_time.minute)
        self.entry_seconds.insert(0, Data.execution_time.second)
        self.mission_name_entry.insert(0, "default")

        self.angle1_entry.insert(0, "30")
        self.angle2_entry.insert(0, "60")
        self.duration_entry.insert(0, "0")

    # def remove_row_button_clicked(self):
    #
    #     if len(Data.command_map):
    #         Data.command_map.pop()
    #     Data.command_list_table.delete(*Data.command_list_table.get_children())
    #
    #     index = 0
    #     for task in Data.command_map:
    #         index = index + 1
    #         Data.command_list_table.insert(parent='', index='end', text='',
    #                                        values=(str(index),
    #                                                'take image' if task["task"] == getImageAt else 'take video',
    #                                                task["angle"],
    #                                                task["duration"],
    #                                                task["atTime"],
    #                                                task["name"]))

    def send_button_clicked(self):
        _thread.start_new_thread(send_command_list, ())

    def add_to_schedule(self):

        Data.execution_time = datetime(int(self.entry_year.get()),
                                       int(self.entry_month.get()),
                                       int(self.entry_day.get()),
                                       int(self.entry_hours.get()),
                                       int(self.entry_minutes.get()),
                                       int(self.entry_seconds.get()))

        temp_map = {"task": getImageAt if Data.selected_switch == 1 else getVideoAt,
                    "angle": self.angle1_entry.get() + ", " + self.angle2_entry.get(),
                    "duration": self.duration_entry.get(),
                    "atTime": str(Data.execution_time.strftime("%d/%m/%Y %H:%M:%S")),
                    "name": self.mission_name_entry.get().strip()}

        Data.command_map.append(temp_map)

        Data.command_list_table.delete(*Data.command_list_table.get_children())

        index = 0
        for task in Data.command_map:
            index = index + 1
            Data.command_list_table.insert(parent='', index='end', text='',
                                           values=(str(index),
                                                   'take image' if task["task"] == getImageAt else 'take video',
                                                   task["angle"],
                                                   task["duration"],
                                                   task["atTime"],
                                                   task["name"]))

    # def switch_button_image(self):
    #     Data.selected_switch = 1
    #     self.take_image_button.config(background="#0ba9bc", foreground="white")
    #     self.take_video_button.config(background="white", foreground="black")
    #
    # def switch_button_video(self):
    #     Data.selected_switch = 0
    #     self.take_image_button.config(background="white", foreground="black")
    #     self.take_video_button.config(background="#0ba9bc", foreground="white")
