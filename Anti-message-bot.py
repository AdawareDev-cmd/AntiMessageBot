import discord
from discord.ext import commands
from discord import client

client = commands.Bot(command_prefix = 'Insert Your Prefix Here')

print("START")
token = "Insert Your Token Here"


@client.event
async def on_message(ctx):
  await ctx.channel.purge(limit=1)

client.run(token)