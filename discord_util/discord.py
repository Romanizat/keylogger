import requests

from utils import auth

header = {
    'authorization': auth.get_discord_token()
}


def create_channel():
    # Create channel for log session and send info about PC specs
    request_url = "https://discord.com/api/v9/guilds/1048572679583707136/channels"
    payload = {
        "name": "test2",
        "parent_id": "1048572735082729482",
        "permission_overwrites": [],
        "type": 0
    }

    return requests.post(request_url, json=payload, headers=header)
