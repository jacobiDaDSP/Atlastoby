import discord
from config.arts import HEIL_ART
from utils.helpers import send_ephemeral_delete
from utils.farm import FarmView

async def heil_command(interaction: discord.Interaction, count: int = 5, button: bool = False):
    if button:
        async def send_func(i):
            for _ in range(count):
                await i.followup.send(HEIL_ART)
        await interaction.response.send_message("Click FARM to stack tokens, then Heil to send", view=FarmView(send_func, "Heil"), ephemeral=True)
    else:
        await send_ephemeral_delete(interaction, f"Sending {count} heils...", delay=1.0)
        for _ in range(count):
            await interaction.followup.send(HEIL_ART)