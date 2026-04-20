import discord
from discord import app_commands
from bot.commands.composicoes import setup_composicoes
from bot.commands.ping import setup_ping

GUILD_ID = 988507022741897226


class DeathClown(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        setup_ping(self.tree)
        setup_composicoes(self.tree)
        setup_createEvents(self.tree)

        guild = discord.Object(id=GUILD_ID)
        self.tree.copy_global_to(guild=guild)
        synced = await self.tree.sync(guild=guild)

        print(f"Sincronizados {len(synced)} comandos no servidor de teste.")

    async def on_ready(self):
        print(f"O bot {self.user} foi ligado com sucesso.")