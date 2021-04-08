# bot.py
import os

import discord

import get_pdf

TOKEN ='ODI5ODM4MzI4MjI3NDMwNDgy.YG99Kw.nybL-eCr9TquO44lj5PJU97h3KA'

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content == '!':
        
        await message.channel.send(file=discord.File(get_pdf.get_pdf()))   



client.run(TOKEN)