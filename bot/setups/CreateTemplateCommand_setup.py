import discord
from discord import app_commands


class CreateTemplateCommand:
    def __init__(self, tree: app_commands.CommandTree):
        self.tree = tree
        self.tree.add_command(self.criar_template)