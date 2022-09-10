import json
from PIL import ImageTk, Image
from logic.constant.constants import time_format
from logic.functions.figures import *
from logic.functions.general import *
from model.gallery_logic import *
from logic.constant.orders import *
from model.server import Server
from model.ssp import *
from datetime import datetime


def start_server():
    Data.server = Server()
    Data.server.start()
    print(Data.server.connect())


def add_request(order, atTime,
     duration="0",
    x=0, y=0,
    name="none",
    command='none',
    sys="none",
    start='0', end=0):

    req = {'order': order,
           'atTime': atTime,
           'duration': duration,
           'x': x,
           'y': y,
           'name': name,
           'command': command,
           'sys': sys,
           'start': start,
           'end': end}

    Data.all_requests.append(req)
    # { order, atTime,
    #  duration="0",
    # x=0, y=0,
    # name="none",
    # command='none',
    # sys="none",
    # start='0', end=0 }


def request(order, atTime,
            duration="0",
            x=0, y=0,
            name="none",
            command='none',
            sys="none",
            start='0', end=0
            ):

    data = {
        'order': order,
        'args': {'duration': duration,
                 'time': atTime,
                 'mission': name,
                 "sys": sys,
                 'command': command,
                 'X': x,
                 'Y': y,
                 'start': start,
                 'end': end},
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

    request(Orders.capture, "0")
    path = Data.server.getImage(str(datetime.now().strftime(time_format)))
    Data.current_image = ImageTk.PhotoImage(Image.open(path))
    Data.image_view.config(image=Data.current_image)


def stream_thread_clicked():

    request(Orders.getStream, "0")
    Data.server.getVideo("output/videos/"+str(datetime.now().strftime(time_format) + ".avi"))


def stream_phone_thread_clicked():

    request(Orders.getStream, "0")
    Data.server.getVideo("output/videos/"+str(datetime.now().strftime(time_format) + ".avi"))


def get_telemetry():

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

        Data.data_table.insert(parent='', index='end', text='', values=line)

    last30 = Data.dataBase.getLast30()

    # change_location(last30["lang"].tolist()[0], last30["lat"].tolist()[0])
    change_acceleration_figure(last30["acceleration"].tolist())
    change_pressure_figure(last30["pressure"].tolist())
    change_temp_figure(last30["tempreture"].tolist())


def fill_table():
    for i in Data.files_table.get_children():
        Data.files_table.delete(i)

    for i in range(len(Data.files)):
        line = (Data.files[i].date,
                Data.files[i].mission,
                'video' if str(Data.files[i].path).find('.avi') != -1 else 'image',
                Data.files[i].x + ", " + Data.files[i].y,
                Data.files[i].duration)

        Data.files_table.insert(parent='', index='end', text=Data.files[i].path, values=line)


def get_saved_images():

    receive_fromOBC()

    print(Data.data_received)
    maap = json.loads(Data.data_received)
    for name in maap["imagesNames"]:
        path = Data.server.getImage(str(name).replace(".jpg", ""))
        Data.current_image = ImageTk.PhotoImage(Image.open(path))
        Data.image_view.config(image=Data.current_image)

    videos = getAllNames(videosFolder)
    images = getAllNames(imageFolder)
    Data.files = images + videos
    fill_table()


def get_saved_videos():

    receive_fromOBC()

    print(Data.data_received)
    maap = json.loads(Data.data_received)
    for name in maap["VideosNames"]:
        Data.server.getVideo("output/videos/"+str(name))

    videos = getAllNames(videosFolder)
    images = getAllNames(imageFolder)
    Data.files = images + videos
    fill_table()


def send_command_list():

    for task in Data.command_map:
        request(task["task"], task["duration"], task["atTime"], task["angle"], task["name"])
        time.sleep(0.1)

