import discord
import decouple
from discord.ext import commands
from discord.utils import get

JOHANNSEBASTIANBOT_APP_ID = decouple.config("JOHANNSEBASTIANBOT_APP_ID")
JOHANNSEBASTIANBOT_CLIENT_SECRET = decouple.config("JOHANNSEBASTIANBOT_CLIENT_SECRET")
JOHANNSEBASTIANBOT_PUBLIC_KEY = decouple.config("JOHANNSEBASTIANBOT_PUBLIC_KEY")
JOHANNSEBASTIANBOT_TOKEN = decouple.config("JOHANNSEBASTIANBOT_TOKEN")

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$hello"):
        await message.channel.send("Hello!")


    # Deixa registrado quando alguém entra no server, e adiciona o título de <musicuzinh@>.
@client.event
async def on_member_join(member):

    role = get(member.guild.roles, name='musicuzinh@')
    await member.add_roles(role)
    print(f'{member} has joined the server.')

client.run(JOHANNSEBASTIANBOT_TOKEN)