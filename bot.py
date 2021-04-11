import os
import discord
from discord.ext import commands
from get_pdf import get_pdf
import datetime
from boto.s3.connection import S3Connection


short_months = {'Dec':'December', 'Jan':'January', 'Feb':'February', 'Mar':'March', 'Apr':'April', 'May':'May', 'Jun':'June', 'Jul':'July', 'Aug':'August', 'Sep':'September', 'Oct':'October', 'Nov':'November'}



s3 = S3Connection(os.environ['88a9d7c3-47cb-4ca3-8faf-56d47a11f622'], os.environ['TOKEN'])
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
  print(f'{bot.user} has connected to Discord!')


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

      if any(char.isdigit() for char in args[1]) is True:
        if int(args[1]) > 0:
          if month in ['January','March','May','July','August','October','December']:
            if int(args[1]) < 32:
              day = args[1]
          elif month in ['April','June','September','November']:
            if int(args[1]) < 31:
              day = args[1]
          else:
            if int(args[1]) < 30:
              day = args[1]

    if args[0] == 'help':
      await ctx.send('''```---5-A-DAY BOT HELP---
*Send !corbett to get current worksheet
*Send !corbett [month] [day] to get specific worksheet

Here is today's worksheet :D```''')



      
    await ctx.send(file=discord.File(get_pdf(month,day), f"5-A-Day ({month} {day}).pdf"))

if TOKEN:
  bot.run(TOKEN)
else:
  print("Please provide a token in .env")
