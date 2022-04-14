import discord, asyncio, os
import random
import os
from discord.ext import commands, tasks
import re
import string

count = 0
thing = os.listdir("/app")

belleset1 = ("D:\\Bots and stuff\\Kazuma 2.0\\maxresdefault.jpg")

client = commands.Bot(command_prefix = "~", case_insensitive=True)
game = discord.Game("I am the true God in here!")
client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=game)
    print("Successfully connected.....Yakuza Time!")

@client.event
async def on_member_join(member):
    print(f'{member} Has joined our Yakuza family')

@client.event
async def on_member_remove(member):
    print(f'{member} Has left without their pinky')
   
@client.event
async def on_command_error(ctx, error):
    await ctx.send('I am a gentleman. And I am gently telling you to LEARN THE FUCKING COMMANDS. Thank you <3')

@client.command()
async def GroundPound(ctx, member : discord.Member):
 
    path = r"/app/Gifs/"
    random_filename = random.choice([
        x for x in os.listdir(path)
        if os.path.isfile(os.path.join(path, x))
    ])
    actual_file = f"{path}/{random_filename}" 
    await ctx.send(f"{ctx.author.mention} Ground Pounded {member.mention}'s mom")
    await ctx.send(file = discord.File(actual_file))

@client.command()
async def Korone(ctx):
 
    path = r"/app/Dominance/"
    random_filename = random.choice([
        x for x in os.listdir(path)
        if os.path.isfile(os.path.join(path, x))
    ])
    actual_file = f"{path}/{random_filename}" 
    await ctx.send(file = discord.File(actual_file))

@client.command()
async def Oyasumi(ctx):
 
    path = r"/app/Oyasumi/"
    random_filename = random.choice([
        x for x in os.listdir(path)
        if os.path.isfile(os.path.join(path, x))
    ])
    actual_file = f"{path}/{random_filename}" 
    await ctx.send(file = discord.File(actual_file))

@client.command()
async def Yes(ctx):
 
    path = r"/app/Yes/"
    random_filename = random.choice([
        x for x in os.listdir(path)
        if os.path.isfile(os.path.join(path, x))
    ])
    actual_file = f"{path}/{random_filename}" 
    await ctx.send(file = discord.File(actual_file))

@client.command()
async def No(ctx):
 
    path = r"/app/No/"
    random_filename = random.choice([
        x for x in os.listdir(path)
        if os.path.isfile(os.path.join(path, x))
    ])
    actual_file = f"{path}/{random_filename}" 
    await ctx.send(file = discord.File(actual_file))

@client.command()
async def Ping(ctx):
 
    path = r"/app/Ping/"
    random_filename = random.choice([
        x for x in os.listdir(path)
        if os.path.isfile(os.path.join(path, x))
    ])
    actual_file = f"{path}/{random_filename}" 
    await ctx.send(file = discord.File(actual_file))

@client.command()
async def Muted(ctx):
 
    path = r"/app/Muted/"
    random_filename = random.choice([
        x for x in os.listdir(path)
        if os.path.isfile(os.path.join(path, x))
    ])
    actual_file = f"{path}/{random_filename}" 
    await ctx.send(file = discord.File(actual_file))

@client.command()
async def WTF(ctx):
 
    path = r"/app/WTF/"
    random_filename = random.choice([
        x for x in os.listdir(path)
        if os.path.isfile(os.path.join(path, x))
    ])
    actual_file = f"{path}/{random_filename}" 
    await ctx.send(file = discord.File(actual_file))

@client.command()
async def WTF(ctx):
 
    path = r"/app/WTF/"
    random_filename = random.choice([
        x for x in os.listdir(path)
        if os.path.isfile(os.path.join(path, x))
    ])
    actual_file = f"{path}/{random_filename}" 
    await ctx.send(file = discord.File(actual_file))

@client.command()
async def STFU(ctx):
 
    path = r"/app/STFU/"
    random_filename = random.choice([
        x for x in os.listdir(path)
        if os.path.isfile(os.path.join(path, x))
    ])
    actual_file = f"{path}/{random_filename}" 
    await ctx.send(file = discord.File(actual_file))

@client.command()
async def Mata_ne(ctx):
 
    path = r"/app/Mata ne/"
    random_filename = random.choice([
        x for x in os.listdir(path)
        if os.path.isfile(os.path.join(path, x))
    ])
    actual_file = f"{path}/{random_filename}" 
    await ctx.send(file = discord.File(actual_file))

@client.command()
async def Omg(ctx):
 
    path = r"/app/OMG/"
    random_filename = random.choice([
        x for x in os.listdir(path)
        if os.path.isfile(os.path.join(path, x))
    ])
    actual_file = f"{path}/{random_filename}" 
    await ctx.send(file = discord.File(actual_file))

@client.command()
async def Gay(ctx):
    await ctx.send(thing)

@client.command()
async def Programmer(ctx):
    await ctx.send('https://cdn.discordapp.com/attachments/674392982530555904/784872349521936404/video0_4-5.mp4')

@client.command()
async def Bullsquid(ctx):
    await ctx.send('https://bullsquid.com/')

@client.command()
async def Hello(ctx):
    await ctx.send('Who the FUCK are you?')

@client.command()
async def Gary(ctx):
    await ctx.send('Gaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaay')


#@client.command()
#async def Belle(ctx):
 #   if (discord.TextChannel.is_nsfw(ctx.channel) is True):
  #  
   #     path = r"/app/Belle no enter/"
    #    random_filename = random.choice([
     #       x for x in os.listdir(path)
      #      if os.path.isfile(os.path.join(path, x))
       # ])
        #actual_file = f"{path}/{random_filename}"
        #await ctx.send(file = discord.File(actual_file))
    #else:
     #   await ctx.send("Hmmmmm you like to watch this shit in public. Disgusting")

@client.command()
async def World(ctx):
    while count < 5:
        await ctx.send('Around the world, Around the world, Around the world, Around the world, Around the world, Around the world, Around the world, Around the world, Around the world, Around the world, Around the world, Around the world, Around the world, Around the world, Around the world, Around the world, Around the world, Around the world, Around the world, Around the world, Around the world, Around the world, Around the world, Around the world, Around the world, Around the world, Around the world, Around the world, Around the world, Around the world, Around the world, Around the world, Around the world, Around the world, Around the world, Around the world, Around the world, Around the world, Around the world, Around the world, Around the world, Around the world, Around the world, Around the world, Around the world, Around the world, Around the world, Around the world, Around the world, Around the world, Around the world, Around the world, Around the world, Around the world, Around the world, Around the world,')
        count + 1

    
@client.command()
async def Gm(ctx):

    path = r"/app/gm/"
    random_filename = random.choice([
        x for x in os.listdir(path)
        if os.path.isfile(os.path.join(path, x))
    ])
    actual_file = f"{path}/{random_filename}"
    await ctx.send(file = discord.File(actual_file))


@client.command()
async def help(ctx):
    embed = discord.Embed(
        title = '~Help',
        description = 'List of Commands',
        colour = discord.Color.green()
    )

    embed.set_footer(text = 'Patrick will beat your ass')
    embed.set_thumbnail(url='https://static.wikia.nocookie.net/yakuza/images/c/c2/Screen_Shot_2018-02-06_at_5.48.36_AM.png/revision/latest?cb=20190504065053')
    embed.set_author(name='Kazuma',
    icon_url='https://static.wikia.nocookie.net/yakuza/images/c/c2/Screen_Shot_2018-02-06_at_5.48.36_AM.png/revision/latest?cb=20190504065053')
    embed.add_field(name='~Hello', value='No', inline=False)
    embed.add_field(name='~8ball', value='Ask me anything', inline=False)
    embed.add_field(name='~Belle', value='Sends image of Belle Delphine in nsfw channels', inline=False)
    embed.add_field(name='~Lamu', value='Sends image of Lamu', inline=False)
    embed.add_field(name='~Programmer', value='I question my master\'s Decisions', inline=False)
    embed.add_field(name='~GroundPound', value='Ground Pounds any user (~GroundPound @Target)', inline=False)
    embed.add_field(name='~Dominance', value='Dominates any user (~Dominance @Target)', inline=False)
    embed.add_field(name='~Bullsquid', value='B U L L S Q U I D', inline=False)

    await ctx.send(embed=embed)

@client.command(aliases = ['8ball'])
async def _8ball(ctx, *, question):
    responses = ['Fuck Off',
                 'Fuck You',
                 'Fuck Yes',
                 'Probably?',
                 'Ask Patrick',
                 'David knows',
                 'Keith said Androw Furry',
                 'My Master would have answered you by telling you \"Lamù best waifu\" ',
                 'Hmmm',
                 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2F78.media.tumblr.com%2F8a5a0b70bfa2f0b3a6524598ccbb5acf%2Ftumblr_otdcn0YmAx1s7o6cuo1_500.gif&f=1&nofb=1'
                 ]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

#@client.event
#async def on_message(message):
#    separators = string.punctuation+string.digits+string.whitespace
#    excluded = string.ascii_letters
#
#    word = "avatar"
#    formatted_word = f"[{separators}]*".join(list(word))
#    regex_true = re.compile(fr"{formatted_word}", re.IGNORECASE)
#    regex_false = re.compile(fr"([{excluded}]+{word})|({word}[{excluded}]+)", re.IGNORECASE)
#    
#    if regex_true.search(message.content) is not None and regex_false.search(message.content) is None:
#
#        await message.channel.purge(limit = 1)
#        await message.channel.send('Stfu scrub, go and love Korone <3')
#    else:


client.run('NTk1MzE5MjUyODMyMjIzMjQz.XRpQQg.VXRQm31XDCcQaQW-ydAsybMhCqA')