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

    
    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        if reaction.message.channel.id == 871967320044617779:
            if reaction.emoji == "🌶️":
                Arma = discord.utils.get(user.server.roles, name="Arma")
                await client.add_roles(user, Arma)
            elif reaction.emoji == ":two:":
                DCS = discord.utils.get(user.server.roles, name="DCS")
                await client.add_roles(user, DCS)
            elif reaction.emoji == ":three:":
                Starbase = discord.utils.get(user.server.roles, name="Starbase")
                await client.add_roles(user, Starbase)
            elif reaction.emoji == ":four:":
                stationeers = discord.utils.get(user.server.roles, name="stationeers")
                await client.add_roles(user, stationeers)
            elif reaction.emoji == ":five:":
                cotw = discord.utils.get(user.server.roles, name="cotw")
                await client.add_roles(user, cotw)
            elif reaction.emoji == ":six:":
                wolfpack = discord.utils.get(user.server.roles, name="wolfpack")
                await client.add_roles(user, wolfpack)
            elif reaction.emoji == ":seven:":
                cc = discord.utils.get(user.server.roles, name="cc")
                await client.add_roles(user, cc)
            else:
                pass
        else:
            pass
    
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        guild = payload.guild_id
        member = payload.member
        if (payload.channel_id == 871967320044617779):
            if (str(payload.emoji) == "1️⃣"):
                role = discord.utils.get(member.guild.roles, name="Arma")
                await payload.member.add_roles(role)
            elif (str(payload.emoji) == "2️⃣"):
                role = discord.utils.get(member.guild.roles, name="DCS")
                await payload.member.add_roles(role)
            elif (str(payload.emoji) == "3️⃣"):
                role = discord.utils.get(member.guild.roles, name="Starbase")
                await payload.member.add_roles(role)
            elif (str(payload.emoji) == "4️⃣"):
                role = discord.utils.get(member.guild.roles, name="stationeers")
                await payload.member.add_roles(role)
            elif (str(payload.emoji) == "5️⃣"):
                role = discord.utils.get(member.guild.roles, name="cotw")
                await payload.member.add_roles(role)
            elif (str(payload.emoji) == "6️⃣"):
                role = discord.utils.get(member.guild.roles, name="wolfpack")
                await payload.member.add_roles(role)
            elif (str(payload.emoji) == "7️⃣"):
                role = discord.utils.get(member.guild.roles, name="cc")
                await payload.member.add_roles(role)
            else:
                pass
        else:
            pass
            
    
    #@commands.command()
    #async def embed(self,ctx):
    #    embed=discord.Embed(title="Choose Your Game", description=f":one: Arma \n:two: DCS \n:three: Starbase \n:four: stationeers \n:five: Hunter Call of the Wild \n:six: Wolfpack \n:seven: Carrier Command")
    #    msg = await ctx.send(embed=embed)

    
    

def setup(client):
    client.add_cog(Main(client))