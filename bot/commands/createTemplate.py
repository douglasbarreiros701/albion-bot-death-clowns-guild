import discord
from discord import app_commands, interactions


def setup_createTemplate(tree: app_commands.CommandTree):
    @tree.command(name='criar_template', description='Criar template para evento')
    async def criar_template(interaction: discord.Interaction):
        view = TemplateView()
        await interactions.response.send_message("Vamos criar um template de evento!", view=view)

