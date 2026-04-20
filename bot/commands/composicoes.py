import discord
from discord import app_commands

from bot.views.composicao_view import ComposicaoView


def setup_composicoes(tree: app_commands.CommandTree):
    @tree.command(name="conteudo", description="Cria uma composição interativa")
    @app_commands.describe(
        tipo_conteudo="Tipo de conteúdo",
        horario_saida="Horário de saída",
        cidade="Cidade de saída",
        food="Food que será usada",
        loot="Tipo de loot"
    )
    async def conteudo(
        interaction: discord.Interaction,
        tipo_conteudo: str,
        horario_saida: str,
        cidade: str,
        food: str,
        loot: str,
    ):
        view = ComposicaoView(tipo_conteudo=tipo_conteudo, horario_saida=horario_saida, cidade=cidade, food=food, loot=loot,)

        await interaction.response.send_message(content=view.montar_mensagem(), view=view)