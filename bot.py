#pip install discord
import discord
import datetime
import asyncio
 
intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents=intents,activity=discord.Game(name='Dead by Daylight'))

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    while True:
        
        now = datetime.datetime.now()
        
        if now.weekday() == 2 and now.hour == 5:
            
            user = await client.fetch_user(262321327992471553)
            user2 = await client.fetch_user(410841879161339905)
            
            await user.send(file=discord.File('screenshot.png'))
            await user.send("Here is the new Shrine!")
            await user2.send(file=discord.File('screenshot.png'))
            await user2.send("Here is the new Shrine!")
        
        await asyncio.sleep(3600)

client.run('MTA2MjA2Mjc4NTQwNTY1MzAzMg.GG7uBD.7srWcTHApNPXmgTLFwQlvE3N6fX9ga7Uvmw7NQ')
