import discord
from discord.ext import commands
from discord import Spotify
import time
import typing
import asyncio
import random
from aiohttp import ClientSession
import datetime
import time
import aiohttp
import os
import discord.utils
from discord import Game
import json
import requests
import pendulum
import safygiphy
from typing import Union

class Fun(commands.Cog):

    """{_*Fun Commands*_}"""

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Fun Cog has been loaded\n-----")

    @commands.command()
    @commands.guild_only()
    async def yazıtura(self, ctx):
        """
        `Flip a coin`
        """
        responses = ["Yazı", "Tura"]
        rancoin = random.choice(responses)
        await ctx.send(rancoin)

    @commands.command()
    async def meme(self, ctx):
        fetch = await ctx.send("Meme Bulunuyor:", delete_after=0.5)
        await asyncio.sleep(1)
        req = requests.get("https://apis.duncte123.me/meme")
        meme = req.json()
        embed = discord.Embed(color=discord.Color.dark_blue(),
                              timestamp=datetime.datetime.utcnow())
        embed.set_image(url=meme['data']['image'])
        embed.add_field(name="Quality Meme", value=f"{meme['data']['title']}")
        embed.set_footer(text=f"{meme['data']['url']}")
        await ctx.send(embed=embed)
    
    @commands.command()
    async def gif(self, ctx, gif: str):
        g = safygiphy.Giphy()
        rgif = g.random(tag=gif)
        embed = discord.Embed()
        embed.set_image(
            url=str(rgif.get("data", {}).get('image_original_url')))
        await ctx.send(embed=embed)
    
    
    @commands.command()
    @commands.guild_only()
    async def yumruk(self, ctx, members: commands.Greedy[discord.Member]):
        """
        `Punch somebody for whatever reason`
        """
        punched = ", ".join(x.name for x in members)
        embed = discord.Embed(description="**{}**,**{}** kardeşimizin kroşesinin tadına baktı! ".format(
            punched, ctx.author), color=random.randint(0x000000, 0xffffff))
        await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    async def şamar(self, ctx, members: commands.Greedy[discord.Member]):
        """
        `Slap somebody for whatever reason`
        """
        slapped = ", ".join(x.name for x in members)
        embed = discord.Embed(description="**{}**,**{}**'a ***ŞAAAK*** diye indirdi. ".format(
            ctx.author, slapped), color=random.randint(0x000000, 0xffffff))
        await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    async def iq(self, ctx):
        """
        `Tells you your IQ`
        """
        x = random.randint(1, 200)
        embed = discord.Embed(
            title="IQ seviyen ne 🤨", description=f"Senin IQ düzeyin: {x}", color=random.randint(0x000000, 0xffffff))
        await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    async def dalga(self, ctx):
        try:
            responses = ['8=D\n***Bamyacık***',
                         '8==D\n***İçine kaçmış bu***',
                         '8===D\n***Oyna büyüsün biraz***',
                         '8====D\n***Moral bozma abi***',
                         '8=====D\n***Gideri var***',
                         '8======D\n***Sen yapıyosun bu sporu***',
                         '8=======D\n***Düşman götüne***',
                         '8========D\n***Orospu görse tövbe eder***',
                         '8=========D\n***Herkes götünü korusun***',
                         '8==========D\n***JOHNNY SİNS AMINAKOYUM***']
            embed = discord.Embed(title="Dalga boyun ne kadar?",
                                  description=f'{random.choice(responses)}', color=random.randint(0x000000, 0xffffff))
            await ctx.channel.send(embed=embed)
        except Exception as error:
            raise(error)

    @commands.command()
    async def insta(self, ctx, username):
        url = f'https://apis.duncte123.me/insta/{username}'
        async with ClientSession() as session:
            async with session.get(url) as response:
                r = await response.json()
                data = r['user']
                username = data["username"]
                followers = data["followers"]["count"]
                following = data["following"]["count"]
                uploads = data["uploads"]["count"]
                biography = data["biography"]
                private = data["is_private"]
                verified = data["is_verified"]

                embed = discord.Embed(title=f'Hesap Detayları: {username}')
                embed.add_field(name='Bio', value=biography +
                                '\u200b', inline=False)
                embed.add_field(name='Hesap Gizli mi?',
                                value=private, inline=False)
                embed.add_field(name='Hesap Onaylanmış mı?',
                                value=verified, inline=False)
                embed.add_field(name='Takipçi',
                                value=followers, inline=False)
                embed.add_field(name='Takip Ettiği',
                                value=following, inline=False)
                embed.add_field(name='Gönderiler', value=uploads, inline=False)
                await ctx.send(embed=embed)
                
    @ commands.command()
    async def insta(self, ctx, username):
        url = f'https://apis.duncte123.me/insta/{username}'
        async with ClientSession() as session:
            async with session.get(url) as response:
                r = await response.json()
                data = r['user']
                username = data["username"]
                followers = data["followers"]["count"]
                following = data["following"]["count"]
                uploads = data["uploads"]["count"]
                biography = data["biography"]
                private = data["is_private"]
                verified = data["is_verified"]

                embed = discord.Embed(title=f'Hesap Detayları: {username}')
                embed.add_field(name='Bio', value=biography +
                                '\u200b', inline=False)
                embed.add_field(name='Hesap Gizli mi?',
                                value=private, inline=False)
                embed.add_field(name='Hesap Onaylanmış mı?',
                                value=verified, inline=False)
                embed.add_field(name='Takipçi',
                                value=followers, inline=False)
                embed.add_field(name='Takip Ettiği',
                                value=following, inline=False)
                embed.add_field(name='Gönderiler', value=uploads, inline=False)
                await ctx.send(embed=embed)


    
    @commands.command()
    async def topla(self, ctx, a:int, b:int):
        await ctx.send(a+b)

    @commands.command()
    async def çıkar(self, ctx, a:int, b:int):
        await ctx.send(a-b)

    @commands.command()
    async def çarp(self, ctx, a:int, b:int):
        await ctx.send(a*b)

    @commands.command()
    async def böl(self, ctx, a:int, b:int):
        if b==0:
            ans="0"
        else:
            ans=a/b
        await ctx.send(ans)
        
    @commands.command()
    async def slots(self, ctx):
        """!slots - Play fruit emojis slot machine."""
        icon_url = 'https://i.imgur.com/8oGuoyq.png'
        slots = ['apple', 'watermelon', 'taco',
                 'cherries', 'doughnut', 'grapes']
        slot1 = slots[random.randint(0, 5)]
        slot2 = slots[random.randint(0, 5)]
        slot3 = slots[random.randint(0, 5)]
        slot4 = slots[random.randint(0, 5)]

        slot_spin = f'|\t:{slot1}:\t|\t:{slot2}:\t|\t:{slot3}:\t|\t:{slot4}:\t|'
        jackpot = '$$$ !!! JACKPOT !!! $$$'

        embed = discord.Embed(colour=discord.Colour.gold())
        embed.set_author(name='Slot Makinesi', icon_url=icon_url)
        embed.add_field(
            name=f'*{ctx.author.name} hakkını kullanıyor...*',
            value='\u200b',
            inline=False,

        )

        if (
            slot1 == slot2 and slot3 == slot4 or
            slot1 == slot3 and slot2 == slot4 or
            slot1 == slot4 and slot2 == slot3
        ):
            embed.add_field(name=slot_spin, value='\u200b')
            embed.set_footer(text=jackpot)
        else:
            embed.add_field(name=slot_spin, value='\u200b')
        await ctx.send(embed=embed)

    @commands.command(name='bigemoji')
    async def get_emoji_url(self, ctx, emoji: Union[discord.Emoji, discord.PartialEmoji, str]):
        """Sends a big version of an emoji and it's URL of available"""
        if isinstance(emoji, (discord.Emoji, discord.PartialEmoji)):
            await ctx.send(str(emoji.url))
        else:
            await ctx.send(emoji)

def setup(bot):
    bot.add_cog(Fun(bot))