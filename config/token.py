import os

Token = os.getenv("DISCORD_TOKEN")

if not Token:
    raise RuntimeError("DISCORD_TOKEN is not set")
