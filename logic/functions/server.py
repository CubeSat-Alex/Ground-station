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
    Data.server.bicon()


def add_request(order,
    atTime,
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


def request(order, atTime = datetime.now().strftime(time_format),
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
                 'requestTime': datetime.now().strftime(time_format),
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
    print(data['order'])
    packet = Data.ssp.data2Packet(jsonData, Address.OBC, Type.Read)
    Data.server.senData(packet)
    # print(packet)


def receive_fromOBC():

    # Data.realtime_bool_temp = False
    arr2 = ''
    # break_counter = 0
    while True:
        end_text = Data.server.recieveData()
        print(end_text)

        if str(end_text).find("end of data") != -1:
            print("Found!")
            arr2 = arr2 + str(end_text).replace("end of data", "")
            break
        else:
            print("Not found!")
            # break_counter = break_counter + 1
            # if break_counter > 20 :
            #     break

        arr2 = arr2 + str(end_text)

    arr = arr2.split(',')
    packet = Data.ssp.packet2data(arr)
    print(packet)
    Data.data_received = packet
    # Data.realtime_bool_temp = True


def capture_thread_clicked():

    request(Orders.capture, "0")
    path = Data.server.getImage(str(datetime.now().strftime('%d-%m-%Y-%H-%M-%S')), save=False)
    Data.current_image = ImageTk.PhotoImage(Image.open(path).resize((1000, 1000)))
    Data.image_view.config(image=Data.current_image)


def stream_thread_clicked():

    Data.timer.cancel()
    Data.realtime_bool_temp = False

    request(Orders.getStream, "0")
    Data.server.getVideo("output/videos/"+str(datetime.now().strftime(time_format) + ".avi"), True)

    Data.timer = Timer(2, Data.server.bicon)
    Data.timer.start()
    Data.realtime_bool_temp = True


def stream_phone_thread_clicked():

    Data.timer.cancel()

    request(Orders.getStream, "0")
    Data.server.getVideo("output/videos/"+str(datetime.now().strftime(time_format) + ".avi"))

    Data.timer = Timer(2, Data.server.bicon)
    Data.timer.start()


def get_telemetry():

    receive_fromOBC()
    time_1 = datetime.now()

    if Data.data_received == '{}':
        return

    Data.dataBase.addData(Data.data_received)

    data = Data.dataBase.getData()
    time_2 = datetime.now() - time_1
    print(time_2.total_seconds())

    for i in Data.data_table.get_children():
        Data.data_table.delete(i)

    for i in range(data.shape[0]):
        date_parts = str(data["date"][i]).split('-')
        line = (date_parts[0].replace('/', '-')+'\n   '+date_parts[1].replace('.', ':'),
                data["tempreture"][i], data["pressure"][i], data["acceleration"][i],
                "X: " + str(data["angleX"][i])
                    + "\nY: " + str(data["angleY"][i])
                    + "\nZ: " + str(data["angleZ"][i]),
                data["altitude"][i],
                "F:" + str(data["ldr1"][i])
                    + ",  B:" + str(data["ldr2"][i])
                    + "\nR:" + str(data["ldr3"][i])
                    + ",  L:" + str(data["ldr4"][i]))

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

    Data.timer.cancel()
    Data.realtime_bool_temp = False

    receive_fromOBC()
    print(Data.data_received)

    maap = json.loads(Data.data_received)
    print(maap)

    for name in maap["VideosNames"]:
        print(name)
        Data.server.getVideo("output/videos/"+str(name), False)

    videos = getAllNames(videosFolder)
    images = getAllNames(imageFolder)
    Data.files = images + videos
    fill_table()

    Data.timer = Timer(2, Data.server.bicon)
    Data.timer.start()
    Data.realtime_bool_temp = True


def send_command_list():

    for task in Data.command_map:
        request(task["task"], task["duration"], task["atTime"], task["angle"], task["name"])
        time.sleep(0.1)

