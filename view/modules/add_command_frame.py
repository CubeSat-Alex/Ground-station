import _thread
from datetime import datetime
from tkinter import *
from tktimepicker import AnalogPicker, constants
from logic.data import Data
from logic.functions import *
from view.modules.commands_list import CommandsListFrame
from tkinter import messagebox


class CommandsFrame(Frame):

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
        table_frame = Frame(right_frame, bg="white",)
        table_buttons_frame = Frame(right_frame, bg="white")
        add_command_frame = Frame(left_frame, bg="white", width=600, height=250, borderwidth=10, highlightbackground="black", highlightthickness=1,
                       background="white")

        #         --------- Elements -----------

        command_list = CommandsListFrame(table_frame)

        self.button_background1 = PhotoImage(file="images/buttons/send.png").subsample(15, 15)
        send_button = Button(table_buttons_frame, text="   Send", command=self.send_button_clicked, relief="flat",
                             bg="white", activebackground="white", foreground="white", image=self.button_background1)

        self.button_background2 = PhotoImage(file="images/buttons/remove.png").subsample(15, 15)
        remove_row_button = Button(table_buttons_frame, text="   remove last row", command=self.remove_row_button_clicked,
                                   relief="flat", bg="white", activebackground="white", foreground="white", image=self.button_background2)

        add_command_lbl = Label(add_command_frame, text="Add command", bg="white", font=("Segoe UI", 14, "bold"))

        self.take_image_button = Button(add_command_frame, text="take image", command=self.switch_button_image, relief="flat",
                             bg="#0ba9bc", activebackground="white", font=("Segoe UI", 14, "bold"), foreground="white")
        self.take_video_button = Button(add_command_frame, text="take video", command=self.switch_button_video, relief="flat",
                             bg="white", activebackground="white", font=("Segoe UI", 14, "bold"))

        with_angle_lbl = Label(add_command_frame, text="with Angle", bg="white", font=("Segoe UI", 14))
        x_lbl = Label(add_command_frame, text="X : ", bg="white", font=("Segoe UI", 14))
        y_lbl = Label(add_command_frame, text="Y : ", bg="white", font=("Segoe UI", 14))
        degree_lbl = Label(add_command_frame, text="degree", bg="white", font=("Segoe UI", 14))
        self.angle1_entry = Entry(add_command_frame, width=6, fg='black', font=('Arial', 16, 'bold'),
                                  background="#e8e8e8")
        self.angle2_entry = Entry(add_command_frame, width=6, fg='black', font=('Arial', 16, 'bold'),
                                  background="#e8e8e8")

        duration_lbl = Label(add_command_frame, text="Duration", bg="white", font=("Segoe UI", 14))
        self.duration_entry = Entry(add_command_frame, width=5, fg='black', font=('Arial', 16, 'bold'), background="#e8e8e8")
        minutes_lbl = Label(add_command_frame, text="min", bg="white", font=("Segoe UI", 14))

        execution_time_lbl = Label(add_command_frame, text="Execution Time", bg="white", font=("Segoe UI", 16))
        self.time_picker_button = Button(add_command_frame, text=Data.execution_time.strftime("%H:%M:%S"),
                                         command=self.time_picker_button_clicked, relief="flat", bg="white",
                                         activebackground="white", font=("Segoe UI", 15), foreground="#0ba9bc")

        self.button_background3 = PhotoImage(file="images/buttons/schedule.png").subsample(15, 15)
        add_to_table_button = Button(add_command_frame, text="Add to the Schedule", command=self.add_to_schedule,
                                   relief="flat", bg="white", activebackground="white", image=self.button_background3,
                                     foreground="white")

        #         --------- packing -----------

        body_frame.pack()
        right_frame.pack(side="right")
        left_frame.pack(side="right")
        table_frame.pack(side="top")
        table_buttons_frame.pack(side="top")
        add_command_frame.pack(side="top", ipady=10)

        command_list.pack()
        send_button.pack(side="left", padx=20, ipadx=20)
        remove_row_button.pack(side="left")

        add_command_lbl.place(x=210, y=0)
        self.take_image_button.place(x=150, y=50)
        self.take_video_button.place(x=300, y=50)
        with_angle_lbl.place(x=0, y=120)
        x_lbl.place(x=120, y=120)
        y_lbl.place(x=250, y=120)
        degree_lbl.place(x=380, y=120)
        self.angle1_entry.place(x=150, y=120)
        self.angle2_entry.place(x=280, y=120)

        execution_time_lbl.place(x=0, y=200)
        self.time_picker_button.place(x=170, y=195)

        duration_lbl.place(x=0, y=160)
        self.duration_entry.place(x=100, y=160)
        minutes_lbl.place(x=200, y=160)

        add_to_table_button.place(x=380, y=220)

    def remove_row_button_clicked(self):
        Data.command_map.pop()

        Data.command_list_table.delete(*Data.command_list_table.get_children())

        index = 0
        for task in Data.command_map:
            index = index + 1
            Data.command_list_table.insert(parent='', index='end', text='',
                                           values=(str(index),
                                                   'take image' if task["task"] == getImageAt else 'take video',
                                                   task["angle"],
                                                   task["duration"],
                                                   task["executionTime"]))
    def send_button_clicked(self):
        _thread.start_new_thread(send_command_list, ())

    def add_to_schedule(self):

        temp_map = {"task": getImageAt if Data.selected_switch == 1 else getVideoAt,
                    "angle": self.angle1_entry.get() + ", " + self.angle2_entry.get(),
                    "duration": self.duration_entry.get(),
                    "atTime": str(Data.execution_time.strftime("%d/%m/%Y %H:%M:%S"))}

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
                                                   task["atTime"]))

    def time_picker_button_clicked(self):
        self.top = Toplevel()
        self.top.title("Time picker")
        self.time_picker = AnalogPicker(self.top, type=constants.HOURS24)
        self.time_picker.pack(expand=True, fill="both", pady=20, padx=20)

        ok_btn = Button(self.top, text="Set", command=self.update_time_from_button, bg="black",
                        font=("Courier", 14, "bold"), foreground="white", relief="flat")
        ok_btn.pack(ipadx=80)

    def update_time_from_button(self):
        Data.execution_time = datetime(datetime.now().year, datetime.now().month, datetime.now().day,
                                       self.time_picker.time()[0], self.time_picker.time()[1], 0)
        text = Data.execution_time.strftime("%H:%M:%S")
        self.time_picker_button.configure(text=text)
        self.top.destroy()

    def switch_button_image(self):
        Data.selected_switch = 1
        self.take_image_button.config(background="#0ba9bc", foreground="white")
        self.take_video_button.config(background="white", foreground="black")

    def switch_button_video(self):
        Data.selected_switch = 0
        self.take_image_button.config(background="white", foreground="black")
        self.take_video_button.config(background="#0ba9bc", foreground="white")


