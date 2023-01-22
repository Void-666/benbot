import discord # Подключаем библиотеку
from discord.ext import commands
import os
import random
import config
intents = discord.Intents.default() # Подключаем "Разрешения"
intents.message_content = True
# Задаём префикс и интенты
bot = commands.Bot(command_prefix=config.prefix, intents=intents) 
benmsg = ["Хо-хо-хо","Ноу","Йес", ":stuck_out_tongue:"]
# С помощью декоратора создаём первую команду
@bot.command()
async def ben(ctx):
    await ctx.send(random.choice(benmsg))


bot.run(config.token)