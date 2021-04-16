import discord
import decouple
import B
import discord.utils
from random import choice
from discord.ext import commands, tasks
from APIs import *

# -------------------- CONSTANTS -------------------- #
TOKEN = decouple.config('JOHANNSEBASTIANBOT_TOKEN')

TONALITIES = {
    "keys": [chr(i) for i in range(65, 72)],
    "accidents": ["#", "♭", ""],
    "quality": [" major", " minor"]
}

SCALES = {
    "keys": [chr(i) for i in range(65, 72)],
    "accidents": ["# ", "♭ ", " "],
    "quality": [
        "major",
        "harmonic major"
        "natural minor",
        "harmonic minor",
        "melodic minor",
        "ionian mode",
        "dorian mode",
        "phrygian mode",
        "lydian mode",
        "mixolydian mode",
        "aeolian mode",
        "locrian mode",
        "acoustic scale (4#-7♭)",
        "super locrian",
        "bebop scale",
        "blues scale",
        "chromatic scale",
        "flamenco scale",
        "enigmatic scale",
        "gypsy scale",
        "half diminished scale",
        "hungarian gypsy/minor scale",
        "hungarian major scale",
        "major pentatonic scale",
        "minor pentatonic scale",
        "neapolitan major scale",
        "neapolitan minor scale",
        "octatonic scale",
        "persian scale",
        "phrygian dominant scale",
        "prometheus scale",
        "tritone scale",
        "two-semitone tritone scale",
        "ukrainian dorian scale",
        "whole tone scale",
    ]
}

# key = os.getenv('key')  # just some things you might want inside the bot here.
#
# wkey = os.getenv('wkey')

# -------------------- INSTANCES ------------------ #
intents = discord.Intents().all()

bot = commands.Bot(command_prefix='&', intents=intents)  # defines the bot prefix.
bot.remove_command('help')  # Removes the auto help command as it can be buggy.

# -------------------- EVENTS ------------------------- #
@bot.event
async def on_ready(ctx):
    print("Bot joined/Updated successfully!")

@bot.event
async def on_command_error(ctx, error):
    await ctx.send(f'Error: {error}')


# Deixa registrado quando alguém entra no server, e adiciona o título de <musicuzinh@>.
@bot.event
async def on_member_join(member):
    print(f'{member} has joined the server.')

    role = discord.utils.get(member.guild.roles, id=831687556277076008)
    await member.add_roles(role)

    system_channel = member.guild.system_channel
    await system_channel.send(f'{member} has joined the server and given the role musicuzinh@.')

# ------------------ COMMANDS ------------------ #

@bot.command(aliases=["teste"])
async def test(ctx):
    await ctx.send('This is a test.')

@bot.command(aliases=["ajuda"])
async def help(ctx):
    embed = discord.Embed(title="Help", description="This page is for helping you guys understand the commands.",
                          color=0xFFFFF)  # Declaring the help command is an embed.

    # embed.add_field(name="command", value="Command to try.")  # adding fields and such here.

    embed.add_field(name="help", value="This is the help command.")

    # embed.add_field(name="ban", value="Bans the user.")

    # embed.add_field(name="kick", value="kicks the user.")

    embed.add_field(name="imitate", value="Imitates the given words.")

    embed.add_field(name="key", value="Returns a random key (tonality).")

    await ctx.send(embed=embed)  # sends the embed.

@bot.command(aliases=["imitar"])
async def imitate(ctx, *, mssg=None):
    if mssg == None:
        await ctx.send('Put the message you need in.')
    else:
        await ctx.send(f'{mssg}')

@bot.command(aliases=["tonalidade", "tonality", "tom"])
async def key(ctx):
    tonality = ""
    for key, value in TONALITIES.items():
        tonality += choice(value)

    await ctx.send(tonality)

@bot.command(aliases=["escala"])
async def scale(ctx):
    scale = ""
    for key, value in SCALES.items():
        scale += choice(value)

    await ctx.send(scale)

@bot.command(aliases=["gatos", "cats"])
async def catfacts(ctx):
    cat_facts = get_cat_facts()
    random_fact = choice(cat_facts)
    await ctx.send(random_fact["text"])

@bot.command(aliases=["drink"])
async def cocktail(ctx):
    drink = get_random_drink()

    embed = discord.Embed(title=drink[0]["strDrink"],)
    embed.set_author(
        name="TheCocktailDB",
        url="https://www.thecocktaildb.com/",
        icon_url="https://www.thecocktaildb.com/images/cocktail_left.png"
    )
    embed.set_image(url=drink[0]["strDrinkThumb"])
    embed.add_field(name="Ingredients", value=drink[1], inline=False)
    embed.add_field(name="Instructions", value=drink[0]["strInstructions"], inline=False)

    info = str(drink[2]).strip("[]")
    embed.set_footer(text=info)

    await ctx.send(embed=embed)

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

# -------------------------------------------------------------- #


# runs the server
B.b()

# runs the bot token.
bot.run(TOKEN)