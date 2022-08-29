from tkinter import *


class SavePositionWidget(Frame):

    def __init__(self, *args):
        Frame.__init__(self, *args)
        self.config(bg="white")
        #         --------- Frames -----------
        lbl_frame = Frame(self, bg="white")
        colored_buttons_frame = Frame(self, bg="white")
        save_go_frame = Frame(self, bg="white")

        #         --------- Elements -----------

        save_location = Label(lbl_frame, text="Save Position", font=("arial", 16), bg="white")

        self.save_image = PhotoImage(file="images/saved.png")
        save_image_button = Button(save_go_frame, text=" Save", image=self.save_image, compound="left",
                                   relief="flat", bg="white", font=("", 13))

        self.go_image = PhotoImage(file="images/go.png")
        go_image_button = Button(save_go_frame, text=" Go", image=self.go_image, compound="left",
                                 relief="flat", bg="white", font=("", 13))

        self.register_1_button = Button(colored_buttons_frame, relief="solid", width=4, height=2, bg="#B1D7B4",
                                        command=lambda: self.register_button_clicked(1))
        self.register_2_button = Button(colored_buttons_frame, relief="solid", width=4, height=2, bg="#B1D7B4",
                                        command=lambda: self.register_button_clicked(2))
        self.register_3_button = Button(colored_buttons_frame, relief="solid", width=4, height=2, bg="#B1D7B4",
                                        command=lambda: self.register_button_clicked(3))
        self.register_4_button = Button(colored_buttons_frame, relief="solid", width=4, height=2, bg="#B1D7B4",
                                        command=lambda: self.register_button_clicked(4))

        #         --------- packing -----------

        self.register_1_button.pack(side="left")
        self.register_2_button.pack(side="left")
        self.register_3_button.pack(side="left")
        self.register_4_button.pack(side="left")

        save_location.pack(pady=20)
        lbl_frame.pack(side="top")
        colored_buttons_frame.pack(side="top")
        save_go_frame.pack(side="top", pady=20)

        save_image_button.pack(side="left", ipady=5, padx=5)
        go_image_button.pack(side="left", ipady=5)

    def register_button_clicked(self, selector):
        selected_register = selector
        self.register_1_button.config(bg="#B1D7B4")
        self.register_2_button.config(bg="#B1D7B4")
        self.register_3_button.config(bg="#B1D7B4")
        self.register_4_button.config(bg="#B1D7B4")
        if selector == 1:
            self.register_1_button.config(bg="#5BB318")
        if selector == 2:
            self.register_2_button.config(bg="#5BB318")
        if selector == 3:
            self.register_3_button.config(bg="#5BB318")
        if selector == 4:
            self.register_4_button.config(bg="#5BB318")
