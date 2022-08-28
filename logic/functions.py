import json
import pandas as pd
from PIL import ImageTk, Image
from logic.data import Data
from datetime import *
from tkinter import messagebox, PhotoImage
import time
from logic.orders import *
from logic.server import Server
from logic.ssp import *


def add_new_line_table(line):
    # Data.data_table.insert(parent='', index='end', text='', values=('20:30:22', '20', '50', '30', '30,40'))
    Data.data_table.insert(parent='', index='end', text='', values=line)


def change_temp_figure(data):
    my_dict = {"Temperature": data}
    df = pd.DataFrame(data=my_dict)
    fig1 = df.plot.line(figsize=(8, 2), title="Temperature", legend="").get_figure()
    Data.Temp_Card.plot.figure = fig1
    Data.Temp_Card.plot.draw()


def change_pressure_figure(data):
    my_dict = {"Pressure": data}
    df = pd.DataFrame(data=my_dict)
    fig2 = df.plot.line(figsize=(8, 2), title="Pressure", legend="").get_figure()
    Data.pressure_Card.plot.figure = fig2
    Data.pressure_Card.plot.draw()


def change_acceleration_figure(data):
    my_dict = {"Acceleration": data}
    df = pd.DataFrame(data=my_dict)
    fig3 = df.plot.line(figsize=(8, 2), title="Acceleration", legend="").get_figure()
    Data.acceleration_Card.plot.figure = fig3
    Data.acceleration_Card.plot.draw()


def change_location(long, lat):
    Data.Map.map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga",
                                        max_zoom=22)
    Data.Map.map_widget.set_position(long, lat)
    Data.Map.map_widget.set_marker(long, lat, text="Here")


def change_text_lbl():
    if datetime.now() < Data.start_session_time:
        Data.data_timer_lbl.config(text=" Not Active Session", background="red")
        Data.duration_until_bext_session = Data.start_session_time - datetime.now()
        total_seconds = Data.duration_until_bext_session.seconds
        converted_format = time.strftime("%H:%M:%S", time.gmtime(total_seconds))
        Data.data_timer_number_lbl.config(text=converted_format, background="red")
        Data.header_timer_frame.config(background="red")

    elif datetime.now() > Data.end_session_time:
        Data.data_timer_lbl.config(text=" Not Active Session", background="red")
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
        Data.data_timer_lbl.config(text=" Active Session", background="#277BC0")
        Data.header_timer_frame.config(background="#277BC0")


def window_dispose():
    if messagebox.askokcancel("Quit", "Do you want to exit?"):
        Data.repeater_session.stop()
        # Data.server.closeConn()
        Data.server.dispose()
        Data.root.destroy()


def show_warning(title, warning):
    messagebox.showwarning(title, warning)


def start_server():
    Data.server = Server()
    Data.server.start()
    print(Data.server.connect())


def request(order, duration, atTime, angle):
    data = {
        'order': order,
        'args': {'duration': duration, 'time': atTime, 'angle': angle},
    }

    jsonData = json.dumps(data)
    print(jsonData)
    packet = Data.ssp.data2Packet(jsonData, Address.OBC, Type.Read)
    Data.server.senData(packet)
    print(packet)


def receive_fromOBC():

    arr2 = ''
    while True:
        end_text = Data.server.recieveData()

        if str(end_text).find("end of data") != -1:
            print("Found!")
            arr2 = arr2 + str(end_text).replace("end of data", "")
            break
        else:
            print("Not found!")

        arr2 = arr2 + str(end_text)

    arr = arr2.split(',')
    print(arr)
    packet = Data.ssp.packet2data(arr)
    print(packet)
    Data.data_received = packet


def capture_thread_clicked():

    request(getImageNow, "0", "0", "0")
    path = Data.server.getImage(str(datetime.now().strftime("%d-%m-%Y-%H-%M-%S")))
    Data.current_image = ImageTk.PhotoImage(Image.open(path))
    Data.image_view.config(image=Data.current_image)


def stream_thread_clicked():

    request(getStream, "0", "0", "0")
    Data.server.getVideo("output/videos/"+str(datetime.now().strftime("%d_%m_%Y %H-%M-%S") + ".avi"))


def get_telemetry():

    request(getTelemetry, "0", "0", "0")
    receive_fromOBC()

    Data.dataBase.addData(Data.data_received)

    data = Data.dataBase.getData()

    for i in Data.data_table.get_children():
        Data.data_table.delete(i)

    for i in range(data.shape[0]):
        line = (data["date"][i], data["tempreture"][i], data["pressure"][i], data["acceleration"][i],
                "X: " + str(data["angleX"][i]) + "Y: " + str(data["angleY"][i]) + "Z: " + str(data["angleZ"][i]),
                data["altitude"][i],
                "F:" + str(data["ldr1"][i]) + "B:" + str(data["ldr2"][i]) + "R:" + str(data["ldr3"][i]) + "L:" + str(
                    data["ldr4"][i]))
        add_new_line_table(line)

    last30 = Data.dataBase.getLast30()

    # change_location(last30["lang"].tolist()[0], last30["lat"].tolist()[0])
    change_acceleration_figure(last30["acceleration"].tolist())
    change_pressure_figure(last30["pressure"].tolist())
    change_temp_figure(last30["tempreture"].tolist())


def get_saved_images():

    request(getImages, "0", "0", "0")
    receive_fromOBC()

    print(Data.data_received)
    maap = json.loads(Data.data_received)
    for name in maap["imagesNames"]:
        print(name)

        path = Data.server.getImage(str(name).replace(".jpg", ""))
        Data.current_image = ImageTk.PhotoImage(Image.open(path))
        Data.image_view.config(image=Data.current_image)


def get_saved_videos():

    request(getVideos, "0", "0", "0")
    receive_fromOBC()

    print(Data.data_received)
    maap = json.loads(Data.data_received)
    for name in maap["VideosNames"]:
        Data.server.getVideo("output/videos/"+str(name))


def send_command_list():

    for task in Data.command_map:
        request(task["task"], task["duration"], task["atTime"], task["angle"])
        time.sleep(0.1)

