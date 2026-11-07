import random
import discord
import config
import database
from ui_components import CakeButton


async def send_cake_greeting(
    channel: discord.TextChannel, target_member: discord.Member
):
    """Функция отправки торта"""

    if not config.GIFS:
        await channel.send("У меня закончились торты! 🎂")
        return

    greeting = random.choice(config.GREETINGS)
    gif = random.choice(config.GIFS)
    text = greeting.format(name=target_member.mention)
    view = CakeButton(target_member)

    await channel.send(
        content=text,
        file=discord.File(gif),
        view=view
    )


def register_events(bot: discord.Client):
    """Регистрация всех обработчиков событий для бота."""

    @bot.event
    async def on_ready():
        print(f"Бот запущен: {bot.user}")

    @bot.event
    async def on_member_join(member):
        channel_id = database.get_welcome_channel(member.guild.id)
        channel = bot.get_channel(channel_id)

        if channel is None:
            print(
                f"На сервере '{member.guild.name}' "
                f"еще не настроен канал приветствий."
            )
            return

        await send_cake_greeting(
            channel,
            target_member=member
        )
        print(f"Приветствуем {member.name}!")

    @bot.event
    async def on_message(message):
        if message.author.bot:
            return

        if message.content.lower() == "!настроить":
            if not message.author.guild_permissions.administrator:
                await message.channel.send(
                    "Эту команду могут использовать "
                    "только администраторы сервера! ❌"
                )
                return

            database.save_welcome_channel(message.guild.id, message.channel.id)
            await message.channel.send(
                f"Успешно! Теперь торты будут прилетать "
                f"в канал {message.channel.mention} 🎉"
            )
            return

        if message.content.lower() == "!торт":
            await send_cake_greeting(
                message.channel,
                target_member=message.author
            )
