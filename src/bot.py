import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import requests

load_dotenv()
api = 'https://api-bruh-bot.elpanajose.repl.co'
token = os.getenv('TOKEN')

bot = commands.Bot(command_prefix='*', help_command=None, intents=discord.Intents.default(),
                   description="sms and email spam bot!")


""" events """


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name=f"*help | in {len(bot.guilds)} servers"))
    print("bot on")


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):  # checks if is on cooldown
        em = '**on cooldown**, please try again in {:.2f} seconds'.format(
            error.retry_after)
        await ctx.send(em)


""" commands """

# sms


@bot.command()
@commands.cooldown(2, 300, commands.BucketType.user)
async def sms(ctx, arg):

    sms_request = requests.post(f'{api}/sms',
                                json={"phone": arg})
    embed_sms = discord.Embed(title="SMS spam!", color=0x7f467f)
    embed_sms.add_field(name="Api response", value=sms_request.text)
    await ctx.send(embed=embed_sms)

# help


@bot.command()
async def help(ctx):
    await bot.change_presence(activity=discord.Game(name=f"*help | in {len(bot.guilds)} servers"))
    embed3 = discord.Embed(title="invitation link!",
                           url="https://discord.com/oauth2/authorize?client_id=817060522067099679&permissions=51200&scope=bot",
                           color=0x00ffff)
    embed3.add_field(name="Email example:", value="*email hello@gmail.com")
    embed3.add_field(name="SMS example:", value="*sms +3231231231")
    await ctx.send(embed=embed3)

# email


@bot.command()
@commands.cooldown(2, 300, commands.BucketType.user)
async def email(ctx, arg):
    email_request = requests.post(f'{api}/email',
                                  json={"email": arg})
    embed_email = discord.Embed(title="Email spam!", color=0xa6b4e3)
    embed_email.add_field(name="Api response:", value=email_request.text)
    await ctx.send(embed=embed_email)
    await ctx.send("This command is under maintenance, More info in https://github.com/bruh-boys/api-bruh-bot")


bot.run(token)
