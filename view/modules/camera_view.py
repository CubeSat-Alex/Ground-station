import _thread
import json
from tkinter import *
from logic.data import Data
from logic.functions import *
from logic.orders import *
from logic.ssp import *
from view.modules.gif import GifPlay


class CameraView(Frame):

    def __init__(self, *args):
        Frame.__init__(self, *args)

        camera_view_frame = Frame(self, bg="white")
        camera_view_buttons_frame = Frame(camera_view_frame, bg="white")
        Data.video_frame = Frame(camera_view_frame, bg="white")

        #         --------- Elements -----------

        self.camera_image = PhotoImage(file="images/view_lbl.png")
        self.camera_image2 = PhotoImage(file="images/real_view.png").subsample(2, 2)
        Data.image_view = Label(camera_view_frame, image=self.camera_image)

        self.play_image = PhotoImage(file="images/play.png")
        start_streem_button = Button(camera_view_buttons_frame, text="   Stream", image=self.play_image,
                                     compound="left",
                                     relief="flat", command=self.start_button_clicked)
        self.stop_image = PhotoImage(file="images/stop.png")
        stop_streem_button = Button(camera_view_buttons_frame, text="   Stop", image=self.stop_image, compound="left",
                                    relief="flat", command=self.stop_button_clicked)
        self.camera_icon = PhotoImage(file="images/camera.png")
        capture_image_button = Button(camera_view_buttons_frame, text="   Capture", image=self.camera_icon, compound="left",
                                            relief="flat", command=self.capture_button_clicked)

        #         --------- packing -----------

        camera_view_buttons_frame.pack(side="bottom")
        camera_view_frame.pack(side="left")

        start_streem_button.pack(side="left", pady=10, ipadx=30, ipady=10)
        stop_streem_button.pack(side="left", pady=10, ipadx=30, ipady=10)
        capture_image_button.pack(side="left", pady=10, ipadx=30, ipady=10)

        Data.image_view.pack(side="top")
        Data.video_frame.pack(side="top")

        #         --------- start run -----------

        self.gif = GifPlay(Data.image_view, 'images/gif.gif', 0.1)

    def start_button_clicked(self):
        # self.gif.start()
        _thread.start_new_thread(stream_thread_clicked, ())

    def stop_button_clicked(self):
        data = {
            'order': stopStream,
            'args': {'duration': 5, 'time': '24/8/22 13:34:00'},
        }
        jsonData = json.dumps(data)
        packet = Data.ssp.data2Packet(jsonData, Address.OBC, Type.Read)
        Data.server.senData(packet)

    def capture_button_clicked(self):
        # getImageNow
        _thread.start_new_thread(capture_thread_clicked, ())
