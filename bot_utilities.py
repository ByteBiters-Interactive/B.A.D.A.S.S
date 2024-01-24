# ---------------------------------------------------------------------- #
# -----------------------------B.A.D.A.S.S------------------------------ #
# ---------------------------------------------------------------------- #

# Imports
import os
import discord
from discord.ext import commands
from database.bot_sql import get_insult_from_database, get_db_login
from datetime import datetime
import json

# Variables
try:
    with open('resources/config.json', 'r') as file:
        config_data = json.load(file)
except FileNotFoundError:
    print(f'[{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}]: The file \'resources/config.json\' does not exist.')
    exit()
except Exception as error:
    print(f'[{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}]: An error occurred while loading config data: {error}')
    exit()

try:
    game_scope = config_data.get('game_scope', 'League of Legends')
except Exception as error:
    print(f'[{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}]: An error ocured while reading \'game_scope\' from config data: ({error})')

lol_players = set()
all_lol_players = set()
new_lol_players = set()
temp = set()

player_counter = 5
new_player_counter = 0
who_left_counter = 0
who_came_counter = 0

who_came_baseline = set()
who_left_baseline = set()

# ---------------------------------------------------------------------- #


class utilities(commands.Cog):
    def __init__(self, bot):
            self.bot = bot
    
    def get_bot_channel_id_from_ctx(ctx): 
        channel = discord.utils.get(ctx.guild.channels, name = 'league-of-legends-champion-channel')
        return channel.id

    def get_server_id_from_ctx(ctx): 
        return ctx.guild.id

    def does_server_already_exists(ctx):
        directory = "./server"
        try:
            # Get a list of all files in the specified directory
            files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
            serverID_txt = str(utilities.get_server_id_from_ctx(ctx))+'.txt'
            if serverID_txt in files:
                return True
            else: 
                return False
        except Exception as error:
            print(f'[{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}]: An error occurred while checking if server is already registered: {error}')
            return False

    # This function updates / fills the "all_members" array with all the members of a Server. (maybe udate in the future to work on multiple servers)
    def list_members_of_server(server_object):
        server_members = []
        for member in server_object.members:
            server_members.append(str(member))
        return server_members

    # This function returns an arryay, containing all the server-IDs of the servers the player is on. 
    async def get_servers_from_player_id(self, player_id):
        player_servers = []
        for server in self.bot.guilds:
            member_ids = [member.id for member in server.members]
            if player_id in member_ids:
                player_servers.append(server.id)
        return player_servers

    # leauge_chekcer()-function. Returns an array off all the guild members, playing League of Legends at the momemnt.
    def league_checker(self):
        import bot_utilities as local
        local.player_counter = 0
        for guild in self.bot.guilds:
            for member in guild.members:
                for activity in member.activities:
                    if activity.name == local.game_scope and len(str(activity)) > 20: # Workaround for custom activity status
                        local.lol_players.add(member.id)
                        local.player_counter += 1

            print(guild.name, ':\t\t', local.player_counter, ' LoL-Players online.')
            local.player_counter = 0

        local.new_lol_players = utilities.new_players(lol_players)
        local.lol_players = set()


    def who_left(lol_players):
        import bot_utilities as local
        
        if local.who_left_counter == 0:
            local.who_left_baseline.update(lol_players)
            local.who_left_counter += 1
            return(set())
        else: 
            left = local.who_left_baseline.difference(lol_players)
            if lol_players:
                local.who_left_baseline = lol_players
            else:
                local.who_left_baseline = set()
              
        local.who_left_counter += 1
        return(left)
        
    def who_came(lol_players):
        import bot_utilities as local
    
        if local.who_came_counter == 0:
            local.who_came_baseline.update(lol_players)
            local.who_came_counter += 1
            return(lol_players)
        else:
            came = lol_players.difference(local.who_came_baseline) # Delete the people that left from baseline / set baseline to lol_players
            if lol_players:
                local.who_came_baseline = lol_players
            else:
                local.who_came_baseline = set()

        local.who_came_counter += 1
        return came

    def new_players(lol_players):
        import bot_utilities as local
        if local.new_player_counter == 0:
            local.new_player_counter += 1
            return utilities.who_came(lol_players)
        local.new_player_counter += 1
        return utilities.who_came(lol_players)
            
    def get_champ_name_from_player_id(self, player_id, server):  
        player_server = self.bot.get_guild(server)
        player_object = player_server.get_member(player_id)
        try:
            champ_name = str(player_object.activity.large_image_text).replace(' ', '')
            return champ_name.replace('&', '')
        except Exception as error:
            print(f'[{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}]: An error occurred while retrieving champ name from player. {error}. Is palyer still playing League of Legends?')
            return 'None'

    # Send a message for every player that plays LoL with an insult based on the champ picked
    async def send_message(channel, player, champ):
        insult_to_send = await get_insult_from_database(await get_db_login(), champ)
        if insult_to_send is not None:
            await channel.send(f'<@{player}> is playing {champ}. ' + insult_to_send)
        else:
            return

    async def announce_players(self):
        import bot_utilities as local
        for player in local.new_lol_players:
            player_servers = await utilities.get_servers_from_player_id(self, player)
            for server in player_servers:
                local_server = self.bot.get_guild(server)
                local_lol_channel = discord.utils.get(local_server.channels, name = 'league-of-legends-champion-channel')
                await utilities.send_message(local_lol_channel, player, utilities.get_champ_name_from_player_id(self, player, server))


# ---------------------------------------------------------------------- #
                
                
async def setup(bot):
    await bot.add_cog(utilities(bot))
    print(f'Module: \"utilities\"\t\t loaded successfully')


# ---------------------------------------------------------------------- #
# Copyright 2024 by Sylvan013 & Anderson4366
