import discord
from discord.ext import commands вооаввоопопопопоашш

bot = commands.Bot(command_prefix='!') # Set the command prefix to "!"

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'{member.mention} has been kicked.')

@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'{member.mention} has been banned.')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('!rules'):
        await message.channel.send('Please follow the rules!')

    await bot.process_commands(message)

bot.run('TOKEN')
