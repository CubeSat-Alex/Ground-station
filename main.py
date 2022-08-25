from tkinter import *
import _thread
from logic.data import *
from logic.database import DataBase
from logic.functions import window_dispose, start_server
from logic.ssp import SSP
from view.main_view import MainView
import cv2


root = Tk()
Data.root = root
Data.ssp = SSP()
Data.cv = cv2
Data.dataBase = DataBase()
_thread.start_new_thread(start_server, ())
main = MainView(root)
main.pack(side="top", fill="both", expand=True)
root.wm_geometry("1600x900+180+50")
root.title('Cube Satellite Station')
root.config(bg="#002B5B")
root.iconbitmap('images/satelite.ico')
root.minsize(600, 600)
root.wm_attributes('-transparentcolor', '#add123')
root.protocol("WM_DELETE_WINDOW", window_dispose)
root.mainloop()











