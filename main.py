import discord
from main2 import *

# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('merhaba'):
        await message.channel.send(":smiley:")
    elif message.content.startswith('şifre'):
        await message.channel.send(sifre_uret(10))
    elif message.content.startswith('görüşürüz'):
        await message.channel.send(":wave:")
    else:
        await message.channel.send(message.content)

client.run("MTE0NDMyOTgzOTAxMzI4NTkyOA.Gb3RDK.jLWcJDf2i4qY35Sf2whftQgmoE0yh-G8gHr-VI")