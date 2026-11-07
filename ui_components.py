import random

import discord

import config


class CakeButton(discord.ui.View):
    """Класс интерфейса, содержащий кнопку для броска торта."""

    def __init__(self, new_member):
        super().__init__(timeout=config.BUTTON_TIMEOUT)
        self.new_member = new_member

    @discord.ui.button(
        label="Кинуть тортом!", emoji="🍰", style=discord.ButtonStyle.primary
    )
    async def throw_cake(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        if not config.GIFS:
            await interaction.response.send_message("Торты закончились! 😭")
            return

        gif = random.choice(config.GIFS)

        await interaction.response.send_message(
            content=(
                f"{interaction.user.mention} запустил(а) торт "
                f"в {self.new_member.mention}! 💥"
            ),
            file=discord.File(gif),
        )
