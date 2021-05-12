import discord
from discord.ext import commands
from discord.flags import Intents
from accounts import SI  # SI its the token
import datetime
import os
import re
from discord.ext.commands import cooldown, BucketType

bot = commands.Bot(command_prefix='*', intents=discord.Intents.default(),
                   description="sms and email spam bot!")


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name=f"ready | *info | in {len(bot.guilds)} servers"))
    print("bot on")


@bot.command()
async def info(ctx):
    await bot.change_presence(activity=discord.Game(name=f"ready | *info | in {len(bot.guilds)} servers"))
    embed3 = discord.Embed(title="invitation link!",
                           url="https://discord.com/oauth2/authorize?client_id=817060522067099679&permissions=51200&scope=bot",
                           color=0x00ffff)
    embed3.add_field(name="Email example:", value="*email hello@gmail.com")
    embed3.add_field(name="SMS example:", value="*sms +3231231231")
    await ctx.send(embed=embed3)


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):  # checks if is on cooldown
        em = '**on cooldown**, please try again in {:.2f}s'.format(
            error.retry_after)
        await ctx.send(em)


@bot.command()
@commands.cooldown(2, 20, commands.BucketType.user)
async def sms(ctx, arg):

    validate = re.findall("\+?[\d]{10,14}", arg)
    if not validate:
        embed10 = discord.Embed(
            title="you didn't pass with a +, or is not a number, or did you pass it with spaces, example: *sms +22123456789", color=330000)
        await ctx.send(embed=embed10)
        return
    embed = discord.Embed(title="the spam takes between takes 2 minutes",
                          color=0x00ff00, timestamp=datetime.datetime.utcnow())
    await ctx.send(embed=embed)
    await bot.change_presence(activity=discord.Game(name=f"busy | *info | in {len(bot.guilds)} servers"))
    os.system(
        f"cd quack ; python3 quack --tool SMS --target  {validate[0]} --threads 60 --timeout 90")
    embed2 = discord.Embed(title="sms spam completed! :skull:",
                           color=0x00ff00, timestamp=datetime.datetime.utcnow())
    await bot.change_presence(activity=discord.Game(name=f"ready | *info | in {len(bot.guilds)} servers"))
    await ctx.send(embed=embed2)


@bot.command()
@commands.cooldown(2, 20, commands.BucketType.user)
async def email(ctx, arg):
    validateEmail = re.findall(
        "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", arg)
    if not validateEmail:
        embed11 = discord.Embed(
            title="you didn't pass a valid email, example: *email hello@gmail.com", color=330000)
        await ctx.send(embed=embed11)
        return

    embed4 = discord.Embed(title="spam sent! takes 1 minute ", color=000000)
    await ctx.send(embed=embed4)
    await bot.change_presence(activity=discord.Game(name=f"busy | *info | in {len(bot.guilds)} servers"))
    os.system("rm tools/EMAIL/sender.json")
    os.system(
        f"python3 impulse.py --method EMAIL --time 60 --target {validateEmail[0]}")
    embed5 = discord.Embed(title=" email spam completed!",
                           color=0x00ff00, timestamp=datetime.datetime.utcnow())
    await bot.change_presence(activity=discord.Game(name=f"ready | *info | in {len(bot.guilds)} servers"))
    await ctx.send(embed=embed5)


bot.run(SI)
