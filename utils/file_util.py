import json
import os
import sys

from classes import Host


def get_file_size(file_name):
    return os.path.getsize(file_name) / 1000000.0


def get_object_size(obj):
    return sys.getsizeof(obj) / 1000000.0


def write_keys_to_file(keys: dict, file_name: str, host: Host):
    with open(file_name, "w") as file:
        dict_to_write = {
            "host": host.to_json(),
            "keys": keys
        }
        json.dump(dict_to_write, file)
