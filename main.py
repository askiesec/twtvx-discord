import discord
import asyncio
import urllib.parse

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if 'https://twitter.com/' in message.content:
        message.delete()
        newuri = urllib.parse.urlparse(message.content)._replace(netloc="vxtwitter.com")
        await asyncio.sleep(1)
        await message.channel.send(urllib.parse.urlunparse(newuri))
        
client.run('')
