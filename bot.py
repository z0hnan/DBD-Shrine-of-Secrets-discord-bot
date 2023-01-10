#pip install discord
#pip install schedule
import discord
import time
import schedule
 
intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents=intents,activity=discord.Game(name='Dead by Daylight'))

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

def job():
    #user = client.get_user(262321327992471553)
    #user.send(file=discord.File('screenshot.png'))
    #user.send("Here is the new Shrine!")
    print("JOB")



client.run('MTA2MjA2Mjc4NTQwNTY1MzAzMg.GSjSpz.s2nUkSDWCaEgaLLFI2g1dSSwZw8gWlgY5vypbg')
