import discord
from discord import app_commands
from bot.commands.composicoes import setup_composicoes
from bot.commands.ping import setup_ping



class DeathClown(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        self.add_view(TemplateView())
        await self.tree.sync()

        async def on_ready(self):
            print(f'O bot {self.user} foi ligado com sucesso.')




