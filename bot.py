import os
import discord
from get_pdf import get_pdf
from dotenv import load_dotenv
import datetime

month = datetime.datetime.now().strftime("%B")
day = datetime.datetime.now().strftime("%#d")

load_dotenv()

TOKEN = os.getenv('TOKEN')
client = discord.Client()

@client.event
async def on_ready():
  print(f'{client.user} has connected to Discord!')
    
@client.event
async def on_message(message):
  if message.author == client.user:
    return
    
  if message.content == '!corbett':
    await message.channel.send(file=discord.File(get_pdf(month,day), "5-A-Day.pdf"))   


if TOKEN:
  client.run(TOKEN)
else:
  print("Please provide a token in .env")
