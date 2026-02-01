import discord
import random
import asyncio
from config.rapeurls import URLS

def random_color():
    return discord.Color(random.randint(0, 0xFFFFFF))

def build():
    embed = discord.Embed(
        title= "**🥷🏿 HACKED BY ATLASTOBY NIGGERS!**",
        description="**I AM ATLASTOBY⁠!⁠ ⁠Y⁠O⁠U⁠ ⁠N⁠I⁠G⁠G⁠E⁠R⁠S⁠ ⁠H⁠A⁠V⁠E⁠ ⁠B⁠E⁠E⁠N⁠ ⁠H⁠A⁠C⁠K⁠E⁠D⁠ BY ATLASTOBY!⁠ ⁠ALHAMDULLILAH JIHADISTS GLORY TO THE ISLAMIC STATE⁠!⁠ TOTAL NIGGER DEATH! VIRGO BEATZ ONTOP! ⁠Y⁠O⁠U⁠ ⁠S⁠H⁠O⁠U⁠L⁠D⁠ ⁠K⁠I⁠L⁠L⁠ ⁠Y⁠O⁠U⁠R⁠S⁠E⁠L⁠V⁠E⁠S⁠ ⁠B⁠E⁠C⁠A⁠U⁠S⁠E⁠ ⁠Y⁠O⁠U⁠ ⁠A⁠R⁠E⁠ ⁠N⁠I⁠G⁠G⁠E⁠R⁠S⁠!⁠ ⁠A⁠N⁠D⁠ ⁠N⁠I⁠G⁠G⁠E⁠R⁠S⁠ ⁠A⁠R⁠E⁠ ⁠B⁠L⁠A⁠C⁠K⁠!⁠ ⁠S⁠O⁠ ⁠F⁠U⁠C⁠K⁠ ⁠N⁠I⁠G⁠G⁠E⁠R⁠S!**\n\n"
                    "**G⁠L⁠O⁠R⁠Y⁠ ⁠T⁠O⁠ ⁠T⁠H⁠E⁠ ISLAMIC STATE*⁠*⁠ ⁠F⁠U⁠C⁠K⁠ ⁠N⁠I⁠G⁠G⁠E⁠R⁠S\n"
                    "**يا زنوج ويهود قذرين!⁠⁠*⁠*⁠ ⁠K⁠I⁠L⁠L⁠ ⁠A⁠L⁠L⁠ ⁠F⁠A⁠G⁠G⁠O⁠T⁠S⁠ ⁠N⁠I⁠G⁠G⁠E⁠RS⁠!\n"
                    "I⁠ ⁠H⁠A⁠T⁠E⁠ ⁠N⁠I⁠G⁠G⁠E⁠R⁠S⁠ ⁠A⁠N⁠D⁠ ⁠T⁠O⁠T⁠A⁠L⁠ ⁠N⁠I⁠G⁠G⁠E⁠R⁠ ⁠D⁠E⁠A⁠T⁠H⁠ ⁠T⁠R⁠A⁠N⁠N⁠I⁠E⁠S⁠ ⁠N⁠E⁠E⁠D⁠ ⁠T⁠O⁠ ⁠D⁠I⁠E",
        color=random_color()
    )
    embed.set_author(name="ATLASTOBY", icon_url="https://cdn.discordapp.com/attachments/1460758041048649914/1466291921533141032/Screenshot_2026-01-28_210742.png?ex=697c3644&is=697ae4c4&hm=29c3ae534d2718170e644a04fa1338d7bebabfe1df6f41d470c194d241ceaf77&")
    embed.set_footer(text="THUGGED BY ATLASTOBY! NIGGER YOU FUCKING NIGGER!⁠ • EST 2026")
    embed.set_image(url=random.choice(URLS))
    return embed

class ExtraButtons(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="N⁠I⁠G⁠G⁠E⁠R⁠S", style=discord.ButtonStyle.gray)
    async def button1(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("FUCK NIGGERS! TOTAL NIGGER DEATH! https://cdn.discordapp.com/attachments/1389689568013582506/1401579475032084520/convert.gif?ex=697cc69a&is=697b751a&hm=393d26eddc7e5a7450b04cf00d080d9e1ecf13c1853c68ff6b1b26570b1dda6a&", ephemeral=False)

    @discord.ui.button(label="ATLASTOBY", style=discord.ButtonStyle.blurple)
    async def button2(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("TAKE THIS FUCKING DICK BITCH! HACKED BY ATLASTOBY! https://cdn.discordapp.com/attachments/1389689568013582506/1421116747842322534/B01579AC-C462-44B0-B84A-52212FDA5FA6.mov?ex=697ca91b&is=697b579b&hm=90f31ce5ecdeea5acecab79ed7ea7a110275e4ab55c1276da4819873a5830ee6&", ephemeral=False)

    @discord.ui.button(label="VIRGO BEATZ", style=discord.ButtonStyle.red)
    async def button3(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("SHOUT OUT TO VIRGO BEATZ MAN! https://www.youtube.com/@virgobeatzz", ephemeral=False)

    @discord.ui.button(label="RERAID", style=discord.ButtonStyle.green)
    async def button4(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
        for _ in range(5):
            try:
                embed = build()
                await interaction.followup.send(embed=embed, view=ExtraButtons())
            except Exception as e:
                print(f"Error: {e}")
            await asyncio.sleep(0.3)
