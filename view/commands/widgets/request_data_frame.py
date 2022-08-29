import _thread
from tkinter import *
from logic.functions.general import *


class RequestDataFrame(Frame):

    def __init__(self, *args):
        Frame.__init__(self, *args, borderwidth=10, highlightbackground="black", highlightthickness=0.2,
                       background="white")

        header_frame = Frame(self, bg="white")
        buttons_frame = Frame(self, bg="white")

        #         --------- elements -----------

        header_lbl = Label(header_frame, text="Request Data", bg="white", font=("Segoe UI", 14, "bold"))
        self.button_background1 = PhotoImage(file="images/buttons/telemetry.png").subsample(12, 12)
        self.button_background2 = PhotoImage(file="images/buttons/images.png").subsample(12, 12)
        self.button_background3 = PhotoImage(file="images/buttons/videos.png").subsample(12, 12)

        get_telemetry_button = Button(buttons_frame, text="Get Telemetry Data", command=self.get_telemetry_click, relief="flat", bg="white",
                             activebackground="white", font=("Segoe UI", 16), image=self.button_background1, foreground="white")
        get_saved_images_button = Button(buttons_frame, text="Get Saved Images", command=self.get_saved_images_click, relief="flat", bg="white",
                                     activebackground="white", font=("Segoe UI", 16), image=self.button_background2, foreground="white")
        get_saved_videos_button = Button(buttons_frame, text="Get Saved Videos", command=self.get_saved_videos_click, relief="flat", bg="white",
                                     activebackground="white", font=("Segoe UI", 16), image=self.button_background3, foreground="white")

        #         --------- packing -----------

        header_frame.pack()
        buttons_frame.pack()
        header_lbl.pack()
        get_telemetry_button.pack(pady=2)
        get_saved_images_button.pack(pady=2)
        get_saved_videos_button.pack(pady=2)

    def get_telemetry_click(self):
        # getTelemetry
        _thread.start_new_thread(get_telemetry, ())

    def get_saved_images_click(self):
        _thread.start_new_thread(get_saved_images, ())

    def get_saved_videos_click(self):
        _thread.start_new_thread(get_saved_videos, ())
