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
    async def DCS(self, ctx, time, date, *,args):
        embed=discord.Embed(title="DCS Digital Combat Simulator", description=f"**Time:** {time}CST \n**Date:** {date} \n**Organizer:** <@{ctx.message.author.id}>\n\n**Mission Description:** \n{args} \n\nReact ✅ to participate")
        await ctx.send("<@&871957137587314761>")
        msg1 = await ctx.send(embed=embed)
        await msg1.add_reaction('✅')
        await ctx.message.delete()

def setup(client):
    client.add_cog(Main(client))