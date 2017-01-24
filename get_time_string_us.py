import datetime

def get_time_str_us():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
