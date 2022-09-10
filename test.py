import tkinter
import customtkinter
import tkintermapview


# customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
# customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
#
# app = customtkinter.CTk()  # create CTk window like you do with the Tk window
# app.geometry("400x240")
#
#
# def button_function():
#     print("button pressed")
#
#
# customtkinter.CTkTextbox().pack()
# customtkinter.CTkCanvas().pack()
# customtkinter.CTkEntry().pack()
# customtkinter.CTkFrame().pack()
# customtkinter.CTkComboBox().pack()
# customtkinter.CTkLabel(text='fsdf').pack()
# customtkinter.CTkSlider().pack()
# customtkinter.CTkProgressBar(width=200).pack()
#
# app.mainloop()


class MapCard(tkinter.Frame):
    long = 3220
    lat = 30

    def __init__(self, *args, long, lat):
        tkinter.Frame.__init__(self, *args)
        # self.value_lbl = Label(self, text=str(long)+", "+str(lat), font=("Segoe UI Light", 25), background="white",
        #                        foreground="#277BC0")

        self.map_widget = tkintermapview.TkinterMapView(self, width=500, height=900, corner_radius=10)
        #         --------- packing -----------
        self.map_widget.pack(side="bottom")

        self.map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)
        # self.map_widget.set_tile_server("https://a.tile.openstreetmap.org/{z}/{x}/{y}.png", max_zoom=22)
        self.map_widget.set_position(lat, long)
        self.map_widget.set_marker(lat, long, text="Here")


root_tk = tkinter.Tk()
root_tk.geometry(f"{800}x{600}")
root_tk.title("map_view_example.py")

frame = tkinter.Frame(root_tk)
Map = MapCard(frame, lat=30.057236, long=31.323368)

Map.pack()
frame.pack()

root_tk.mainloop()
