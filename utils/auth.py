def get_discord_token():
    with open("credentials.txt", "r") as credentials_file:
        credentials = credentials_file.readlines()
        try:
            return credentials[0]
        except IndexError:
            print("Discord token not found")
            return None
