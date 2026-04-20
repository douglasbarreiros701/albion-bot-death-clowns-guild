import discord
from discord import app_commands


def setup_ping(tree: app_commands.CommandTree):
    @tree.command(name="ping", description="Testa se o bot está online")
    async def ping(interaction: discord.Interaction):
        await interaction.response.send_message("Pong!")