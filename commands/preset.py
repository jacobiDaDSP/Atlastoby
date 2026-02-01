import discord
import asyncio
from config.presets import PRESET_MESSAGE
from utils.helpers import send_ephemeral_delete
from utils.farm import FarmView

async def preset_command(interaction: discord.Interaction, count: int = 5, button: bool = False):
    if button:
        async def send_func(i):
            for _ in range(count):
                await i.followup.send(PRESET_MESSAGE)
        await interaction.response.send_message("Click FARM to stack tokens, then Preset to send", view=FarmView(send_func, "Preset"), ephemeral=True)
    else:
        await send_ephemeral_delete(interaction, f"Sending {count} messages...", delay=1.0)
        for _ in range(count):
            await interaction.followup.send(PRESET_MESSAGE)