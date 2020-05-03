import discord
from discord.ext import commands
from requests import get


token = ''
client = commands.Bot(command_prefix = ".")

@client.event
async def on_ready():
    print('ready')
@client.event
async def on_message(message):
        # don't respond to ourselves
        if message.author == client.user:
            return

        if str(message.content).lower() == 'get ip':
            ip = get('https://api.ipify.org').text
            await message.channel.send(ip)
            
            
if __name__ == "__main__":
    with open('token.txt' , 'r') as token_file:
        token = token_file.read()
        token_file.close()
    client.run(token)   