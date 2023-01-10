#pip install discord
import discord
 
intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents=intents)
 
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
 
@client.event
async def on_message(message):
    print("message-->", message)
    if message.author == client.user:
        return
 
    if message.content.startswith('hi'):
        await message.channel.send('Hello!')

    if message.content.startswith('shrine?'):
        await message.channel.send(file=discord.File('screenshot.png'))
        await message.channel.send('@z0hnan Here is the new Shrine!')

client.run('MTA2MjA2Mjc4NTQwNTY1MzAzMg.GSjSpz.s2nUkSDWCaEgaLLFI2g1dSSwZw8gWlgY5vypbg')