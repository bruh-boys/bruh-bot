import discord
from discord.ext import commands
from monda import SI
import datetime
import os
import asyncio # To get the exception

@client.command(...)
async def _command(ctx):
    # code
    try:
        msg = await client.wait_for("message", check=check, timeout=30) # 30 seconds to reply
    except asyncio.TimeoutError:
        await ctx.send("Sorry, you didn't reply in time!")

bot.run(SI)