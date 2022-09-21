import _thread
from tkinter import *
from tkinter.ttk import Treeview, Style
from logic.functions.server import *
import customtkinter


class CommandsListFrame(Frame):

    def __init__(self, *args):
        Frame.__init__(self, *args, background="#1f6aa5")

        table_frame = customtkinter.CTkFrame(self, bg='red', border_width=0, borderwidth=2)
        table_frame.pack(side='top', fill='x')

        style = Style()
        style.configure("mystyle.Treeview", highlightthickness=1, bd=1, font=('Calibri', 13))
        style.configure("mystyle.Treeview.Heading", font=('Calibri', 13, 'bold'))

        Data.command_list_table = Treeview(table_frame,
                                           style="mystyle.Treeview",
                                           height=12)

        Data.command_list_table['columns'] = ('ID', 'Command', 'Execution', 'name', 'arguments')

        Data.command_list_table.column("#0", width=0)
        Data.command_list_table.column("ID", width=20)
        Data.command_list_table.column("Command", width=150)
        Data.command_list_table.column("Execution", width=150)
        Data.command_list_table.column("name", width=150)
        Data.command_list_table.column("arguments", width=200)

        Data.command_list_table.heading("#0", text="", anchor=CENTER)
        Data.command_list_table.heading("ID", text="ID", anchor=CENTER)
        Data.command_list_table.heading("Command", text="Command", anchor=CENTER)
        Data.command_list_table.heading("Execution", text="Listing Time", anchor=CENTER)
        Data.command_list_table.heading("name", text="Mission name", anchor=CENTER)
        Data.command_list_table.heading("arguments", text="Arguments", anchor=CENTER)

        Data.command_list_table.pack(fill='x', expand=1)

        btn = customtkinter.CTkButton(self, text=' Send ', text_font=('', 16),
                     command=self.buttonClick)
        btn.pack(side='bottom', fill='x')

    def buttonClick(self):
        _thread.start_new_thread(self.send_commands, ())

    def realtime_communication(self):
        print('real time open')
        print(Data.realtime_bool_temp)
        print(int(Data.realtime_duration) * 1000)
        if Data.realtime_bool_temp:
            request(Orders.openRealTime, '0')
            try:
                receive_fromOBC()
            except:
                # if Data.realtime_bool:
                #     self.after(int(Data.realtime_duration) * 1000, self.realtime_communication)
                return
            st = json.loads(str(Data.data_received).strip())

            temp = str(st['TT']['T'])
            pressure = str(st['TT']['P'])
            acceleration = str(st['ADCS']['A'])
            angle = str(int(float(str(st['ADCS']['Z']))))  # + ', ' + str(st['ADCS']['Y']
            altitude = str(st['TT']['A'])

            ldr1 = str(st['TT']['LDR1'])
            ldr2 = str(st['TT']['LDR2'])
            ldr3 = str(st['TT']['LDR3'])
            ldr4 = str(st['TT']['LDR4'])

            Data.realtime_table.insert(parent='', index='end', text='', values=(
                datetime.now().strftime(time_format), temp, pressure, acceleration, angle, altitude, ldr1, ldr2, ldr3, ldr4
            ))

        if Data.realtime_bool:
            self.after(int(Data.realtime_duration) * 1000, self.realtime_communication)

    def send_commands(self):

        for req in Data.all_requests:

            if req["order"] != Orders.openRealTime and req["order"] != 'close':

                Data.overlay_lbl.config(text='Current Status : '+self.get_order_name(req["order"]))

                request(req["order"],
                        req['atTime'],
                        duration=req['duration'],
                        x=req['x'], y=req['y'],
                        name=req['name'],
                        command=req['command'],
                        sys=req['sys'],
                        start=req['start'],
                        end=req['end'])

            if req["order"] == Orders.getTime:
                time_to_send = datetime.now()
                receive_fromOBC()
                print(Data.data_received)
                obcDate = datetime.strptime(Data.data_received[1:-1], time_format)
                print(obcDate)
                difference = time_to_send - obcDate
                print(difference.total_seconds())
                messagebox.showinfo("time difference", 'time difference is \n' + str(difference.total_seconds()) + " S")

            elif req["order"] == Orders.getStorage:
                receive_fromOBC()
                jsn = json.loads(Data.data_received)

                image_size = str(int(jsn['Images']) / 1000) + ' KB' if jsn['Images'] < 1000000 else str(
                    int(jsn['Images']) / 1000000) + ' MB'
                video_size = str(int(jsn['Videos']) / 1000) + ' KB' if jsn['Videos'] < 1000000 else str(
                    int(jsn['Videos']) / 1000000) + ' MB'
                telemetry_size = str(int(jsn['Telemtry']) / 1000) + ' KB' if jsn['Telemtry'] < 1000000 else str(
                    int(jsn['Telemtry']) / 1000000) + ' MB'
                logs_size = str(int(jsn['Logs']) / 1000) + ' KB' if jsn['Logs'] < 1000000 else str(
                    int(jsn['Logs']) / 1000000) + ' MB'

                Data.image_lbl_var.config(text=image_size)
                Data.videos_lbl_var.config(text=video_size)
                Data.telemetry_var.config(text=telemetry_size)
                Data.logs_lbl_var.config(text=logs_size)

                Data.image_prog.config(value=int(int(jsn['Images']) / 1000000000))
                Data.videos_prog.config(value=int(int(jsn['Videos']) / 1000000000))
                Data.telemetry_prog.config(value=int(int(jsn['Telemtry']) / 1000000000))
                Data.logs_prog.config(value=int(int(jsn['Logs']) / 1000000000))

                for key, value in jsn.items():
                    Data.cache.add(key, value)

            elif req["order"] == Orders.openRealTime:

                Data.overlay_lbl.config(text='Current Status : '+self.get_order_name(req["order"]))

                Data.realtime_bool = True
                Data.realtime_bool_temp = True
                try:
                    Data.timer.cancel()
                except:
                    pass

                _thread.start_new_thread(self.realtime_communication, ())

            elif req["order"] == 'close':
                Data.realtime_bool = False
                # Data.timer = Timer(2, Data.server.bicon)
                # Data.timer.start()
                Data.overlay_lbl.config(text='Current Status : closing real time data')

            elif req["order"] == Orders.getVideos:
                Data.timer.cancel()
                Data.realtime_bool_temp = False
                get_saved_videos()
                Data.timer = Timer(2, Data.server.bicon)
                Data.timer.start()
                Data.realtime_bool_temp = True

            elif req["order"] == Orders.getImages:
                Data.timer.cancel()
                Data.realtime_bool_temp = False
                get_saved_images()
                Data.timer = Timer(2, Data.server.bicon)
                Data.timer.start()
                Data.realtime_bool_temp = True

            elif req["order"] == Orders.getLogs:
                print('inside get logs')
                Data.timer.cancel()
                Data.realtime_bool_temp = False
                receive_fromOBC()
                Data.dataBase.addLogs(Data.data_received)
                print('adding to table')
                self.add_to_table()
                Data.timer = Timer(2, Data.server.bicon)
                Data.timer.start()
                Data.realtime_bool_temp = True

            elif req["order"] == Orders.getTelemetry:
                Data.timer.cancel()
                Data.realtime_bool_temp = False
                get_telemetry()
                Data.timer = Timer(2, Data.server.bicon)
                Data.timer.start()
                Data.realtime_bool_temp = True

            time.sleep(3)

        Data.all_requests.clear()
        Data.commands_counter = 0
        Data.command_list_table.delete(*Data.command_list_table.get_children())
        Data.overlay_lbl.config(text='Ready')

    def add_to_table(self):
        jsn = Data.dataBase.getLogs()
        print(jsn)

        for i in Data.logs_table.get_children():
            Data.logs_table.delete(i)

        for i in range(jsn.shape[0]):
            orbit_num = jsn["orbit"][i]
            command = jsn["details"][i]
            time = jsn["date"][i]
            status = jsn["state"][i]

            Data.logs_table.insert(parent='', index='end', text='', values=(
                orbit_num, command, time, status
            ))

    def get_order_name(self, char):
        if char == 'd':
            return 'get Time'
        elif char == 'e':
            return 'set on board time'
        elif char == 'g':
            return 'controlSubsystem'
        elif char == 'h':
            return 'getSubsystemStatus'
        elif char == 'i':
            return 'openRealTime'
        elif char == 'i':
            return 'setNextSession'
        elif char == 'l':
            return 'getTelemetry'
        elif char == 'p':
            return 'getImages'
        elif char == 'q':
            return 'getVideos'
        elif char == 'm':
            return 'deleteTelemetry'
        elif char == 's':
            return 'deleteVideos'
        elif char == 'r':
            return 'deleteImages'
        elif char == 'j':
            return 'takeVideo'
        elif char == 'k':
            return 'takeImage'
        elif char == 'b':
            return 'getStream'
        elif char == 'c':
            return 'stopStream'
        elif char == 'a':
            return 'capture'
        elif char == 'n':
            return 'getLogs'
        elif char == 'o':
            return 'deleteLogs'
        elif char == 't':
            return 'getStorage'
        elif char == 'u':
            return 'ping'
