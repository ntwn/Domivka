import time


def date_time_to_unix():
    return time.time()


def unix_time_to_data(unix_time):
    return time.strftime("%d.%m.%Y %H:%M:%S", time.gmtime(unix_time))
