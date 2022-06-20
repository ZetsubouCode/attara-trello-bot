import discord
from .__env import ENV

client = discord.Client()

@client.event
async def on_ready():
    print("we have logged in successfully as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user or message.channel.name != 'bot-test':
        return
    
    if message.content.startswith('!help'):
        await message.channel.send()

    if message.content.startswith('!showtask'):
        await message.channel.send()

client.run(ENV.TOKEN)