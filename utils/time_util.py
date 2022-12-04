from datetime import datetime


def now():
    return datetime.now()


def get_current_date():
    return datetime.now().strftime("%d-%m-%Y")


def get_current_time():
    return datetime.now().strftime("%H:%M:%S")


def get_current_date_and_time():
    return datetime.now().strftime("%d-%m-%Y %H:%M:%S")


def convert_date_to_date_format(date):
    return date.strftime("%d-%m-%Y")


def convert_date_to_time_format(date):
    return date.strftime("%H:%M:%S")


def convert_date_to_date_and_time_format(date):
    return date.strftime("%d-%m-%Y %H:%M:%S")
