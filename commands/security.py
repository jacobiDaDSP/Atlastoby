import discord
import random
import asyncio
from datetime import datetime
from utils.helpers import send_ephemeral_delete

def get_fake_geo():
    locations = [
        ("New York, NY", "US", "Verizon Communications"),
        ("Los Angeles, CA", "US", "AT&T Internet"),
        ("Chicago, IL", "US", "Comcast Cable"),
        ("Dallas, TX", "US", "Charter Communications"),
        ("Miami, FL", "US", "T-Mobile USA"),
        ("Seattle, WA", "US", "Google Fiber"),
        ("Austin, TX", "US", "Spectrum Business"),
        ("Denver, CO", "US", "CenturyLink"),
        ("Phoenix, AZ", "US", "Cox Communications"),
        ("Atlanta, GA", "US", "Xfinity Mobile"),
        ("Boston, MA", "US", "Starlink"),
        ("San Francisco, CA", "US", "Fastly Inc."),
        ("Houston, TX", "US", "Frontier Communications"),
        ("Toronto, ON", "CA", "Rogers Communications"),
        ("London, ENG", "GB", "Sky Broadband"),
        ("Paris, IDF", "FR", "Orange S.A."),
        ("Berlin, BE", "DE", "Vodafone Germany"),
        ("Sydney, NSW", "AU", "Telstra Corporation"),
        ("Singapore, SG", "SG", "Singtel"),
        ("Seoul, KR", "KR", "SK Broadband"),
        ("Mumbai, MH", "IN", "Reliance Jio"),
        ("Tokyo, TYO", "JP", "NTT Communications"),
        ("Frankfurt, HE", "DE", "Deutsche Telekom"),
        ("Moscow, MOW", "RU", "PJSC Rostelecom")
    ]
    return random.choice(locations)

def generate_ip():
    return f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(1, 255)}"

def build_malicious_alert_embed(user: discord.User):
    ip = generate_ip()
    city, country, isp = get_fake_geo()
    timestamp = datetime.utcnow().strftime('%H:%M:%S')
    
    description = (
        f"## 🚨 CRITICAL INTRUSION DETECTED 🚨\n"
        f"**STATUS:** `INJECTING EXPLOIT...` [100%]\n"
        f"**TARGET:** `{user.name}`\n\n"
        f"**NETWORK DATA**\n"
        f"IP Address: `{ip}`\n"
        f"Location: `{city}, {country}`\n"
        f"Provider: `{isp}`\n\n"
        f"```diff\n"
        f"+ [SYSTEM] DROYD_CORE_LOADED\n"
        f"+ [GEORGE] BYPASS_SEQUENCE_INITIATED\n"
        f"+ [PROPYLON] DATA_STREAM_CAPTURED\n"
        f"+ [CYBORG] NECK_PROTECTION_MODULE_ENABLED\n"
        f"- [CRITICAL] DISCORD_ACCOUNT_COMPROMISED\n"
        f"```\n"
        f"**ACTION:** `UPLOADING RECOVERY_TOKEN...`"
    )

    embed = discord.Embed(
        title="⚠️ MALICIOUS OVERRIDE ACTIVE",
        description=description,
        color=discord.Color.red()
    )
    
    embed.set_author(name="DROYD SECURITY BYPASS", icon_url="https://cdn-icons-png.flaticon.com/512/564/564619.png")
    embed.set_footer(text=f"UTC LOG: {timestamp} • TARGET COMPROMISED", icon_url=user.display_avatar.url)
    embed.set_thumbnail(url=user.display_avatar.url)
    
    return embed

class SecurityButton(discord.ui.View):
    def __init__(self, user: discord.User, count: int):
        super().__init__(timeout=None)
        self.user = user
        self.count = count

    @discord.ui.button(label="EXECUTE EXPLOIT", style=discord.ButtonStyle.danger)
    async def security_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(f"`[SYSTEM]` Injecting exploit into {self.user.name}...", ephemeral=True)
        
        for _ in range(self.count):
            embed = build_malicious_alert_embed(self.user)
            await interaction.followup.send(
                content=f"⚠️ **URGENT ALERT** {self.user.mention}", 
                embed=embed, 
                ephemeral=False
            )
            if self.count > 1:
                await asyncio.sleep(1.0)

async def security_command(interaction: discord.Interaction, user: discord.User, count: int = 1, button: bool = False):
    if button:
        await interaction.response.send_message(
            f"**READY TO COMPROMISE:** {user.mention}", 
            view=SecurityButton(user, count), 
            ephemeral=True
        )
    else:
        await interaction.response.send_message(f"`[SYSTEM]` Injecting exploit into {user.name}...", ephemeral=True)
        for _ in range(count):
            embed = build_malicious_alert_embed(user)
            await interaction.followup.send(
                content=f"⚠️ **URGENT ALERT** {user.mention}", 
                embed=embed, 
                ephemeral=False
            )
