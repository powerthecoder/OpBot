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
    async def wolfpack(self, ctx, time, date, *,args):
        embed=discord.Embed(title="Wolfpack", description=f"**Time:** {time}CST \n**Date:** {date} \n\n**Mission Description:** \n{args} \nReact to participate")
        await ctx.send("<@&871957352373432322>")
        msg1 = await ctx.send(embed=embed)
        await msg1.add_reaction('✅')

def setup(client):
    client.add_cog(Main(client))