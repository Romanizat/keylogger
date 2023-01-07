from dhooks import Webhook, File
from requests.exceptions import HTTPError

from utils import auth

hook = None
try:
    hook = Webhook(auth.get_discord_webhook_url())
except ValueError as e:
    print(e)
    print("Please enter a valid Discord webhook url in auth.py")
except Exception as e:
    print(e)
    print("Error when trying to connect to Discord")


def send_message(message):
    try:
        hook.send(message)
    except HTTPError as ex:
        print(ex)
        print("HTTP Error when trying to send message to Discord")
    except Exception as ex:
        print(ex)
        print("Unknown Error when trying to send message to Discord")


def send_file(file_path, file_name, message):
    try:
        file = File(file_path, name=file_name)
        hook.send(message + ':', file=file)
    except FileNotFoundError as ex:
        print(ex)
        print("File not found when trying to send file to Discord")
    except HTTPError as ex:
        print(ex)
        print("HTTP Error when trying to send file to Discord")
    except Exception as ex:
        print(ex)
        print("Unknown Error when trying to send file to Discord")
