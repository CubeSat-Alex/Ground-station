from tkinter import *
from logic.functions.general import window_dispose, initial_setup
from view.main_view import MainView


root = Tk()
initial_setup(root)
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











