import os
import discord
from discord.ext import commands
from get_pdf import get_pdf
from dotenv import load_dotenv
import datetime



load_dotenv()

TOKEN = os.getenv('TOKEN')
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
  print(f'{bot.user} has connected to Discord!')
    
# @bot.event
# async def on_message(message):
#   if message.author == bot.user:
#     return
    
#   if message.content == '!corbett':
#     

@bot.command()
async def corbett(ctx,arg):
  if ctx.author == bot.user:
    return
  
  if arg == 'today':
    month = datetime.datetime.now().strftime("%B")
    day = datetime.datetime.now().strftime("%#d")
    
    await ctx.send(file=discord.File(get_pdf(month,day), "5-A-Day.pdf"))

  else:
    
      
    month = arg
    day = 10
    await ctx.send(file=discord.File(get_pdf(month,day), "5-A-Day.pdf"))


if TOKEN:
  bot.run(TOKEN)
else:
  print("Please provide a token in .env")
