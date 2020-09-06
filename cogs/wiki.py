from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import os
import datetime
import random
import wikipedia
import discord


class wiki(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Wikipedia Cog has been loaded\n-----")

    @commands.command()
    async def kimdir(self,ctx,word):
        def viki_sum(arg):
            definition = wikipedia.summary(arg,sentences=3,chars=1000)
            return definition
        embed = discord.Embed(title="***Wiki'de Bulduklarım:***",description=viki_sum(word))
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(wiki(bot))