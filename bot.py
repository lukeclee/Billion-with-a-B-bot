#discord bot
import os
import random
import datetime

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

@bot.command(name='drip', help=' - Rates your fit!')
async def drip(ctx):
    rate = str(random.randint(0, 11))
    await ctx.send("I rate your fit " + rate + "/10!")

@bot.command(name='8ball', help=' - Responds with a fortune just like a Magic 8-Ball')
async def eightBall(ctx):
    ball_responses = [
        'It is certain.',
        'It is decidedly so.',
        'Without a doubt.',
        'Yes, definitely.',
        'You may rely on it',
        'As I see it, yes.',
        'Most likely.',
        'Outlook good.',
        'Yes.',
        'Signs point to yes.',
        'Reply hazy try again',
        'Ask again later.',
        'Better not tell you now.',
        'Cannot predict now.',
        'Concentrate and ask again.',
        'Don\'t count on it.',
        'My reply is no.',
        'My sources say no.',
        'Outlook not so good.',
        'Very doubtful.'
    ]

    fortune = random.choice(ball_responses)
    await ctx.send(fortune)

@bot.command(name='roll', help=' - Responds with a value from rolled dice')
async def roll(ctx, arg1, arg2):
    diceNum = int(arg1)
    die = int(arg2[1:])
    #diceNum = 1
    #die = 20
    result = 0
    for i in range(diceNum):
        result += random.randint(1, die)
    
    await ctx.send("You rolled " + str(diceNum) + " d" + str(die) + " and got " + str(result) + ".")

@bot.event
async def on_voice_state_update(member, before, current):
    if before.channel is None and current.channel is not None:
        guild = member.guild
        luke = await guild.fetch_member("143615219418005504")
        if luke.id != member.id and luke.voice is None:
            message = member.name + " has joined the " + current.channel.name + " voice channel in " + current.channel.guild.name + " server"
            await DMChannel.send(luke, message)

        if len(current.channel.members) < 2 and datetime.datetime.today().weekday() == 3:
            listOfTextChannels = guild.text_channels
            channelToSendMessage = listOfTextChannels[0]
            roleToMention = guild.get_role(905328272827641856)
            await channelToSendMessage.send(roleToMention.mention + ", " + member.name + " has joined the " + current.channel.name + " voice channel for Throwdown Thursday and is lonely! :(")
        
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Sorry, I don't know how to do that. You can type !help to see a list of available commands.")

bot.run(TOKEN)