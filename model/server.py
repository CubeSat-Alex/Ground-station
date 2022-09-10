import _thread
import json
import pickle
import socket
import struct
from datetime import datetime
from threading import Timer

from logic.constant.orders import Orders
from logic.data import Data
from model.ssp import *


class Server:
    ip = "192.168.43.103"
    port = 5005

    def __init__(self):
        self.image_on_canvas = None
        self.photo = None
        self.serverSocket = socket.socket()

    def start(self):
        self.serverSocket.bind((self.ip, self.port))
        self.serverSocket.listen(2)

    def connect(self):
        (self.client, clientAddress) = self.serverSocket.accept()
        return clientAddress

    def recieveData(self):
        try:
            dataFromClient = self.client.recv(4*1024)
            return dataFromClient.decode()
        except:
            return 0

    def senData(self, data):
        Data.timer.cancel()
        try:
            self.client.send(','.join([str(elem).strip() for elem in data]).encode())
            print("SEND SUCCESSFULLY")
        except:
            print("NOT SENT")
            # _thread.start_new_thread(self.reconnect, ())
        Data.timer = Timer(2, Data.server.bicon)
        Data.timer.start()

    def bicon(self):

        data = {
            'order': Orders.ping,
            'args': {},
        }
        jsonData = json.dumps(data)
        print(jsonData)
        packet = Data.ssp.data2Packet(jsonData, Address.OBC, Type.Read)

        try:
            self.client.send(','.join([str(elem).strip() for elem in packet]).encode())
            print("connection is a live")
        except:
            print("reconnecting in process")
            self.connect()

        Data.timer = Timer(2, Data.server.bicon)
        Data.timer.start()

    def getVideo(self, fileName, stream):
        print('in get videos')

        data = b""
        payload_size = struct.calcsize("Q")
        fourcc = Data.cv.VideoWriter_fourcc(*'XVID')
        out = Data.cv.VideoWriter(fileName, fourcc, 24.0, (320, 240))

        frames_counter = 0

        while True:
            while len(data) < payload_size:
                packet = self.client.recv(4 * 1024)  # 4K
                if not packet:
                    break
                data += packet
            packed_msg_size = data[:payload_size]
            data = data[payload_size:]
            msg_size = struct.unpack("Q", packed_msg_size)[0]

            while len(data) < msg_size:
                newData = self.client.recv(4 * 1024)
                data += newData

            frame_data = data[:msg_size]
            data = data[msg_size:]
            if len(data) < payload_size:
                print("here")
                out.release()
                Data.cv.destroyAllWindows()
                break

            # frame = Data.cv.cvtColor(pickle.loads(frame_data), Data.cv.COLOR_BGR2RGB)

            frames_counter = frames_counter + 1
            print(f' time : {datetime.now()}, frame : {frames_counter}')
            frame = pickle.loads(frame_data)

            out.write(frame)

            # self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
            # canvas.itemconfig(self.image_on_canvas, image=self.photo)

            if stream:
                Data.cv.imshow("RECEIVING VIDEO", frame)
            Data.cv.waitKey(1)


    def getImage(self, name):
        Data.timer.cancel()

        data = b""
        payload_size = struct.calcsize("Q")
        while len(data) < payload_size:
            packet = self.client.recv(4 * 1024)  # 4K
            if not packet:
                break
            data += packet
        packed_msg_size = data[:payload_size]
        data = data[payload_size:]
        msg_size = struct.unpack("Q", packed_msg_size)[0]

        while len(data) < msg_size:
            newData = self.client.recv(4 * 1024)
            data += newData

        frame_data = data[:msg_size]
        data = data[msg_size:]
        if len(data) < payload_size:
            print("rr")
        frame = pickle.loads(frame_data)
        path = "output/images/" + name + ".png"
        print(path)
        Data.cv.imwrite(path, frame)

        Data.timer = Timer(2, Data.server.bicon)
        Data.timer.start()

        return path

    def closeConn(self):
        self.client.close()

    def dispose(self):
        self.serverSocket.close()

