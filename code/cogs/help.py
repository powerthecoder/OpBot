import os
import sys
import time
import random
import discord
from discord.ext import commands
from discord.ext import tasks
from discord import Member
from discord.ext.commands import has_permissions
from discord.ext.commands import has_role
from discord.ext.commands import MissingPermissions
from discord.utils import find
from discord.utils import get
import asyncio
import json

class Main(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def help(self,ctx):
        embed=discord.Embed(title="Carrier Command", description=f"**Help Menu** \n\n**Command Ussage**:\n-game <time> <date> <description>\nComamnd Example:\n-dcs 2000 1/2/3 Mission Description \n\n\n**Games:**\n Arma\n DCS\n Starbase\n stationeersn\n cotw (Hunter Call of the wild)\n Wolfpack\n cc (Carrier Command)")
        msg1 = await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Main(client))