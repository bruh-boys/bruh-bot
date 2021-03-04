import discord
from discord.ext import commands
from monda import SI
import datetime
import os

bot = commands.Bot(command_prefix='*', description="Test bot")
# Event
@bot.event
async def on_ready():
   await bot.change_presence(activity=discord.Streaming(name="paiwebb.herokuapp.com", url="https://twitch.tv/monda"))
   print("\033[4;35m"+"bot on")


@bot.command()
async def ping(ctx):
   await ctx.send('pong')


@bot.command()
async def atack(ctx):
      embed = discord.Embed(title ="the attack takes between 4-5 minutes", color=0x00ff00, timestamp=datetime.datetime.utcnow())
      await ctx.send(embed=embed)
      #os.system("cd quack ; python3 quack --tool SMS --target  number --threads 60 --timeout 90")
      #os.system("python3 impulse.py --method SMS --time 90 --threads 60 --target  number")
      embed2 = discord.Embed(title ="atack completed! :skull:" ,color=0x00ff00,  timestamp=datetime.datetime.utcnow())
      await ctx.send(embed=embed2)
      

bot.run(SI)



