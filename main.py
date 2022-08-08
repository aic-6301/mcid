import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

bot = commands.Bot(command_prefix='mc!', intents=discord.Intents.all())
load_dotenv()
token = os.environ['TOKEN']

@bot.event
async def on_ready():
    print('ready')


class mcid(discord.ui.Modal):
    def __init__(self):
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
    async def on_submit(self, interaction) -> None:
        self.value = self.name.value
        self.stop()
        await interaction.response.send_message(f'MCIDを{self.value}に登録しました。', ephemeral=True)

class board(discord.ui.View):
    def __init__(bot):
        super().__init__()
        discord.ui.view.timeout = None
    @discord.ui.button(label='MCID入力', style=discord.ButtonStyle.secondary, emoji='📝', row=2)
    async def mcid(self, interaction: discord.Interaction, button: discord.ui.Button):
        modal = mcid()
        channel = bot.get_channel(1006171661789306991)
        await interaction.response.send_modal(modal)
        await modal.wait()
        e = discord.Embed(title=f"{self.author.name}のMCID", description=modal.value)
        e.add_field(name='namemc', value=f'https://ja.namemc.com/{modal.value}', inline=False)
        await channel.send(embed=e)



@bot.command()
async def mcide(ctx):
        embed = discord.Embed(title="MCID用", colour=discord.Colour(0x1122a6), description="MCIDを送信してください。")
        embed.set_footer(text='Powered by AIC_6301')
        await ctx.send(embed=embed, view=board())

bot.run(token)