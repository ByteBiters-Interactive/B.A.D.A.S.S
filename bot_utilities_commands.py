# ---------------------------------------------------------------------- #
# -----------------------------B.A.D.A.S.S------------------------------ #
# ---------------------------------------------------------------------- #

# Imports
import discord
from discord.ext import commands
import bot_utilities as bot_utilities
from bot_core_functionality import core

# Intents
intents = discord.Intents.all() 
intents.message_content = True
intents.members = True 

# Create bot-instance TODO: this needs to be made COG!!
bot = commands.Bot(command_prefix='!', intents=intents)

# ---------------------------------------------------------------------- #


@bot.command(name='initialize')
async def initialize(ctx, channel_name = 'league-of-legends-champion-channel'):
    # Check if the command was already executed on this server (guild)
    server_data = {}
    if ctx.guild:
        guild = ctx.guild

        if bot_utilities.utilities.does_server_already_exists(ctx) == False:
            # Save ServerID as Text File
            myServerID = str(bot_utilities.utilities.get_server_id_from_ctx(ctx))
            serverID =  './Server/'+ myServerID + '.txt'
            file = open(serverID, 'w')
            file.close()
            
            # Create a new text-channel & send a confirmation message
            await guild.create_text_channel(channel_name)
            await ctx.send(f"Channel '{channel_name}' created successfully \nChannel ID: {bot_utilities.utilities.get_bot_channel_id_from_ctx(ctx)} \nServer-ID: {myServerID}")
        else:
            await ctx.send(f"""A channel has already been cretaed on this server! \nIf you deleted the channel or want to proceed for whatever reason, consider using \"!force-initialize\". \nNote: that this is an experimental feature and may not lead to your desired outcome.""")

    else:
        await ctx.send("This command can only be used on a server.")


@bot.command(name='force-initialize')
async def force_initialize(ctx, channel_name = 'league-of-legends-champion-channel'):
    if ctx.guild:
        guild = ctx.guild

        # Create a new text-channel & send a conformation message 
        await guild.create_text_channel(channel_name)
        await ctx.send(f"Channel '{channel_name}' created successfully \nChannel ID: {bot_utilities.utilities.get_bot_channel_id_from_ctx(ctx)} \nServer-ID: {bot_utilities.utilities.get_server_id_from_ctx(ctx)}")
    else:
         await ctx.send(f"A channel already exists on this Server.")


@bot.command(name='start')
async def start(self):
    await core.do_your_stuff.start(self)


# ---------------------------------------------------------------------- #
         

# Every extension should have this function
async def setup(bot):
    bot.add_command(initialize)
    bot.add_command(force_initialize)
    bot.add_command(start)
    print(f'Module: \"utilities_bot_commands\" loaded successfully')


# ---------------------------------------------------------------------- #
# Copyright 2024 by Sylvan013 & Anderson4366
