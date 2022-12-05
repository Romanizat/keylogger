def get_discord_webhook_url():
    with open("credentials.txt", "r") as credentials_file:
        credentials = credentials_file.readlines()
        try:
            return credentials[0]
        except IndexError:
            print("Discord webhoook not found")
            return None
