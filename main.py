# def get_pc_specs():
#     # Get the specs of the PC
#     return "specs"
#
#
# def send_pc_specs():
#     # Get the specs of the PC
#     specs = get_pc_specs()
#     # Send the specs to the server
#     send_to_server(specs)
from discord_util import discord

if __name__ == '__main__':
    print("Key logger started")

    # # Send PC specs of the user to the Discord server
    # send_pc_specs()

    discord.login()
    discord.create_channel("test")
    discord.send_message("Hello world")
