import discord
from utils.helpers import send_ephemeral_delete
from utils.farm import FarmView

async def talk_command(interaction: discord.Interaction, text: str, count: int = 1, button: bool = False):
    if button:
        async def send_func(i):
            for _ in range(count):
                await i.followup.send(text)
        await interaction.response.send_message("Click FARM to stack tokens, then Talk to send", view=FarmView(send_func, "Talk"), ephemeral=True)
    else:
        await send_ephemeral_delete(interaction, f"Talking {count} times...", delay=1.0)
        for _ in range(count):
            await interaction.followup.send(text)