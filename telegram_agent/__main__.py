import os
from .agent import TelegramAgent

def main():
    bot_token = os.environ.get("TELEGRAM_BOT_TOKEN")
    channel_name = os.environ.get("TELEGRAM_CHANNEL_NAME")

    if not bot_token or not channel_name:
        print("Error: Please set the TELEGRAM_BOT_TOKEN and TELEGRAM_CHANNEL_NAME environment variables.")
        return

    agent = TelegramAgent(bot_token, channel_name)
    agent.run()

if __name__ == "__main__":
    main()
