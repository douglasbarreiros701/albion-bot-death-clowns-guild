import discord
import asyncio


class TemplateInteractionHandler:
    def __init__(self, interaction: discord.Interaction):
        self.interaction = interaction
        self.template_data = {}


    async def coletar_nome_evento(self):
        await self.interaction.followup.send('Por favor, forneça o nome do evento:', ephemeral=True)

        try:
            response = await self.interaction.client.wait_for(
        'message',
                check=lambda message: message.author == self.interaction.user and message.channel == self.interaction.channel,
                timeout=60.0
            )

            nome_evento = response.content
            self.template_data["nome"] = nome_evento

            await self.interaction.followup.send(f"Nome do evento: {nome_evento}. Agora, forneça a descrição", ephemeral=True)

            await self.coletar_descricao_evento()

        except asyncio.TimeoutError:
            await self.interaction.followup.send("Tempo esgotado! Por favor, tente novamente!", ephemeral=True)


            async def coletar_descricao_evento(self):
                await self.interaction.followup.send("Por favor, forneça a descrição do evento:", ephemeral=True)

                try:
                    response = await self.interaction.client.wait_for(
                        'message',
                        check=lambda message: message.author == self.interaction.user and message.channel == self.interaction.channel,
                        timeout=60.0
                    )

                    descricao_evento = response.content
                    self.template_data["descricao"] = descricao_evento
                    await self.interaction.followup.send(f"Descrição do evento: {descricao_evento}. Agora, forneça a data:", ephemeral=True)
                    await self.coletar_descricao_evento()
                except asyncio.TimeoutError:
                    await self.interaction.followup.send("Tempo esgotado! Por favor, tente novamente!")
