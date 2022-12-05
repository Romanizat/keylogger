from dhooks import Webhook, File

from utils import auth

hook = Webhook(auth.get_discord_webhook_url())


def send_message(message):
    hook.send(message)


def send_file(file_path, file_name):
    file = File(file_path, name=file_name)
    hook.send('New logs:', file=file)
