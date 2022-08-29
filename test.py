from tkinter import *
from ldr_panel import LDRPanel
from logic.functions import *

root = Tk()
root.wm_geometry("1600x900+180+50")
root.title('Cube Satellite Station')
root.config(bg="#002B5B")
root.iconbitmap('images/satelite.ico')
root.minsize(600, 600)
root.wm_attributes('-transparentcolor', '#add123')
root.protocol("WM_DELETE_WINDOW", window_dispose)

satellite_orbit = LDRPanel(root)
satellite_orbit.pack()

root.mainloop()



