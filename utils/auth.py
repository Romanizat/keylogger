def get_discord_email_and_password():
    with open("credentials.txt", "r") as credentials_file:
        credentials = credentials_file.readlines()
        try:
            return credentials[1], credentials[3]
        except IndexError:
            print("Discord credentials not found")
            return None, None
