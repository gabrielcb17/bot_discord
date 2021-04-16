import discord
import decouple
import B
import discord.utils
from discord.ext import commands, tasks

TOKEN = decouple.config('JOHANNSEBASTIANBOT_TOKEN')

# key = os.getenv('key')  # just some things you might want inside the bot here.
#
# wkey = os.getenv('wkey')

intents = discord.Intents().all()

# client = discord.Client(intents=intents)  # declaring what the bot is.

bot = commands.Bot(command_prefix='&', intents=intents)  # Makes the bot prefix.
bot.remove_command('help')  # Removes the auto help command as it can be buggy.



@bot.event
async def on_ready(ctx):
    print("Bot joined/Updated successfully!")


@bot.command()
async def imitate(ctx, *, mssg=None):
    if mssg == None:
        await ctx.send('Put the message you need in.')
    else:
        await ctx.send(f'{mssg}')


# @bot.command()
# @commands.has_permissions(administrator=True)
# async def kick(ctx, user: discord.Member, *, reason):
#     await user.kick(reason=reason)
#     await ctx.send(f'{user} kicked for {reason}')
#
#
# @bot.command()
# @commands.has_permissions(administrator=True)
# async def ban(ctx, user: discord.Member, *, reason):
#     await user.kick(reason=reason)
#     await ctx.send(f'{user} banned for {reason}')


@bot.event
async def on_command_error(ctx, error):
    await ctx.send(f'Error: {error}')


@bot.command()
async def test(ctx):
    await ctx.send('This is a test.')


@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Help", description="This page is for helping you guys understand the commands.",
                          color=0xFFFFF)  # Declaring the help command is an embed.

    # embed.add_field(name="command", value="Command to try.")  # adding fields and such here.

    embed.add_field(name="help", value="This is the help command.")

    # embed.add_field(name="ban", value="Bans the user.")
    #
    # embed.add_field(name="kick", value="kicks the user.")

    embed.add_field(name="imitate", value="Imitates the given words.")

    await ctx.send(embed=embed)  # sends the embed.


# Deixa registrado quando alguém entra no server, e adiciona o título de <musicuzinh@>.
@bot.event
async def on_member_join(member):
    print(f'{member} has joined the server.')

    role = discord.utils.get(member.guild.roles, id=831687556277076008)
    await member.add_roles(role)

    system_channel = member.guild.system_channel
    await system_channel.send(f'{member} has joined the server and given the role musicuzinh@.')


# runs the server
B.b()

# runs the bot token.
bot.run(TOKEN)