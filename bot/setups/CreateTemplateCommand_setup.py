import discord
from discord import app_commands


class CreateTemplateCommand:
    def __init__(self, tree: app_commands.CommandTree):
        self.tree = tree
        self.tree.add_command(self.criar_template)

        @app_commands.command(name='criar_template', description='Crie o template para um evento')
        async def criar_template(self, interaction: discord.Interaction):
            await interaction.response.send_message('Digite o nome do evento', ephemeral=True)
            #interaction!!!!1

            handler =