import telegram

class TelegramAgent:
    def __init__(self, bot_token, channel_name):
        self.bot_token = bot_token
        self.channel_name = channel_name
        self.bot = telegram.Bot(token=self.bot_token)

    def run(self):
        """
        Reads messages from the specified Telegram channel.
        """
        updates = self.bot.get_updates()
        for update in updates:
            if update.channel_post:
                print(f"Message from {update.channel_post.chat.title}: {update.channel_post.text}")
