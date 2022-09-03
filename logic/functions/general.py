import _thread
import cv2
from tkinter import messagebox
import time
from logic.data import Data
from logic.functions.server import start_server
from model.database import DataBase
from model.gallery_logic import *
from model.ssp import *
from datetime import datetime


def add_new_line_table(line):
    # Data.data_table.insert(parent='', index='end', text='', values=('20:30:22', '20', '50', '30', '30,40'))
    Data.data_table.insert(parent='', index='end', text='', values=line)


def change_text_lbl():
    if datetime.now() < Data.start_session_time:
        Data.data_timer_lbl.config(text=" Next Session will be after", background="red")
        Data.duration_until_bext_session = Data.start_session_time - datetime.now()
        total_seconds = Data.duration_until_bext_session.seconds
        converted_format = time.strftime("%H:%M:%S", time.gmtime(total_seconds))
        Data.data_timer_number_lbl.config(text=converted_format, background="red")
        Data.header_timer_frame.config(background="red")

    elif datetime.now() > Data.end_session_time:
        Data.data_timer_lbl.config(text=" Next Session will be after", background="red")
        Data.duration_until_bext_session = datetime.now() - Data.start_session_time
        total_seconds = Data.duration_until_bext_session.seconds
        total_seconds = 86400 - total_seconds
        converted_format = time.strftime("%H:%M:%S", time.gmtime(total_seconds))
        Data.data_timer_number_lbl.config(text=converted_format, background="red")
        Data.header_timer_frame.config(background="red")

    else:
        Data.duration_until_bext_session = Data.end_session_time - datetime.now()
        total_seconds = Data.duration_until_bext_session.seconds
        converted_format = time.strftime("%H:%M:%S", time.gmtime(total_seconds))
        Data.data_timer_number_lbl.config(text=converted_format, background="#277BC0")
        Data.data_timer_lbl.config(text=" Session will be closed after", background="#277BC0")
        Data.header_timer_frame.config(background="#277BC0")


def window_dispose():
    if messagebox.askokcancel("Quit", "Do you want to exit?"):
        Data.repeater_session.stop()
        # Data.server.closeConn()
        Data.server.dispose()
        Data.root.destroy()


def show_warning(title, warning):
    messagebox.showwarning(title, warning)


def initial_files():
    videos = getAllNames(videosFolder)
    images = getAllNames(imageFolder)
    Data.files = images + videos


def initial_setup(root):
    Data.root = root
    Data.ssp = SSP()
    Data.cv = cv2
    Data.dataBase = DataBase()
    initial_files()
    _thread.start_new_thread(start_server, ())


def change_command_frame(frameName):
    frame = Data.commands_frames[frameName]
    frame.tkraise()
