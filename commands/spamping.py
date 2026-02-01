import discord
import asyncio
from utils.helpers import send_ephemeral_delete, delete_safe
from utils.farm import FarmView

async def spam_command(interaction: discord.Interaction, user: discord.User, count: int = 10, message: str = "GET SPAMMED", button: bool = False):
    if button:
        async def send_func(i):
            for _ in range(count):
                await i.followup.send(f"{user.mention} {message}")
        await interaction.response.send_message("Click FARM to stack tokens, then Spam to send", view=FarmView(send_func, "Spam"), ephemeral=True)
    else:
        await send_ephemeral_delete(interaction, f"Spamming {count} messages...", delay=1.0)
        for _ in range(count):
            await interaction.followup.send(f"{user.mention} {message}")