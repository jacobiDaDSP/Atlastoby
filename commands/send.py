import discord
import asyncio
from config.presets import PRESET_MESSAGE
from utils.files import send_with_file, get_random_path
from utils.helpers import send_ephemeral_delete
from utils.farm import FarmView

async def send_command(interaction: discord.Interaction, count: int = 10, button: bool = False):
    if button:
        async def send_func(i):
            for _ in range(count):
                await i.followup.send(f"**{PRESET_MESSAGE}**")
        await interaction.response.send_message("Click FARM to stack tokens, then Send to send", view=FarmView(send_func, "Send"), ephemeral=True)
    else:
        await send_ephemeral_delete(interaction, f"Sending {count} messages...", delay=2.0)
        async def send_one():
            path = get_random_path()
            try:
                if path:
                    await interaction.followup.send(content=f"**{PRESET_MESSAGE}**", file=discord.File(path))
                else:
                    await interaction.followup.send(content=f"**{PRESET_MESSAGE}**")
            except:
                pass
        await asyncio.gather(*(send_one() for _ in range(count)))