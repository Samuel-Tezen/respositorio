# This example requires the 'members' and 'message_content' privileged intents to function.

import discord
from discord.ext import commands
import random

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='?', description=description, intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


@bot.command()
async def sumar(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def multiplicar(ctx, left: int, right: int):
    """Adds two numbers together."""
    x = left * right
    await ctx.send(x)

@bot.command()
async def dividir(ctx, left: int, right: int):
    """Adds two numbers together."""
    x = left / right
    await ctx.send(x)

@bot.command()
async def restar(ctx, left: int, right: int):
    """Adds two numbers together."""
    x = left - right
    await ctx.send(x)


bot.run('aqui no hay nada xd')
