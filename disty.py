import discord
from discord.ext import commands
from discord.ext.commands import has_permissions

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

@bot.command()
@has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f"{member} був виключений за причиною: {reason}")

@bot.command()
@has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f"{member} був заблокований за причиною: {reason}")

@bot.event
async def on_message(message):
    if message.content.startswith("!rules"):
        await message.channel.send("Будь ласка, дотримуйтесь правил чату!")
    await bot.process_commands(message)

bot.run("YOUR_TOKEN")
