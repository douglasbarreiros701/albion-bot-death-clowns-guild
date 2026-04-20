import os
from dotenv import load_dotenv
from bot.client import DeathClown

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

if TOKEN is None:
    raise ValueError("DISCORD_TOKEN não foi encontrado no arquivo .env")

bot = DeathClown()
bot.run(TOKEN)