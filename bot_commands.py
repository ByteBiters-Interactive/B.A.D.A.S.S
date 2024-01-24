# ---------------------------------------------------------------------- #
# -----------------------------B.A.D.A.S.S------------------------------ #
# ---------------------------------------------------------------------- #

# Imports
from discord.ext import commands
from bot_core_functionality import core
from datetime import datetime

# ---------------------------------------------------------------------- #
     
            
class bot_commands(commands.Cog):
    def __init__(self, bot):
            self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send('Pong!')
        print(f'[{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}]: \'!ping\' command was called on \'{ctx.guild}\'.')

    @commands.command()
    async def status(self, ctx):
        number_of_servers = 0 
        for servers in self.bot.guilds:
            number_of_servers = number_of_servers + 1
        await ctx.send(f'B.A.D.A.S.S is Online & registered on {number_of_servers} Servers.')
        print(f'[{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}]: \'!status\' command was called from \'{ctx.guild}\'.')

    @commands.command()
    async def do_stuff(self, ctx):
        from bot_utilities import utilities
        await utilities.announce_players(self)
        print(f'[{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}]: \'!do_stuff\' command was called from \'{ctx.guild}\'.')

    @commands.command()
    async def test(self, ctx):
        from bot_utilities import utilities
        utilities.league_checker(self)
        print(f'[{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}]: \'!test\' command was called from \'{ctx.guild}\'.')


# ---------------------------------------------------------------------- #
        

async def setup(bot):
    await bot.add_cog(bot_commands(bot))
    print(f'Module: \"bot_commands\" \t\t loaded successfully')


# ---------------------------------------------------------------------- #
# Copyright 2024 by Sylvan013 & Anderson4366
