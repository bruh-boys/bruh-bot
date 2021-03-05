import discord
from discord.ext import commands
from monda import SI
import datetime
import os
import time

bot = commands.Bot(command_prefix='*', description="Test bot")
# Event
@bot.event
async def on_ready():
   await bot.change_presence(activity=discord.Streaming(name="*info", url="https://twitch.tv/monda"))
   print("\033[4;35m"+"bot on")


@bot.command()
async def info(ctx):
   embed3 = discord.Embed(title ="""commands:

EMAIL: *email test@test.com

SMS: *sms +573221243431""", color=0x00ff00)
   await ctx.send(embed=embed3)


@bot.command()
async def sms(ctx,arg):
      embed = discord.Embed(title ="the attack takes between 1-2 minutes", color=0x00ff00, timestamp=datetime.datetime.utcnow())
      await ctx.send(embed=embed)
      os.system(f"cd quack ; python3 quack --tool SMS --target  {arg} --threads 60 --timeout 90")
      #os.system(f"python3 impulse.py --method SMS --time 90 --threads 60 --target {arg} ")
      embed2 = discord.Embed(title ="atack completed! :skull:" ,color=0x00ff00,timestamp=datetime.datetime.utcnow())
      await ctx.send(embed=embed2)

@bot.command()
async def email(ctx,arg):
     embed4 = discord.Embed(title ="spam sent!", color=000000)
     await ctx.send(embed=embed4)
     os.system(f"python3 impulse.py --method EMAIL --time 20 --threads 15 --target {arg}")
     embed5 = discord.Embed(title ="atack completed!", color=0x00ff00, timestamp=datetime.datetime.utcnow())
     await ctx.send(embed=embed5)

      
bot.run(SI)



