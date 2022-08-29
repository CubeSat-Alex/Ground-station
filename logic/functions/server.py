import json
from PIL import ImageTk, Image
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


def request(order, duration, atTime, angle, name):
    data = {
        'order': order,
        'args': {'duration': duration, 'time': atTime, 'angle': angle, 'mission': name},
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

    request(getImageNow, "0", "0", "0", "none")
    path = Data.server.getImage(str(datetime.now().strftime("%d-%m-%Y-%H-%M-%S")))
    Data.current_image = ImageTk.PhotoImage(Image.open(path))
    Data.image_view.config(image=Data.current_image)


def stream_thread_clicked():

    request(getStream, "0", "0", "0", "none")
    Data.server.getVideo("output/videos/"+str(datetime.now().strftime("%d_%m_%Y %H-%M-%S") + ".avi"))


def stream_phone_thread_clicked():

    request('z', "0", "0", "0", "none")
    Data.server.getVideo("output/videos/"+str(datetime.now().strftime("%d_%m_%Y %H-%M-%S") + ".avi"))


def get_telemetry():

    request(getTelemetry, "0", "0", "0", "none")
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

    request(getImages, "0", "0", "0", 'none')
    receive_fromOBC()

    print(Data.data_received)
    maap = json.loads(Data.data_received)
    for name in maap["imagesNames"]:
        print(name)

        path = Data.server.getImage(str(name).replace(".jpg", ""))
        Data.current_image = ImageTk.PhotoImage(Image.open(path))
        Data.image_view.config(image=Data.current_image)


def get_saved_videos():

    request(getVideos, "0", "0", "0", "none")
    receive_fromOBC()

    print(Data.data_received)
    maap = json.loads(Data.data_received)
    for name in maap["VideosNames"]:
        Data.server.getVideo("output/videos/"+str(name))


def send_command_list():

    for task in Data.command_map:
        request(task["task"], task["duration"], task["atTime"], task["angle"], task["name"])
        time.sleep(0.1)

