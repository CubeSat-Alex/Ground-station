from tkinter import *
import ctypes as ct
from logic.functions.general import window_dispose, initial_setup
from view.main_view import MainView

# version
def dark_title_bar(window):
    window.update()
    DWMWA_USE_IMMERSIVE_DARK_MODE = 20
    set_window_attribute = ct.windll.dwmapi.DwmSetWindowAttribute
    get_parent = ct.windll.user32.GetParent
    hwnd = get_parent(window.winfo_id())
    rendering_policy = DWMWA_USE_IMMERSIVE_DARK_MODE
    value = 2
    value = ct.c_int(value)
    set_window_attribute(hwnd, rendering_policy, ct.byref(value),
                         ct.sizeof(value))


root = Tk()
initial_setup(root)
main = MainView(root)
main.pack(side="top", fill="both", expand=True)
# root.wm_geometry("1600x900+180+50")
root.state('zoomed')
root.title('Cube Satellite Station')
root.config(bg="#002B5B")
root.iconbitmap('images/satelite.ico')
root.minsize(600, 600)
root.wm_attributes('-transparentcolor', '#add123')
root.protocol("WM_DELETE_WINDOW", window_dispose)
dark_title_bar(root)
root.mainloop()











