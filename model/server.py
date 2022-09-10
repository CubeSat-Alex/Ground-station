import pickle
import socket
import struct
from logic.data import Data


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
        try:
            self.client.send(','.join([str(elem).strip() for elem in data]).encode())
            print("SEND SUCCESSFULLY")

        except:
            print("NOT SENT")

    def getVideo(self, fileName):
        data = b""
        payload_size = struct.calcsize("Q")
        fourcc = Data.cv.VideoWriter_fourcc(*'XVID')
        out = Data.cv.VideoWriter(fileName, fourcc, 24.0, (320, 240))

        frames_counter = 0

        while True:
            while len(data) < payload_size:
                packet = self.client.recv(64 * 1024)  # 4K
                if not packet:
                    break
                data += packet
            packed_msg_size = data[:payload_size]
            data = data[payload_size:]
            msg_size = struct.unpack("Q", packed_msg_size)[0]

            while len(data) < msg_size:
                newData = self.client.recv(64 * 1024)
                data += newData

            frame_data = data[:msg_size]
            data = data[msg_size:]
            if len(data) < payload_size:
                print("here")
                out.release()
                Data.cv.destroyAllWindows()
                break

            # frame = Data.cv.cvtColor(pickle.loads(frame_data), Data.cv.COLOR_BGR2RGB)
            frame = pickle.loads(frame_data)

            frames_counter = frames_counter + 1

            out.write(frame)

            # self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
            # canvas.itemconfig(self.image_on_canvas, image=self.photo)

            # Data.cv.imshow("RECEIVING VIDEO", frame)
            Data.cv.waitKey(1)

        print('frames : ')
        print(frames_counter)

    def getImage(self, name):
        data = b""
        payload_size = struct.calcsize("Q")
        while len(data) < payload_size:
            packet = self.client.recv(4 * 1024)  # 4K
            if not packet: break
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
        return path

    def closeConn(self):
        self.client.close()

    def dispose(self):
        self.serverSocket.close()

# server = Server()
# server.start()
# address = server.connect()

# server.getImage()
