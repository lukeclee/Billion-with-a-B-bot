#discord bot
import os
import random

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='drop', help='Responds with a random drop location in Verdansk')
async def drop(ctx):
    drop_locations = [
        'Dam',
        'Military Base',
        'Quarry',
        'Airport',
        'TV Station',
        'Bridge Town',
        'Storage Town',
        'Superstore',
        'Stadium',
        'Lumber',
        'Boneyard',
        'Train Station',
        'Hospital',
        'Downtown',
        'Farmland',
        'Promenade West',
        'Promenade East',
        'Hills',
        'Park',
        'Port',
        'Shipwreck',
        'Prison'
    ]

    response = random.choice(drop_locations)
    await ctx.send("Let's go " + response + "!")

bot.run(TOKEN)