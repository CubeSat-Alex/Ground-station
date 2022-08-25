from datetime import datetime, timedelta


class Data:
    data_timer_lbl = None
    data_timer_number_lbl = None
    header_timer_frame = None
    data_table_frame = None
    data_table = None
    Temp_Card = None
    pressure_Card = None
    acceleration_Card = None
    Map = None
    root = None
    start_session_time = datetime(2022, 8, 24, 12, 7, 00)
    end_session_time = datetime(2022, 8, 24, 12, 8, 00)
    duration_until_bext_session = timedelta(20, 20, 20)
    repeater_session = None
    execution_time = datetime(2022, 8, 24, 4, 12, 00)
    server = None
    ssp = None
    received_flag = False
    data_received = None
    cv = None
    image_view = None
    current_image = None
    video_frame = None
    dataBase = None
    selected_switch = 1

