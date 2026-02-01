import discord
from config.rapeurls import URLS
from utils.helpers import format_urls, send_ephemeral_delete
from utils.farm import FarmView

async def rape_command(interaction: discord.Interaction, batches: int = 5, button: bool = False):
    if button:
        async def send_func(i):
            for _ in range(batches):
                text = format_urls(URLS)
                if text:
                    await i.followup.send(text)
        await interaction.response.send_message("Click FARM to stack tokens, then Rape to send", view=FarmView(send_func, "Rape"), ephemeral=True)
    else:
        await send_ephemeral_delete(interaction, f"Sending {batches} batches...", delay=1.0)
        for _ in range(batches):
            text = format_urls(URLS)
            if text:
                await interaction.followup.send(text)