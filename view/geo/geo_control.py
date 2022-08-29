from tkinter import *
from view.geo.widgets.camera_view import CameraView
from model.page import Page


class GEOControl(Page):

    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        self.config(bg="white")

        #         --------- Frames -----------
        # logo_head_frame = Frame(bg="white")
        centered_frame = Frame(self, bg="white")
        # camera_movement_control_frame = Frame(centered_frame, bg="white")
        # bottom_frame = Frame(camera_movement_control_frame, bg="white")

        #         --------- Elements -----------
        #
        # self.logo = PhotoImage(file="images/EgsaLogo.png").subsample(2, 2)
        # self.logo_lbl = Label(logo_head_frame, image=self.logo, bg="white")
        # self.dashboard_lbl = Label(logo_head_frame, text="GEO Control", bg="white", font=("Segoe UI", 30, "bold"),
        #                            background="white")
        #
        # self.logo_lbl.pack(side="left")
        # self.dashboard_lbl.pack(side="left", expand=1)
        # logo_head_frame.place(x=0, y=0)

        # joystick = Joystick(camera_movement_control_frame)
        camera_view = CameraView(centered_frame)
        # save_position_widget = SavePositionWidget(camera_movement_control_frame)
        # session_period_frame = SessionPeriodFrame(centered_frame)
        # request_data_frame = RequestDataFrame(centered_frame)
        # command_frame = CommandsFrame(self)

        # angle_lbl = Label(bottom_frame, text="Angle : ", font=("arial", 16), bg="white")
        # self.angle1_entry = Entry(bottom_frame, width=6, fg='black', font=('Arial', 16), background="#e8e8e8")
        # self.angle2_entry = Entry(bottom_frame, width=6, fg='black', font=('Arial', 16), background="#e8e8e8")
        #
        # self.button_background = PhotoImage(file="images/buttons/go.png").subsample(18, 18)
        # go_button = Button(bottom_frame, text="Go", command=self.go_button_clicked, relief="flat",
        #                    bg="white", activebackground="white", image=self.button_background, foreground="white")

        #         --------- packing -----------

        centered_frame.pack(anchor="center", expand=1)
        # bottom_frame.pack(side="bottom", pady=30)

        camera_view.pack(side="left", padx=20)
        # camera_movement_control_frame.pack(side="left", padx=80)
        # joystick.pack(side="left")
        # save_position_widget.pack(side="left", padx=50)
        # # session_period_frame.pack()
        # # request_data_frame.pack()
        # # command_frame.pack(side="bottom")
        #
        # angle_lbl.pack(side="left")
        # self.angle1_entry.pack(side="left")
        # self.angle2_entry.pack(side="left", padx=30)
        # go_button.pack(side="left")

    # def go_button_clicked(self):
    #     pass

