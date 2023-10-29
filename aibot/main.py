import discord
from discord.ext import commands
from model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
 
            await attachment.save(f'./images/{file_name}')

            class_name = get_class(f'./images/{file_name}')
            if class_name == 'Portret':
                await ctx.send('I think this picture is a portrait')
            elif class_name == 'Peizazh':
                await ctx.send('Isn`t that a landscape?')
            elif class_name == 'Naturmort':
                await ctx.send('It`s definitely a still-life!')
            elif class_name == 'Animalistika':
                await ctx.send('Maybe its animalistic?')
    else:
        await ctx.send("В сообщении отсутствуют вложения с изображениями.")    

bot.run("token")
