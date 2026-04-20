import discord


class ComposicaoView(discord.ui.View):
    def __init__(self, tipo_conteudo: str, horario_saida: str, cidade: str, food: str, loot: str):
        super().__init__(timeout=None)

        self.tipo_conteudo = tipo_conteudo
        self.horario_saida = horario_saida
        self.cidade = cidade
        self.food = food
        self.loot = loot

        self.slots = {
            "tank": None,
            "healer": None,
            "sc": None,
            "fg": None,
            "dps_druid": None,
            "dps_1": None,
            "dps_2": None,
        }

    def _nome_ou_vazio(self, membro: discord.Member | None) -> str:
        return membro.mention if membro else "vazio"

    def montar_mensagem(self) -> str:
        return (
            f"**{self.tipo_conteudo.upper()}**\n\n"
            f"**Horário Saída:** {self.horario_saida}\n"
            f"**Cidade:** {self.cidade}\n"
            f"**Food:** {self.food}\n"
            f"**Loot:** {self.loot}\n\n"
            f"🟦 **TANK:** {self._nome_ou_vazio(self.slots['tank'])}\n"
            f"🟩 **HEALER:** {self._nome_ou_vazio(self.slots['healer'])}\n"
            f"🟥 **SC (Double Reset):** {self._nome_ou_vazio(self.slots['sc'])}\n"
            f"🟥 **FG:** {self._nome_ou_vazio(self.slots['fg'])}\n"
            f"🟥 **DPS (Capote Druid):** {self._nome_ou_vazio(self.slots['dps_druid'])}\n"
            f"🟥 **DPS:** {self._nome_ou_vazio(self.slots['dps_1'])}\n"
            f"🟥 **DPS:** {self._nome_ou_vazio(self.slots['dps_2'])}"
        )

    def limpar_usuario_dos_slots(self, usuario: discord.Member) -> None:
        for slot, membro in self.slots.items():
            if membro and membro.id == usuario.id:
                self.slots[slot] = None

    async def ocupar_slot(self, interaction: discord.Interaction, nome_slot: str) -> None:
        usuario = interaction.user

        if not isinstance(usuario, discord.Member):
            await interaction.response.send_message(
                "Esse botão só funciona dentro de servidor.",
                ephemeral=True
            )
            return

        ocupante_atual = self.slots[nome_slot]

        if ocupante_atual is not None and ocupante_atual.id != usuario.id:
            await interaction.response.send_message(
                "Cargo já ocupado! Escolha outro.",
                ephemeral=True
            )
            return

        self.limpar_usuario_dos_slots(usuario)
        self.slots[nome_slot] = usuario

        await interaction.response.edit_message(
            content=self.montar_mensagem(),
            view=self
        )

    @discord.ui.button(label="Tank", style=discord.ButtonStyle.primary, row=0)
    async def botao_tank(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.ocupar_slot(interaction, "tank")

    @discord.ui.button(label="Healer", style=discord.ButtonStyle.success, row=0)
    async def botao_healer(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.ocupar_slot(interaction, "healer")

    @discord.ui.button(label="SC", style=discord.ButtonStyle.danger, row=0)
    async def botao_sc(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.ocupar_slot(interaction, "sc")

    @discord.ui.button(label="FG", style=discord.ButtonStyle.danger, row=1)
    async def botao_fg(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.ocupar_slot(interaction, "fg")

    @discord.ui.button(label="DPS Druid", style=discord.ButtonStyle.danger, row=1)
    async def botao_dps_druid(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.ocupar_slot(interaction, "dps_druid")

    @discord.ui.button(label="DPS 1", style=discord.ButtonStyle.secondary, row=1)
    async def botao_dps_1(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.ocupar_slot(interaction, "dps_1")

    @discord.ui.button(label="DPS 2", style=discord.ButtonStyle.secondary, row=2)
    async def botao_dps_2(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.ocupar_slot(interaction, "dps_2")

    @discord.ui.button(label="Sair", style=discord.ButtonStyle.secondary, row=2)
    async def botao_sair(self, interaction: discord.Interaction, button: discord.ui.Button):
        usuario = interaction.user

        if not isinstance(usuario, discord.Member):
            await interaction.response.send_message(
                "Esse botão só funciona dentro de servidor.",
                ephemeral=True
            )
            return

        self.limpar_usuario_dos_slots(usuario)

        await interaction.response.edit_message(
            content=self.montar_mensagem(),
            view=self
        )