import discord

class FarmView(discord.ui.View):
    def __init__(self, send_func, action_label: str = "Send"):
        super().__init__(timeout=None)
        self.send_func = send_func
        self.tokens = []
        self.send_btn.label = action_label

    @discord.ui.button(label="FARM", style=discord.ButtonStyle.green)
    async def farm_btn(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.tokens.append(interaction)
        await interaction.response.edit_message(content=f"{len(self.tokens)} tokens farmed")

    @discord.ui.button(label="Send", style=discord.ButtonStyle.blurple)
    async def send_btn(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.edit_message(content=f"Sending with {len(self.tokens) + 1} tokens...")
        await self.send_func(interaction)
        for token in self.tokens:
            await self.send_func(token)