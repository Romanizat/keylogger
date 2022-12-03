import json

import requests

from utils import auth

header = {}
channel_id = None


def login():
    # Login to Discord
    request_url = "https://discord.com/api/v9/auth/login"
    email, password = auth.get_discord_email_and_password()
    payload = {
        "login": email,
        "password": password,
        "undelete": False,
        "captcha_key": None,
        "login_source": None,
        "gift_code_sku_id": None
    }
    response = json.loads(requests.post(request_url, json=payload).text)
    global header
    header["authorization"] = response["token"]
    print("Logged in to Discord")


def create_channel(channel_name):
    # Create channel for log session
    request_url = "https://discord.com/api/v9/guilds/1048572679583707136/channels"
    payload = {
        "name": str(channel_name),
        "parent_id": "1048572735082729482",
        "permission_overwrites": [],
        "type": 0
    }

    response = json.loads(requests.post(request_url, json=payload, headers=header).text)
    print("Created channel")
    global channel_id
    channel_id = response["id"]


def send_message(message):
    # Send message to the channel
    request_url = "https://discord.com/api/v9/channels/" + str(channel_id) + "/messages"
    payload = {
        "content": str(message),
        "tts": False
    }
    requests.post(request_url, json=payload, headers=header)
