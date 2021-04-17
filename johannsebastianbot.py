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

BOT_PREFIX = "&"

# key = os.getenv('key')  # just some things you might want inside the bot here.
#
# wkey = os.getenv('wkey')

# -------------------- INSTANCES ------------------ #
intents = discord.Intents().all()

bot = commands.Bot(
    command_prefix=BOT_PREFIX,   # defines the bot prefix.
    intents=intents,
    help_command=None,
    strip_after_prefix=True
)
# bot.remove_command('help')  # Removes the auto help command as it can be buggy.

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
    prefix = await bot.get_prefix(ctx.message)
    embed = discord.Embed(title="Help", description="This is a description of all my commands.",
                          color=0xFFFFF)  # Declaring the help command is an embed.

    # embed.add_field(name="command", value="Command to try.")  # adding fields and such here.

    embed.add_field(name=f"{prefix}help", value="This is the help command.")

    embed.add_field(name=f"{prefix}profile",
                    value="Mention someone to see profile (don't mention anyone to see your own profile)")

    # embed.add_field(name="ban", value="Bans the user.")

    # embed.add_field(name="kick", value="kicks the user.")

    embed.add_field(name=f"{prefix}imitate", value="Imitates the given words.")

    embed.add_field(name=f"{prefix}key", value="Returns a random key (tonality).")

    embed.add_field(name=f"{prefix}scale", value="Returns a random musical scale.")

    embed.add_field(name=f"{prefix}catfacts", value="Returns a random cat fact (list changes every day).")

    embed.add_field(name=f"{prefix}catpic", value="Returns a random cat picture.")

    embed.add_field(name=f"{prefix}foxpic", value="Returns a random fox picture.")

    embed.add_field(name=f"{prefix}cocktail", value="Returns a random cocktail recipe.")

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

@bot.command(aliases=["cat", "gatinho"])
async def catpic(ctx):
    url = get_cat_pics()
    embed = discord.Embed(title="meow 🐱")
    embed.set_image(url=url)
    await ctx.send(embed=embed)

# API is buggy
# @bot.command(aliases=["dog", "cão", "doguinho", "cãozinho"])
# async def dogpic(ctx):
#     url = get_dog_pics()
#     file_format = url.split(".")[-1]
#     if file_format == "jpeg" or file_format == "jpg":
#         embed = discord.Embed(title="woof 🐶")
#         embed.set_image(url=url)
#         await ctx.send(embed=embed)
#     else:
#         embed = discord.Embed(title="woof 🐶")
#         embed.add_field(
#             name="Sorry, image not found 🙁",
#             value="that's unfortunate, but no good boyz were available for the photo shooting"
#         )

@bot.command(aliases=["fox", "raposa"])
async def foxpic(ctx):
    url = get_fox_pics()
    embed = discord.Embed(title="WHAT DOES THE FOX SAY?? 🦊")
    embed.set_image(url=url)
    await ctx.send(embed=embed)

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

    lenght = len(drink[0]["strInstructions"])

    if len(drink[0]["strInstructions"]) > 1024:
        embed.add_field(name="Instructions", value=drink[0]["strInstructions"][:1024], inline=False)
        lenght -= 1024
        i = 1
        while lenght > 1024:
            embed.add_field(name="...", value=drink[0]["strInstructions"][1024 * i:1024 * (i+1)], inline=False)
            lenght -= 1024
            i += 1
        embed.add_field(name="...", value=drink[0]["strInstructions"][1024 * i:], inline=False)

    else:
        embed.add_field(name="Instructions", value=drink[0]["strInstructions"], inline=False)

    info = str(drink[2]).strip("[]")
    embed.set_footer(text=info)

    await ctx.send(embed=embed)

@bot.command(aliases=["perfil"])
async def profile(ctx, user: discord.Member=None):
    if user:
        author = user
    else:
        author = ctx.author
    roles = [author.roles[i].name for i in range(len(author.roles))]
    str_roles = ", ".join(roles)

    embed = discord.Embed(title=f"{author.name}'s profile")
    if author.name != author.nick and author.nick is not None:
        embed.add_field(name="a.k.a", value=author.nick)
    embed.add_field(name="Joined at", value=author.joined_at.strftime("%Y/%m/%d %H:%M"))
    embed.add_field(name="Roles", value=str_roles, inline=False)
    if author.activities:
        activities = [author.activities[i].name for i in range(len(author.activities))]
        str_activities = ", ".join(activities)
        embed.add_field(name="Now doing", value=str_activities)
    embed.set_image(url=author.avatar_url)

    await ctx.send(embed=embed)


# ------------------- ADMIN COMMANDS --------------------- #
@bot.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, user: discord.Member, *, reason):
    await user.kick(reason=reason)
    await ctx.send(f'{user} kicked for {reason}')


@bot.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, user: discord.Member, *, reason):
    await user.kick(reason=reason)
    await ctx.send(f'{user} banned for {reason}')

# -------------------------------------------------------------- #

# runs the server
B.b()

# runs the bot token.
bot.run(TOKEN)