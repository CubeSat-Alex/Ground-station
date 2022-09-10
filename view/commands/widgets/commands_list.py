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
        Data.command_list_table.heading("Execution", text="Upload Time", anchor=CENTER)
        Data.command_list_table.heading("name", text="Mission name", anchor=CENTER)
        Data.command_list_table.heading("arguments", text="Arguments", anchor=CENTER)

        # Data.command_list_table.insert(parent='', index='end', text='', values=(
        #     "1", "take image", datetime.now(), "alex", "angle: 30,60"
        # ))
        # Data.command_list_table.insert(parent='', index='end', text='', values=(
        #     "2", "take video", datetime.now(), "alex", "angle: 30,60 , duration : 3 min"
        # ))

        Data.command_list_table.pack(fill='x', expand=1)

        btn = customtkinter.CTkButton(self, text=' Send ', text_font=('', 16),
                     command=lambda: _thread.start_new_thread(self.send_commands, ()))
        btn.pack(side='bottom', fill='x')

    def send_commands(self):
        for req in Data.all_requests:
            request(req["order"], req['atTime'],
                    duration=req['duration'],
                    x=req['x'], y=req['y'],
                    name=req['name'],
                    command=req['command'],
                    sys=req['sys'],
                    start=req['start'],
                    end=req['end'])

            if req["order"] == Orders.getTime:
                receive_fromOBC()
                print(Data.data_received)

                obcDate = datetime.strptime(Data.data_received[1:-1], time_format)

                print(obcDate)
                difference = datetime.now() - obcDate
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

            elif req["order"] == Orders.getVideos:
                get_saved_videos()

            elif req["order"] == Orders.getImages:
                get_saved_images()

            elif req["order"] == Orders.getImages:
                receive_fromOBC()
                Data.dataBase.addLogs(Data.data_received)
                self.add_to_table()

            elif req["order"] == Orders.getTelemetry:
                get_telemetry()

        Data.all_requests.clear()
        Data.command_list_table.delete(*Data.command_list_table.get_children())

    def add_to_table(self):
        jsn = Data.dataBase.getLogs()

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

