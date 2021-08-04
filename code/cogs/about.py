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
    async def about(self, ctx):
        embed=discord.Embed(title="Discord Bot Developer", description="**Developer:** <@291360056002215937> \n**Name:** Leo Power \n**GitHub**: https://github.com/powerthecoder")
        embed.set_author(name="About")
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Main(client))