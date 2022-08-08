import discord
from discord.ext import commands

bot = commands.Bot(prefix='mc!', intents=discord.intents.all())
token = token

@bot.event
async def on_ready():
    print('ready')


class mcid(discord.ui.Modal):
    def __init__():
        super().__init__(
            title="MCID送信",
            timeout=60,
        )
        self.value = None

        self.name = discord.ui.TextInput(
            label="MCIDを入力",
            style=discord.TextStyle.short,
            placeholder="AIC_6301",
            required=True,
        )
        self.add_item(self.name)

class board(discord.ui.View):
    def __init__(bot):
        super().__init__()
        discord.ui.view.timeout = None
        self.bot = bot.bot
@discord.ui.button(label='名前変更', style=discord.ButtonStyle.secondary, emoji='📝', row=2)
    async def rename(self, interaction: discord.Interaction, button: discord.ui.Button):
        result = await owner.check(self, interaction.user, interaction.channel)
        
        if result == 'vc1':
            modal = rename()
            await interaction.response.send_modal(modal)
            await modal.wait()
            if modal.value == '':
                await self.bot.vc1.edit(name='VC-1(128Kbps)')
            else:
                await self.bot.vc1.edit(name=modal.value)
