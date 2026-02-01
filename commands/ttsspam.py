import discord
import asyncio
from utils.helpers import send_ephemeral_delete
from utils.farm import FarmView

async def ttsspam_command(interaction: discord.Interaction, text: str, count: int = 5, button: bool = False):
    if button:
        async def send_func(i):
            for _ in range(count):
                await i.followup.send(text, tts=True)
                await asyncio.sleep(0.3)
        await interaction.response.send_message("Click FARM to stack tokens, then TTS to send", view=FarmView(send_func, "TTS"), ephemeral=True)
    else:
        await send_ephemeral_delete(interaction, f"Spamming TTS {count} times...", delay=1.0)
        for _ in range(count):
            await interaction.followup.send(text, tts=True)
            await asyncio.sleep(0.3)