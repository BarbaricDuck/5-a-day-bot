import os
import discord
from discord.ext import commands
from get_pdf import get_pdf
from dotenv import load_dotenv
import datetime

print("Hello, I'm running!")

short_months = {'Dec':'December', 'Jan':'January', 'Feb':'February', 'Mar':'March', 'Apr':'April', 'May':'May', 'Jun':'June', 'Jul':'July', 'Aug':'August', 'Sep':'September', 'Oct':'October', 'Nov':'November'}


load_dotenv()

TOKEN = os.getenv('TOKEN')
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
  print(f'{bot.user} has connected to Discord!')


@bot.command()
async def corbett(ctx,*args):
  if ctx.author == bot.user:
    return

  answers = False

  month = datetime.datetime.now().strftime("%B")
  day = datetime.datetime.now().strftime("%#d")

  if not args:
    await ctx.send(file=discord.File(get_pdf(month,day,answers), f"5-A-Day ({month} {day}).pdf"))

  else:  

    if args[0].title() == 'Answers':
      answers = True

    if args[0].title() in short_months.keys():
      month = short_months[args[0].title()]
    
    elif args[0].title() in short_months.values():
      month = args[0].title()
    
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

    if len(args) > 2:
      if args[2].title == 'Answers':
        answers = True

    if args[0] == 'help':
      await ctx.send('''```---5-A-DAY BOT HELP---

Github: https://github.com/bengroves2004/5-a-day-bot

*Send !corbett to get current worksheet
*Send !corbett [month] [day] to get specific worksheet
*Send !corbett answers to get current answers
*Send !corbett [month] [day] answers to get current answers

Here is today's worksheet :D```''')

    await ctx.send(file=discord.File(get_pdf(month,day,answers), f"5-A-Day ({month} {day}).pdf"))

if TOKEN:
  bot.run(TOKEN)
else:
  print("Please provide a token in .env")
