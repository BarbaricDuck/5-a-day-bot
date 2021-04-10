import os
import discord
from discord.ext import commands
from get_pdf import get_pdf
from dotenv import load_dotenv
import datetime

short_months = {'Dec':'December', 'Jan':'January', 'Feb':'Febuary', 'Mar':'March', 'Apr':'April', 'May':'May', 'Jun':'June', 'Jul':'July', 'Aug':'August', 'Sep':'September', 'Oct':'October', 'Nov':'November'}


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
async def corbett(ctx,*args):
  if ctx.author == bot.user:
    return

  month = datetime.datetime.now().strftime("%B")
  day = datetime.datetime.now().strftime("%#d")

  if not args:
    await ctx.send(file=discord.File(get_pdf(month,day), f"5-A-Day ({month} {day}).pdf"))

  else:  


    if args[0].title() in short_months.keys():
      month = short_months[args[0].title()]
    
    elif args[0].title() in short_months.values():
      month = args[0]
    
    if len(args) > 1:
      
      day = args[1]

    if args[0] == 'help':
      await ctx.send('''---5-A-DAY BOT HELP---
*Send !corbett to get current worksheet
*Send !corbett [month] [day] to get specific worksheet

Here is today's worksheet :D''')



      
    await ctx.send(file=discord.File(get_pdf(month,day), f"5-A-Day ({month} {day}).pdf"))


if TOKEN:
  bot.run(TOKEN)
else:
  print("Please provide a token in .env")
