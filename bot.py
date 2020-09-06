import discord
import string
import random
import asyncio
import os
from discord.ext import commands
from discord.utils import get
from discord.ext.commands import Bot
import datetime
import pendulum
from discord import Spotify
from pathlib import Path
from asyncio import sleep

client = commands.Bot(command_prefix="j!")
admin = client.get_guild("346613100356567041")
client.remove_command('help')
link = "https://discord.com/oauth2/authorize?client_id=719936787790823497&permissions=8&scope=bot"
sunucu = "https://discord.gg/cQtcDhh"

cwd = Path(__file__).parents[0]
cwd = str(cwd)

for filename in os.listdir(cwd+'/cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


@ client.command()
async def spotify(ctx, user: discord.Member = None):
    user = user or ctx.author
    for activity in user.activities:
        if isinstance(activity, Spotify):
            em = discord.Embed(color=activity.color)
            em.title = f'{user.name}, {activity.title} dinliyor.'
            em.set_thumbnail(url=activity.album_cover_url)
            em.description = f"**Şarkı Adı**: {activity.title}\n**Sanatçı**: {activity.artist}\n**Albüm**: {activity.album}\n**Şarkı Uzunluğu**: {pendulum.duration(seconds=activity.duration.total_seconds()).in_words(locale='en')}"
            await ctx.send(embed=em)
            break
    else:
        embed = discord.Embed(color=0xff0000)
        embed.title = f'{user.name} şu anda Spotify dinlemiyor!'
        await ctx.send(embed=embed)


@ client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('j!help'))
    print("Bot hazır!")


@ client.event
async def on_member_join(member):
        if member.guild.id == 723325209456672819:
            role = get(member.guild.roles, name='Member')
            await member.add_roles(role)


@ client.event
async def on_raw_reaction_add(payload):
    message_id = payload.message_id
    if message_id == 739497359741943860:

        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)

        if payload.emoji.name == 'verify':
            role = discord.utils.get(guild.roles, name='Verified Member')

        role2 = discord.utils.get(guild.roles, name='Member')

        if role is not None:
            print(role.name + " was found!")
            print(role.id)
            member = discord.utils.find(
                lambda m: m.id == payload.user_id, guild.members)
            await member.add_roles(role)
            await member.remove_roles(role2)


@ client.command()
@ commands.cooldown(1, 5, commands.BucketType.guild)
async def sence(ctx, *, question):
    cevaplar = ["Kesinlikle!",
                "Bunun gerçek olmadığını sen de biliyorsun.",
                "Allah yardım etsin",
                "hulk gercekmi?",
                "Caz yapma yavşak",
                "Sormadın sayıyorum, devam et",
                "Şüphesiz.",
                "Hele yarrama bak hele",
                "Biraz içerlemiş gibisin Eruhlu?",
                "BOHOHOHOHOHYT RECPE İWEDKE 😂😂😂😂"]
    await ctx.send(f'{random.choice(cevaplar)}')


@ client.command()
@ commands.cooldown(1, 5, commands.BucketType.guild)
async def info(ctx):
    dpyVersion = discord.__version__
    serverCount = len(client.guilds)
    memberCount = len(set(client.get_all_members()))
    embed = discord.Embed(
        title=f'{client.user.name} istatistik', description="Amazoen#0001", timestamp=ctx.message.created_at, colour=discord.Colour.red())

    embed.add_field(name='***discord.py Versiyonu:***',
                    value=dpyVersion, inline=False)
    embed.add_field(name='***Botu Kullanan Sunucu Sayısı:***',
                    value=serverCount, inline=False)
    embed.add_field(name='***Botu Kullanan Kullanıcı Sayısı:***',
                    value=memberCount, inline=False)
    embed.add_field(name=":space_invader:***Destek Sunucusu***",
                    value=f'[:space_invader: Davet!]({sunucu})', inline=False)
    embed.add_field(name=":mailbox_with_mail: ***Sunucuna Ekle***",
                    value=f'[:e_mail: Link!]({link})', inline=False)

    embed.set_author(name=client.user.name, icon_url=client.user.avatar_url)
    embed.set_footer(text='jos')
    await ctx.send(embed=embed)


@ client.command()
@ commands.cooldown(1, 5, commands.BucketType.guild)
async def avatar(ctx, member: discord.Member = None):
    member = member or ctx.author
    show_avatar = discord.Embed(color=discord.Color.dark_blue())
    show_avatar.set_image(url='{}'.format(member.avatar_url))

    await ctx.send(embed=show_avatar)


@ client.command()
async def userinfo(ctx, member: discord.Member = None):
    member = member or ctx.author
    roles = [role for role in member.roles]
    embed = discord.Embed(colour=member.color,
                          timestamp=ctx.message.created_at)

    embed.set_author(name=f"Kullanıcı Adı:\n{member}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(
        text=f"Talep Eden {ctx.author}", icon_url=ctx.author.avatar_url)
    embed.add_field(name="ID:", value=member.id, inline=False)
    embed.add_field(name="Kullanıcı Adı:",
                    value=member.display_name, inline=False)
    embed.add_field(name="Sunucuya Katıldığı Tarih:",
                    value=member.joined_at.strftime("%m,%d,%Y"), inline=False)
    embed.add_field(name=f"Rol / Roller ({len(roles)})", value=" ".join(
        [role.mention for role in roles]), inline=False)
    embed.add_field(name="Bot?", value=member.bot, inline=False)
    embed.set_footer(
        text=f"Talep Eden {ctx.author}", icon_url=ctx.author.avatar_url)

    await ctx.send(embed=embed)


@ client.command()
async def serverinfo(ctx):
    guild = ctx.guild
    embed = discord.Embed(title=f'{guild} sunucusunun bilgileri', description="Coded by Amazoen#1907",
                          timestamp=ctx.message.created_at, color=discord.Color.red())

    embed.set_thumbnail(url=guild.icon_url)
    embed.add_field(name="Kanal Sayısı:", value=len(
        guild.channels), inline=False)
    embed.add_field(name="Rol Sayısı:", value=len(guild.roles), inline=False)
    embed.add_field(name="Booster Sayısı:",
                    value=guild.premium_subscription_count, inline=False)
    embed.add_field(name="Üye Sayısı:", value=guild.member_count, inline=False)
    embed.add_field(name="Kuruluş Tarihi:",
                    value=guild.created_at.strftime("%m,%d,%Y"), inline=False)
    embed.add_field(name="Sunucu Sahibi:", value=guild.owner, inline=False)
    embed.add_field(name="Gecikme", value=f'{round(client.latency *1000)} ms')
    embed.set_footer(
        text=f"Komut {ctx.author} tarafından kullanıldı.", icon_url=ctx.author.avatar_url)
    embed.add_field(name=":space_invader:***Destek Sunucusu***",
                    value=f'[:space_invader: Davet!]({sunucu})', inline=False)
    embed.add_field(name=":mailbox_with_mail: ***Sunucuna Ekle***",
                    value=f'[:e_mail: Link!]({link})', inline=False)

    await ctx.send(embed=embed)


@ client.command()
async def say(ctx, *args):
    msg = str(' '.join(args))
    await ctx.message.delete()
    if "@everyone" in msg:
        await ctx.send("`İyi deneme :d`", delete_after=5)
        return
    elif "@here" in msg:
        await ctx.send("`Bunun işe yarayacağını mı düşündün?`", delete_after=5)
    else:
        await ctx.send(msg)

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! Bu işlem {round(client.latency *1000)} ms sürdü.')
    
client.run("x")