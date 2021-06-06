#discord bot
import os
import random

from discord.ext import commands
from discord import DMChannel
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='drop', help=' - Responds with a random drop location in Verdansk')
async def drop(ctx):
    drop_locations = [
        'Summit',
        'Military Base',
        'Salt Mine',
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
        'Factory',
        'Prison',
        'Array'
    ]

    response = random.choice(drop_locations)
    await ctx.send("Let's go " + response + "!")

@bot.event
async def on_voice_state_update(member, before, current):
    if before.channel is None and current.channel is not None:
        guild = member.guild
        luke = await guild.fetch_member("143615219418005504")
        if luke.id != member.id and luke.voice is None:
            message = member.name + " has joined the " + current.channel.name + " voice channel in " + current.channel.guild.name + " server"
            await DMChannel.send(luke, message)
        
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Sorry, I don't know how to do that. You can type !help to see a list of available commands.")

bot.run(TOKEN)