import os
import sys
import time
import random
import discord
from discord.ext import commands
from discord.ext import tasks
from discord import Member
from discord.ext.commands import has_permissions
from discord.ext.commands import MissingPermissions
from discord.utils import find
from discord.utils import get
import asyncio
from datetime import datetime
import json

cogs = [
    'cogs.Arma',
    'cogs.cc',
    'cogs.cotw',
    'cogs.DCS',
    'cogs.Starbase',
    'cogs.stationeers',
    'cogs.wolfpack',
    'cogs.help',
    'cogs.about',
    'events.add_role'
]

class client(commands.AutoShardedBot):
    def __init__(self):
        with open("settings.json", "r") as f:
            settings = json.load(f)
        self.token = settings['token']
        self.prefix = settings['prefix']
        
        intents = discord.Intents(messages=True, guilds=True)
        intents.typing = False
        intents.presences = False
        intents.reactions = True

        super().__init__(command_prefix=self.prefix, case_insensitive=True, intents=intents)
        self.devs = [
            291360056002215937
        ]
        self.version = settings['version']

    async def on_ready(self):
        #await client.change_presence(status=discord.Status.online, activity=discord.Game(''))
        await client.change_presence(status=discord.Status.online)
        #await client.change_presence(status=discord.Status.dnd, activity=discord.Game('In Development'))
        #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=""))

        print()
        print("-------------------------------")
        print("Bot Online")
        print('Logged In As: ',client.user.name)
        print('ID: ',client.user.id)
        print('Bot Version: ',self.version)
        print('Discord Version: ',discord.__version__)
        print('-------------------------------')
        print()
        print()

        for cog in cogs:
            try:
                client.load_extension(cog)
                print(f"Loaded {cog}")
            except Exception as e:
                print(f"Error Loading {cog}. Error is {e}")

client = client()
client.remove_command('help')


@client.command(pass_context=True)
async def reload(ctx, cog=None):
    if not int(ctx.author.id) in client.devs:
        print("Reload Cogs failed wrong person")
        embed=discord.Embed(title="Error", description=f"You must be a developer to reload a cog", color=client.red)
        msg = await ctx.send(embed=embed)
        await asyncio.sleep(5)
        await msg.delete()
    else:
        if not cog:
            return
        else:
            try:
                print("Reloading Cogs")
                client.reload_extension(cog)
                await ctx.message.add_reaction('✅')
                msg = await ctx.send(f"Reloading **{cog}**")
                await asyncio.sleep(20)
                await msg.delete()
            except Exception as e:
                await ctx.message.add_reaction('❌')
                msg = await ctx.send(f"<@291360056002215937> Error **{cog}**!\n```{e}```")
                dev_logs = client.get_channel(665553350355582986)
                mod_logs = client.get_channel(477356858051526656)
                await asyncio.sleep(20)
                await msg.delete()
                await dev_logs.send(f"<@291360056002215937> Error **{cog}**!\n```{e}```")
                await mod_logs.send(f"<@291360056002215937> Error **{cog}**!\n```{e}```")

client.run(client.token)