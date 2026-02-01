import discord
from config.presets import ANDREW_TATE
from utils.helpers import send_ephemeral_delete
from utils.farm import FarmView

async def andrewtate_command(interaction: discord.Interaction, count: int = 5, button: bool = False):
    if button:
        async def send_func(i):
            for _ in range(count):
                await i.followup.send(ANDREW_TATE)
        await interaction.response.send_message("Click FARM to stack tokens, then Tate to send", view=FarmView(send_func, "Tate"), ephemeral=True)
    else:
        await send_ephemeral_delete(interaction, f"Sending {count} Andrew Tate messages...", delay=1.0)
        for _ in range(count):
            await interaction.followup.send(ANDREW_TATE)