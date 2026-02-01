import discord
import asyncio
from utils.helpers import send_ephemeral_delete, delete_safe
from utils.farm import FarmView

async def ghostping_command(interaction: discord.Interaction, user: discord.User, count: int = 5, button: bool = False):
    if button:
        async def send_func(i):
            for _ in range(count):
                m = await i.followup.send(user.mention)
                await delete_safe(m)
        await interaction.response.send_message("Click FARM to stack tokens, then Ghost to send", view=FarmView(send_func, "Ghost"), ephemeral=True)
    else:
        await send_ephemeral_delete(interaction, f"Sending {count} ghostpings...", delay=1.0)
        for _ in range(count):
            m = await interaction.followup.send(user.mention)
            await delete_safe(m)