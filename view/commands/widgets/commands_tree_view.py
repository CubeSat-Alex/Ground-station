from tkinter import *
from tkinter.ttk import Treeview, Style
from logic.data import Data
from logic.functions.general import change_command_frame


class TreeView(Frame):

    def __init__(self, *args):
        Frame.__init__(self, *args, borderwidth=10, highlightbackground="black", highlightthickness=0.2,
                       background="white")

        style = Style()
        style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Calibri', 11))
        style.configure("mystyle.Treeview.Heading", font=('Calibri', 14, 'bold'))
        style.configure("mystyle.Treeview", font=('Calibri', 15))
        style.configure("mystyle.Treeview", rowheight=30)
        style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])

        # create a treeview
        self.tree = Treeview(self, style="mystyle.Treeview", height=400, selectmode="extended")
        self.fill_tree(self.tree)
        self.tree.bind("<Double-1>", self.OnDoubleClick)
        self.tree.pack(ipady=50, fill='y')

    def OnDoubleClick(self, event):
        item = self.tree.identify('item', event.x, event.y)
        page = self.tree.item(item, "text")

        if page == "set on board time":
            change_command_frame("SetOnBoardTimeFrame")
        elif page == "set Session time":
            change_command_frame("SetSessionTimeFrame")
        elif page == "get time difference":
            change_command_frame("GetTimeDifferenceFrame")
        elif page == "ADCS":
            change_command_frame("ADCSFrame")
        elif page == "Telemetry":
            change_command_frame("GPSFrame")
        elif page == "real time":
            change_command_frame("OpenRealTimeFrame")
        elif page == "delete telemetry":
            change_command_frame("DeleteTelemetryFrame")
        elif page == "telemetry":
            change_command_frame("GETTelemetryFrame")
        elif page == "take image":
            change_command_frame("TakeImageFrame")
        elif page == "take video":
            change_command_frame("TakeVideoFrame")
        elif page == "Payload":
            change_command_frame("DownloadsFrame")
        elif page == "logs":
            change_command_frame("LogsFrame")

    def fill_tree(self, tree):
        tree.heading('#0', text='Commands', anchor=W)
        tree.column("#0", width=300)
        # adding data
        tree.insert('', END, text='Direct', open=True, iid='direct')
        tree.insert('', END, text='Play Back', open=True, iid='play-back')
        tree.insert('', END, text='Mission', open=True, iid='mission')
        tree.insert('', END, text='Download', open=True, iid='download')
        tree.insert('', END, text='Logs', open=True, iid='logs')

        # adding children direct
        tree.insert('', END, text='get time difference', open=False, iid='getTime')
        tree.insert('', END, text='set on board time', open=False, iid='setOnBoardTime')
        tree.insert('', END, text='set Session time', open=False, iid='setSessionTime')
        tree.insert('', END, text='subsystems', open=False, iid='control-sub')
        # tree.insert('', END, text='getSubsystemStatus', open=False, iid='get-sub-status')
        tree.insert('', END, text='real time', open=False, iid='open-real')

        tree.insert('', END, text='ADCS', open=False, iid='ADCS')
        tree.insert('', END, text='Telemetry', open=False, iid='GPS')

        tree.move('getTime', 'direct', 0)
        tree.move('setOnBoardTime', 'direct', 1)
        tree.move('setSessionTime', 'direct', 2)
        tree.move('control-sub', 'direct', 3)
        # tree.move('get-sub-status', 'direct', 3)
        tree.move('open-real', 'direct', 4)

        tree.move('ADCS', 'control-sub', 0)
        tree.move('GPS', 'control-sub', 1)

        # adding children play back
        tree.insert('', END, text='telemetry', open=False, iid='get_telemetry')

        tree.move('get_telemetry', 'play-back', 0)

        # adding children mission
        tree.insert('', END, text='take image', open=False, iid='take_image')
        tree.insert('', END, text='take video', open=False, iid='take_video')

        tree.move('take_image', 'mission', 0)
        tree.move('take_video', 'mission', 1)

        # adding children download
        tree.insert('', END, text='Payload', open=False, iid='files')
        tree.move('files', 'download', 0)

        # adding children logs
        tree.insert('', END, text='logs', open=False, iid='get-logs')

        tree.move('get-logs', 'logs', 0)
