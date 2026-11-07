import discord

import config
from bot_events import register_events

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = discord.Client(intents=intents)

register_events(bot)

if __name__ == "__main__":
    if not config.TOKEN:
        raise ValueError("Не найден DISCORD_TOKEN в файле .env")

    discord.utils.setup_logging()

    bot.run(config.TOKEN)
