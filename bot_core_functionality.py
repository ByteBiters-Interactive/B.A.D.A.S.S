# ---------------------------------------------------------------------- #
# -----------------------------B.A.D.A.S.S------------------------------ #
# ---------------------------------------------------------------------- #

# Imports
import json
from discord.ext import commands, tasks
from datetime import datetime

# Variables
try:
    with open('resources/config.json', 'r') as file:
        config_data = json.load(file)
except FileNotFoundError:
    print(f'The file \'resources/config.json\' does not exist.')
    exit()
except Exception as error:
    print(f'An error occurred while loading config data: {error}')
    exit()

try:
    iteration_cycle = config_data.get('iteration_cycle', '1')
except Exception as error:
    print(f'An error ocured while reading \'game_scope\' from config data: ({error}), continuing with deafult value of 1 minute')

core_loop_index = 0
core_loop_minutes_formated = 0 # does only work if iteration_cycle is set to 1
# ---------------------------------------------------------------------- #

            
class core(commands.Cog):
    def __init__(self, bot):
            self.bot = bot


    @tasks.loop(minutes = int(iteration_cycle))
    async def do_your_stuff(self):
        from bot_utilities import utilities
        import bot_core_functionality
        bot_core_functionality.core_loop_minutes_formated = '{:02d}:{:02d}'.format(*divmod(bot_core_functionality.core_loop_index, 60))
        print(f'[{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}]\t Background-loop cycle: {bot_core_functionality.core_loop_index} \t Runtime: {bot_core_functionality.core_loop_minutes_formated}')
        utilities.league_checker(self)
        await utilities.announce_players(self)
        bot_core_functionality.core_loop_index += 1 


# ---------------------------------------------------------------------- #
        

async def setup(bot):
    await bot.add_cog(core(bot))
    print(f'Module: \"core\" \t\t\t loaded successfully')


# ---------------------------------------------------------------------- #
# Copyright 2024 by Sylvan013 & Anderson4366
