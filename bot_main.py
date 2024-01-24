# ---------------------------------------------------------------------- #
# -----------------------------B.A.D.A.S.S------------------------------ #
# ---------------------------------------------------------------------- #

# Imports (discord.py neccassary)
import discord
from discord.ext import commands
from datetime import datetime

# Intents
intents = discord.Intents.all()
intents.message_content = True
intents.members = True

# Create bot-instance
bot = commands.Bot(command_prefix='!', intents=intents)

# Variables
welcome_message = f'\033[1mBA\033[0mdly coded \033[1mD\033[0miscord Game \033[1mA\033[0mnnouncement \033[1mS\033[0mystem for \033[1mS\033[0mervers'
token_path = 'resources/token.txt' 
try:
    with open(token_path, 'r') as file:
        token = file.read()
except FileNotFoundError:
    print(f'[{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}]: The file \'{token_path}\' does not exist.')
    exit()
except Exception as error:
    print(f'[{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}]: An error occurred while loading the bot token: {error}')
    exit()

# ---------------------------------------------------------------------- #


# on_ready()-function. Prints startup informations and loads extentions 
@bot.event
async def on_ready():

    print(   ) #////////////////////////#
    
    print(f'Codename: B.A.D.A.S.S ({welcome_message})\n')
    print(f'[{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}]:\nBot is online as: \"{bot.user.name}\"!\t[Bot-ID: {bot.user.id}]\n\n')
    print(f'\033[4mConnected to the following servers:\033[0m') 
    for server in bot.guilds:
        print(f'Server: {server}\tServer-ID: {server.id}')

    print('\n') #////////////////////////#

    print(f'\033[4mThe following Extentions were loaded:\033[0m') 
    await bot.load_extension('bot_utilities_commands')
    await bot.load_extension('bot_commands')
    await bot.load_extension('bot_utilities')
    await bot.load_extension('bot_core_functionality')

    print(   ) #////////////////////////#
    print('---------------------------------------------------------')


# ---------------------------------------------------------------------- #


# Run the bot with the token
bot.run(token)


# ---------------------------------------------------------------------- #
# Copyright 2024 by Sylvan013 & Anderson4366
