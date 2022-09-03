from datetime import datetime, timedelta


class Data:
    data_timer_lbl = None
    data_timer_number_lbl = None
    header_timer_frame = None
    data_table_frame = None
    files_table = None
    data_table = None
    Temp_Card = None
    pressure_Card = None
    acceleration_Card = None
    ldr_panel = None
    satellite_orbit = None
    Map = None
    root = None
    start_session_time = datetime(datetime.now().year, datetime.now().month, datetime.now().day, 12, 7, 00)
    end_session_time = datetime(datetime.now().year, datetime.now().month, datetime.now().day, 12, 10, 00)
    duration_until_bext_session = timedelta(20, 20, 20)
    repeater_session = None
    execution_time = datetime(datetime.now().year, datetime.now().month, datetime.now().day, datetime.now().hour,
                              datetime.now().minute, datetime.now().second)
    server = None
    ssp = None
    received_flag = False
    data_received = None
    cv = None
    image_view = None
    current_image = None
    video_frame = None
    dataBase = None
    command_list_table = None
    long_term_table = None
    realtime_table = None
    logs_table = None
    selected_switch = 1
    command_map = []
    plot1 = None
    plot2 = None
    plot3 = None
    mission_entry = None
    files = []
    commands_frames = {}
    commands_counter = 0
    realtime_bool = False

