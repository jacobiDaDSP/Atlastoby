import discord
import asyncio
from utils.embed import build, ExtraButtons
from utils.farm import FarmView

async def embedspam_command(interaction: discord.Interaction, count: int = 10, button: bool = False):
    if button:
        async def send_func(i):
            for _ in range(count):
                try:
                    embed = build()
                    await i.followup.send(embed=embed, view=ExtraButtons())
                except Exception as e:
                    print(f"Error: {e}")
                await asyncio.sleep(0.3)
        await interaction.response.send_message("Click FARM to stack tokens, then Embed to send", view=FarmView(send_func, "Embed"), ephemeral=True)
    else:
        await interaction.response.send_message(f"Sending {count} embeds...", ephemeral=True)
        for _ in range(count):
            try:
                embed = build()
                await interaction.followup.send(embed=embed, view=ExtraButtons())
            except Exception as e:
                print(f"Error: {e}")
            await asyncio.sleep(0.3)