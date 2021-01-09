import discord
from discord.ext import commands

client = commands.Bot(command_prefix=">")

@client.event
async def on_ready():
    print("Shocko is ready!!!")

@client.command()
async def hello(ctx):
    await ctx.send("Hello")

client.run("r_O428hQZiZMH0RYvtXdXugZM8b8J34w")